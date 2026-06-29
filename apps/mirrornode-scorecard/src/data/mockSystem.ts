export const mockSystem = {
  status: 'SYSTEM NOMINAL',
  kernel: 'PTAH KERNEL · ACTIVE',
  phase: 'Phase 2',
  metrics: {
    openIncidents: 3,
    acknowledged: 0,
    resolved: 1,
    activeAgents: 4,
  },
  incidents: [
    {
      id: 'INC-003',
      title: 'Frontend Policy Logic Detected',
      severity: 'S1',
      state: 'OPEN',
    },
    {
      id: 'INC-002',
      title: 'Key Mutation Attempt Intercepted',
      severity: 'S1',
      state: 'OPEN',
    },
    {
      id: 'INC-001',
      title: 'Oracle Context Overflow',
      severity: 'S2',
      state: 'OPEN',
    },
  ],
}
