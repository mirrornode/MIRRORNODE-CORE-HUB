import './App.css'
import { config } from './lib/config'
import { mockSystem } from './data/mockSystem'

export default function App() {
  return (
    <main className="app-shell">
      <section className="hero">
        <p className="eyebrow">MIRRORNODE / detached local surface</p>
        <h1>System Integrity Scorecard</h1>
        <p className="lede">
          Local projection shell for Theia event and state APIs.
        </p>

        <div className="card-grid">
          <article className="card">
            <span className="label">System status</span>
            <strong>{mockSystem.status}</strong>
          </article>

          <article className="card">
            <span className="label">Kernel</span>
            <code>{mockSystem.kernel}</code>
          </article>

          <article className="card">
            <span className="label">Phase</span>
            <strong>{mockSystem.phase}</strong>
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
            <strong>{mockSystem.metrics.activeAgents}</strong>
          </article>
        </div>

        <section className="panel">
          <div className="panel-head">
            <h2>Incident Center</h2>
            <span className="panel-meta">
              Open {mockSystem.metrics.openIncidents} · Resolved {mockSystem.metrics.resolved}
            </span>
          </div>

          <div className="incident-list">
            {mockSystem.incidents.map((incident) => (
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
