import { config } from './config'
import { mockSystem } from '../data/mockSystem'

export type ScorecardSystem = typeof mockSystem

export async function getSystemSnapshot(): Promise<ScorecardSystem> {
  try {
    const response = await fetch(`${config.apiBaseUrl}/api/mirror/system`)

    if (!response.ok) {
      throw new Error(`HTTP ${response.status}`)
    }

    const data = await response.json()
    return data as ScorecardSystem
  } catch {
    return mockSystem
  }
}
