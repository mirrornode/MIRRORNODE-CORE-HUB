import { mockSystem } from '../data/mockSystem'

export type ScorecardSystem = typeof mockSystem

export async function getSystemSnapshot(): Promise<ScorecardSystem> {
  return mockSystem
}
