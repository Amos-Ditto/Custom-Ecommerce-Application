/** @type {import('tailwindcss').Config} */

module.exports = {
	content: ["./components/**/*.{js,vue,ts}", "./layouts/**/*.vue", "./pages/**/*.vue", "./plugins/**/*.{js,ts}", "./nuxt.config.{js,ts}"],
	theme: {
		extend: {
			colors: {
				"c-base": "rgb(250, 250, 250)",
				"c-mode": "#f3f3f3",
				"c-dark": "#191919",
				"alt-dark": "#212121",
				custom: "#F1a930",
			},
			transitionProperty: {
				length: "height, width",
				spacing: "margin, padding",
			},
		},
	},
	darkMode: "class",
	plugins: [require("@tailwindcss/line-clamp"), require("tailwindcss-dark-mode")()],
};
