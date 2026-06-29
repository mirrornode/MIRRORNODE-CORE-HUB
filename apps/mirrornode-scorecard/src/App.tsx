import './App.css'
import { useEffect, useState } from 'react'
import { config } from './lib/config'
import { getSystemSnapshot, type ScorecardSource, type ScorecardSystem } from './lib/systemAdapter'

export default function App() {
  const [system, setSystem] = useState<ScorecardSystem | null>(null)
  const [source, setSource] = useState<ScorecardSource | null>(null)

  useEffect(() => {
    getSystemSnapshot().then(({ system, source }) => {
      setSystem(system)
      setSource(source)
    })
  }, [])

  if (!system) {
    return (
      <main className="app-shell">
        <section className="hero">
          <p className="eyebrow">MIRRORNODE / detached local surface</p>
          <h1>System Integrity Scorecard</h1>
          <p className="lede">Loading local system snapshot...</p>
        </section>
      </main>
    )
  }

  const live = source === 'live endpoint'

  return (
    <main className="app-shell">
      <section className="hero">
        <div className="hero-topline">
          <p className="eyebrow">MIRRORNODE / detached local surface</p>
          <div className={`source-badge ${live ? 'live' : 'mock'}`}>
            <span className="source-dot" />
            <span className="source-label">{source}</span>
          </div>
        </div>

        <h1>System Integrity Scorecard</h1>
        <p className="lede">
          Local projection shell for Theia event and state APIs.
        </p>

        <div className="card-grid">
          <article className="card">
            <span className="label">System status</span>
            <strong>{system.status}</strong>
          </article>

          <article className="card">
            <span className="label">Kernel</span>
            <code>{system.kernel}</code>
          </article>

          <article className="card">
            <span className="label">Phase</span>
            <strong>{system.phase}</strong>
          </article>

          <article className="card">
            <span className="label">API base URL</span>
            <code>{config.apiBaseUrl}</code>
          </article>

          <article className="card">
            <span className="label">WebSocket URL</span>
            <code>{config.wsUrl}</code>
          </article>

          <article className="card">
            <span className="label">Active agents</span>
            <strong>{system.metrics.activeAgents}</strong>
          </article>
        </div>

        <section className="panel">
          <div className="panel-head">
            <h2>Incident Center</h2>
            <span className="panel-meta">
              Open {system.metrics.openIncidents} · Resolved {system.metrics.resolved}
            </span>
          </div>

          <div className="incident-list">
            {system.incidents.map((incident) => (
              <article className="incident" key={incident.id}>
                <div>
                  <p className="incident-id">{incident.id}</p>
                  <h3>{incident.title}</h3>
                </div>
                <div className="incident-tags">
                  <span className="tag">{incident.severity}</span>
                  <span className="tag muted">{incident.state}</span>
                </div>
              </article>
            ))}
          </div>
        </section>
      </section>
    </main>
  )
}
