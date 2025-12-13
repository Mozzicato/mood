import type { NextConfig } from "next";

const nextConfig: NextConfig = {
  async rewrites() {
    // In production (Railway), we might need to use the full URL directly in the frontend code
    // or ensure this environment variable is set correctly in the Railway project.
    const backendUrl = process.env.BACKEND_URL || 'https://mood-app-production-bbbc.up.railway.app';
    return [
      {
        source: '/api/:path*',
        destination: `${backendUrl}/:path*`,
      },
    ];
  },
};

export default nextConfig;
