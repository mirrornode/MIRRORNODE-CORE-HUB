import http from 'node:http'

const system = {
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

const server = http.createServer((req, res) => {
  if (req.url === '/api/mirror/system') {
    res.writeHead(200, { 'Content-Type': 'application/json', 'Access-Control-Allow-Origin': '*' })
    res.end(JSON.stringify(system))
    return
  }

  res.writeHead(404, { 'Content-Type': 'application/json', 'Access-Control-Allow-Origin': '*' })
  res.end(JSON.stringify({ error: 'Not found' }))
})

const port = 8000
server.listen(port, () => {
  console.log(`mirror stub listening on http://localhost:${port}`)
})
