"""
OSIRIS AUDIT ARTIFACT SCHEMA v1.0.0

Legal Position: Constrained static audits only
- No compliance certification
- No runtime behavior claims
- Explicit constraints documented

Last Updated: 2026-01-26
Status: PRODUCTION READY
"""

from pydantic import BaseModel, Field, validator
from typing import List, Dict, Optional, Literal, Any
from datetime import datetime
from enum import Enum
import hashlib
import json

try:
    import ulid
except ImportError:
    # Fallback ID generation if ulid not available
    import uuid
    class ulid:
        @staticmethod
        def new():
            return uuid.uuid4().hex.upper()

# ================================================================
# ENUMERATIONS (V1 CONSTRAINED)
# ================================================================

class ClaimType(str, Enum):
    """
    Categories of audit claims (v1 constrained).
    
    Invariants:
    - COMPLIANCE removed (use GOVERNANCE for policy alignment)
    - Categories reflect static analysis only
    
    UI Display:
    - SECURITY → "Security (Static Analysis Only)"
    - GOVERNANCE → "Governance (Project Policies)"
    """
    SECURITY = "SECURITY"           # Vulnerability/exposure patterns
    GOVERNANCE = "GOVERNANCE"       # Project policy alignment
    QUALITY = "QUALITY"            # Code quality metrics
    ARCHITECTURE = "ARCHITECTURE"   # Structural patterns

class EvidenceType(str, Enum):
    """
    Types of supporting evidence (v1 constrained).
    
    Invariants:
    - BEHAVIOR excluded from v1 (gated for v2+)
    - v1 focuses on static artifacts only
    """
    CODE = "CODE"              # Source code inspection
    METADATA = "METADATA"      # Package.json, configs, manifests
    ABSENCE = "ABSENCE"        # Verified non-existence via search

class FindingStatus(str, Enum):
    """Claim verification outcomes"""
    SUPPORTED = "SUPPORTED"          # Evidence supports claim
    UNSUPPORTED = "UNSUPPORTED"      # Evidence contradicts claim
    PARTIAL = "PARTIAL"              # Mixed evidence
    UNVERIFIABLE = "UNVERIFIABLE"    # Insufficient evidence

class RiskSeverity(str, Enum):
    """Risk impact levels"""
    CRITICAL = "CRITICAL"
    HIGH = "HIGH"
    MEDIUM = "MEDIUM"
    LOW = "LOW"
    INFO = "INFO"

# ================================================================
# ID GENERATION (ULID-BASED)
# ================================================================

def generate_claim_id() -> str:
    """Generate unique claim ID: CLAIM-<ULID>"""
    return f"CLAIM-{ulid.new()}"

def generate_evidence_id() -> str:
    """Generate unique evidence ID: EVIDENCE-<ULID>"""
    return f"EVIDENCE-{ulid.new()}"

def generate_finding_id() -> str:
    """Generate unique finding ID: FINDING-<ULID>"""
    return f"FINDING-{ulid.new()}"

def generate_risk_id() -> str:
    """Generate unique risk ID: RISK-<ULID>"""
    return f"RISK-{ulid.new()}"

# ================================================================
# CORE ENTITIES
# ================================================================

class AuditTarget(BaseModel):
    """
    Target scope and constraints for this audit.
    
    Invariants:
    - repositories must be non-empty
    - constraints explicitly document what was NOT analyzed
    """
    repositories: List[str] = Field(..., min_items=1)
    scope: List[str] = Field(
        default_factory=list,
        description="Paths/patterns included in analysis"
    )
    constraints: Dict[str, Any] = Field(
        default_factory=dict,
        description="Explicit limitations (e.g., runtime_access=false)"
    )

class EngineInfo(BaseModel):
    """Engine version and configuration"""
    version: str = Field(..., regex=r"^\d+\.\d+\.\d+$")
    commit: Optional[str] = None
    analyzers: List[str] = Field(
        default_factory=list,
        description="Analyzer names with versions (e.g., 'secret-detector@1.0.0')"
    )

class AuditMetadata(BaseModel):
    """
    Metadata describing the audit run.
    
    Invariants:
    - version must match semver pattern
    - timestamp must be UTC
    - hud_compat defines minimum HUD version
    """
    version: str = Field(..., regex=r"^\d+\.\d+\.\d+$")
    timestamp: datetime
    run_id: str
    hud_compat: str = Field(..., regex=r"^\d+\.\d+\.\d+$")
    
    target: AuditTarget
    engine: EngineInfo


class Claim(BaseModel):
    """
    A testable assertion about the target system.
    
    Invariants:
    - id follows pattern CLAIM-<ULID> (26-char base32)
    - confidence in range [0.0, 1.0]
    - all evidence_ids must resolve to Evidence entities
    """
    id: str = Field(..., regex=r"^CLAIM-[0-9A-HJKMNP-TV-Z]{26}$")
    type: ClaimType
    statement: str = Field(..., min_length=1)
    source: str = Field(..., description="Analyzer that produced this claim")
    confidence: float = Field(..., ge=0.0, le=1.0)
    
    evidence_ids: List[str] = Field(default_factory=list)
    finding_id: Optional[str] = None
    risk_ids: List[str] = Field(default_factory=list)


class EvidenceLocation(BaseModel):
    """Location of evidence artifact"""
    repository: str
    path: Optional[str] = None
    commit: Optional[str] = None
    url: Optional[str] = None


class Evidence(BaseModel):
    """
    Observable fact supporting or refuting a claim.
    
    Invariants:
    - id follows pattern EVIDENCE-<ULID>
    - location required for CODE/METADATA types
    - search_criteria required for ABSENCE type
    """
    id: str = Field(..., regex=r"^EVIDENCE-[0-9A-HJKMNP-TV-Z]{26}$")
    type: EvidenceType
    description: str
    
    location: Optional[EvidenceLocation] = None
    search_criteria: Optional[List[str]] = Field(
        None,
        description="For ABSENCE: what was searched and not found"
    )
    
    claim_ids: List[str] = Field(default_factory=list)
    finding_ids: List[str] = Field(default_factory=list)
    
    @validator('location', always=True)
    def validate_location_for_type(cls, v, values):
        """CODE/METADATA require location, ABSENCE requires search_criteria"""
        evidence_type = values.get('type')
        if evidence_type in (EvidenceType.CODE, EvidenceType.METADATA):
            if not v:
                raise ValueError(f"{evidence_type} evidence requires location")
        return v
    
    @validator('search_criteria', always=True)
    def validate_search_for_absence(cls, v, values):
        """ABSENCE evidence requires search_criteria"""
        if values.get('type') == EvidenceType.ABSENCE and not v:
            raise ValueError("ABSENCE evidence requires search_criteria")
        return v


class Finding(BaseModel):
    """
    Verdict on a claim based on collected evidence.
    
    Invariants:
    - id follows pattern FINDING-<ULID>
    - claim_id must resolve to existing Claim
    - confidence in range [0.0, 1.0]
    """
    id: str = Field(..., regex=r"^FINDING-[0-9A-HJKMNP-TV-Z]{26}$")
    claim_id: str
    status: FindingStatus
    reasoning: str = Field(..., min_length=1)
    
    evidence_ids: List[str] = Field(default_factory=list)
    confidence: float = Field(..., ge=0.0, le=1.0)
    risk_ids: List[str] = Field(default_factory=list)


class CauseChain(BaseModel):
    """Links risk to its root claim and finding"""
    claim_id: str
    finding_id: str


class Risk(BaseModel):
    """
    Identified vulnerability or concern with mitigation guidance.
    
    Invariants:
    - id follows pattern RISK-<ULID>
    - cause_chain must reference existing entities
    """
    id: str = Field(..., regex=r"^RISK-[0-9A-HJKMNP-TV-Z]{26}$")
    severity: RiskSeverity
    category: str
    description: str
    
    cause_chain: CauseChain
    mitigation: List[str] = Field(default_factory=list)
    finding_ids: List[str] = Field(default_factory=list)


# ================================================================
# ROOT ARTIFACT
# ================================================================

class AuditArtifact(BaseModel):
    """
    Complete immutable audit artifact.
    
    Invariants:
    - All entity IDs unique within their type
    - All cross-references resolve
    - Artifact immutable after validation
    
    Verification: Engine validates before emission
    """
    metadata: AuditMetadata
    claims: List[Claim]
    evidence: List[Evidence]
    findings: List[Finding]
    risks: List[Risk]
    
    @validator('claims', 'evidence', 'findings', 'risks')
    def validate_unique_ids(cls, entities):
        """Ensure all IDs unique within entity type"""
        ids = [e.id for e in entities]
        if len(ids) != len(set(ids)):
            raise ValueError("Duplicate entity IDs detected")
        return entities
    
    def validate_references(self) -> None:
        """
        Validate all cross-references resolve.
        MUST be called by Engine before emission.
        
        Raises:
            AssertionError if any reference is invalid
        """
        claim_ids = {c.id for c in self.claims}
        evidence_ids = {e.id for e in self.evidence}
        finding_ids = {f.id for f in self.findings}
        risk_ids = {r.id for r in self.risks}
        
        # Validate Claim references
        for claim in self.claims:
            for eid in claim.evidence_ids:
                assert eid in evidence_ids, \
                    f"Claim {claim.id} references non-existent {eid}"
            if claim.finding_id:
                assert claim.finding_id in finding_ids, \
                    f"Claim {claim.id} references non-existent finding {claim.finding_id}"
            for rid in claim.risk_ids:
                assert rid in risk_ids, \
                    f"Claim {claim.id} references non-existent {rid}"
        
        # Validate Evidence references
        for evidence in self.evidence:
            for cid in evidence.claim_ids:
                assert cid in claim_ids, \
                    f"Evidence {evidence.id} references non-existent {cid}"
            for fid in evidence.finding_ids:
                assert fid in finding_ids, \
                    f"Evidence {evidence.id} references non-existent {fid}"
        
        # Validate Finding references
        for finding in self.findings:
            assert finding.claim_id in claim_ids, \
                f"Finding {finding.id} references non-existent claim {finding.claim_id}"
            for eid in finding.evidence_ids:
                assert eid in evidence_ids, \
                    f"Finding {finding.id} references non-existent {eid}"
            for rid in finding.risk_ids:
                assert rid in risk_ids, \
                    f"Finding {finding.id} references non-existent {rid}"
        
        # Validate Risk references
        for risk in self.risks:
            assert risk.cause_chain.claim_id in claim_ids, \
                f"Risk {risk.id} cause_chain references non-existent claim"
            assert risk.cause_chain.finding_id in finding_ids, \
                f"Risk {risk.id} cause_chain references non-existent finding"
            for fid in risk.finding_ids:
                assert fid in finding_ids, \
                    f"Risk {risk.id} references non-existent {fid}"
    
    def compute_hash(self) -> str:
        """
        Compute SHA-256 hash of canonical JSON representation.
        Used for integrity verification.
        """
        canonical = json.dumps(
            self.dict(),
            sort_keys=True,
            separators=(',', ':'),
            default=str
        )
        return hashlib.sha256(canonical.encode()).hexdigest()
    
    class Config:
        json_encoders = {
            datetime: lambda v: v.isoformat()
        }
