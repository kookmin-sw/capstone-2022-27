import adapter from '@sveltejs/adapter-auto';

/** @type {import('@sveltejs/kit').Config} */
const config = {
	kit: {
		adapter: adapter(),
		vite: () => ({
			server: {
				proxy: {
					'/api/': {
						target: 'http://127.0.0.1:3001',
						secure: false,
						changeOrigin: true,
					}
				}
			}
		})
	}
}

export default config;
