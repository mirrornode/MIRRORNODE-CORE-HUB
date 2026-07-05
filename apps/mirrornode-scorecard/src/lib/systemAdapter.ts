import { config } from './config'
import { mockSystem } from '../data/mockSystem'

export type ScorecardSystem = typeof mockSystem
export type ScorecardSource = 'live endpoint' | 'mock fallback'
export type EndpointHealth = 'online' | 'degraded'

export async function getSystemSnapshot(): Promise<{
  system: ScorecardSystem
  source: ScorecardSource
  health: EndpointHealth
  syncedAt: string
}> {
  const syncedAt = new Date().toISOString()

  try {
    const response = await fetch(`${config.apiBaseUrl}/api/mirror/system`)

    if (!response.ok) {
      throw new Error(`HTTP ${response.status}`)
    }

    const data = await response.json()
    return {
      system: data as ScorecardSystem,
      source: 'live endpoint',
      health: 'online',
      syncedAt,
    }
  } catch {
    return {
      system: mockSystem,
      source: 'mock fallback',
      health: 'degraded',
      syncedAt,
    }
  }
}
