# OSIRIS Release Surface Status

The CORE-HUB OSIRIS release workflow is currently **verification-enabled and release-disabled**.

- Charter receipt verification is required and must fail closed on a name, authority, or SHA-256 mismatch.
- `osiris/Dockerfile` is not present in CORE-HUB, so image build, signing, integration-test, promotion, and publication jobs must not execute.
- Adding a Docker release surface is a separate implementation action and is not implied by a green verification run.

This file also provides a bounded path trigger for re-proving the OSIRIS workflow after repair without altering the signed charter or its receipt.
