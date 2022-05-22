import adapter from '@sveltejs/adapter-node';

/** @type {import('@sveltejs/kit').Config} */
const config = {
	kit: {
		adapter: adapter({
			out: 'dist',
		}),
		vite: () => ({
			server: {
				fs: {
					allow: ['..']
				}
			}
		})
	}
}

export default config;
