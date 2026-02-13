/** @type {import('next').NextConfig} */
const nextConfig = {
  typescript: {
    ignoreBuildErrors: true,
  },
  images: {
    unoptimized: true,
  },
  async rewrites() {
    return [
      {
        source: '/',
        destination: '/index.html',
      },
      {
        source: '/hakkimizda',
        destination: '/hakkimizda.html',
      },
      {
        source: '/iletisim',
        destination: '/iletisim.html',
      },
      {
        source: '/cozumler',
        destination: '/cozumler.html',
      },
      {
        source: '/guvenlik-kvkk',
        destination: '/guvenlik-kvkk.html',
      },
      {
        source: '/kullanim-senaryolari',
        destination: '/kullanim-senaryolari.html',
      },
      {
        source: '/nasil-calisir',
        destination: '/nasil-calisir.html',
      },
      {
        source: '/ozellikler',
        destination: '/ozellikler.html',
      },
      {
        source: '/sss',
        destination: '/sss.html',
      },
    ]
  },
}

export default nextConfig
