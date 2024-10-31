import { join } from 'path'

import forms from '@tailwindcss/forms';
import typography from '@tailwindcss/typography';
import { skeleton } from '@skeletonlabs/tw-plugin'
/** @type {import('tailwindcss').Config} */
export default {
	darkMode: 'class',
	content: ['./src/**/*.{html,js,svelte,ts}', join(require.resolve('@skeletonlabs/skeleton'), '../**/*.{html,js,svelte,ts}'),'./node_modules/flowbite-svelte/**/*.{html,js,svelte,ts}'],
	theme: {
		extend: {},
	},
	plugins: [
		require('flowbite/plugin'),
		forms,
		typography,
		skeleton({
			themes: {
				preset: 
					[ "skeleton", "wintry", "modern" ,
					{
						name: 'skeleton',
						enhancements: true,
					},
				],
			},
		}),
	],
};
