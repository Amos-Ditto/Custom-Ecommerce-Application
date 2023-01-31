/** @type {import('tailwindcss').Config} */

const colors = require("tailwindcss/colors");

module.exports = {
	content: ["./components/**/*.{js,vue,ts}", "./layouts/**/*.vue", "./pages/**/*.vue", "./plugins/**/*.{js,ts}", "./nuxt.config.{js,ts}"],
	theme: {
		extend: {
			colors: {
				"app-bg": "rgb(242, 236, 235)",
			},
			transitionProperty: {
				length: "height, width",
				spacing: "margin, padding",
			},
		},
	},
	darkMode: "class",
	plugins: [require("@tailwindcss/line-clamp")],
};
