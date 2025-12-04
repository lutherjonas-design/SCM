import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'

const VITE_HOST = process.env.VITE_HOST || true
const VITE_PORT = Number(process.env.VITE_PORT || 5173)
const VITE_USE_POLLING = (process.env.VITE_USE_POLLING ?? 'true').toLowerCase() === 'true'
const VITE_POLL_INTERVAL = Number(process.env.VITE_POLL_INTERVAL || 100)

// Optional HMR overrides (usually not needed)
const VITE_HMR_HOST = process.env.VITE_HMR_HOST
const VITE_HMR_CLIENT_PORT = process.env.VITE_HMR_CLIENT_PORT
  ? Number(process.env.VITE_HMR_CLIENT_PORT)
  : undefined

export default defineConfig({
  plugins: [react()],
  server: {
    host: VITE_HOST,                // '0.0.0.0' or true
    port: VITE_PORT,
    strictPort: true,
    hmr: {
      port: VITE_PORT,
      ...(VITE_HMR_HOST ? { host: VITE_HMR_HOST } : {}),
      ...(VITE_HMR_CLIENT_PORT ? { clientPort: VITE_HMR_CLIENT_PORT } : {}),
    },
    watch: {
      usePolling: VITE_USE_POLLING,
      interval: VITE_POLL_INTERVAL,
    },
  },
})