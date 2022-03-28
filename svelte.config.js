import adapter from '@sveltejs/adapter-static';

/** @type {import('@sveltejs/kit').Config} */
const config = {
	kit: {
		adapter: adapter({
			pages: 'dist',
			assets: 'static',
			fallback: null,
			precompress: false
		}),

		prerender: {
			default: true
		},
		vite: () => ({})
	}
}

export default config;
