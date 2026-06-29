import './App.css'
import { config } from './lib/config'

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
            <span className="label">API base URL</span>
            <code>{config.apiBaseUrl}</code>
          </article>

          <article className="card">
            <span className="label">WebSocket URL</span>
            <code>{config.wsUrl}</code>
          </article>

          <article className="card">
            <span className="label">Status</span>
            <strong>Detached UI running locally</strong>
          </article>
        </div>
      </section>
    </main>
  )
}
