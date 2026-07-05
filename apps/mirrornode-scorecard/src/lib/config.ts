export const config = {
  apiBaseUrl: import.meta.env.VITE_THEIA_API_BASE_URL || 'http://localhost:8000',
  wsUrl: import.meta.env.VITE_THEIA_WS_URL || 'ws://localhost:8000/ws',
}
