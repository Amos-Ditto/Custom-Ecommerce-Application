// https://nuxt.com/docs/api/configuration/nuxt-config
export default defineNuxtConfig({
	css: ["~/assets/css/tailwind.css", "~/assets/css/global.css"],
	modules: [
		"@nuxtjs/tailwindcss",
		"@pinia/nuxt",
		"@nuxt/image-edge",
		"@nuxtjs/color-mode",
		"nuxt-icon",
		"@vueuse/nuxt",
		"@nuxtjs/apollo",
	],
	app: {
		pageTransition: { name: "page", mode: "out-in" },
	},
	colorMode: {
		preference: "system", // default value of $colorMode.preference
		fallback: "light", // fallback value if not system preference found
		hid: "nuxt-color-mode-script",
		globalName: "__NUXT_COLOR_MODE__",
		componentName: "ColorScheme",
		classPrefix: "",
		classSuffix: "",
		storageKey: "nuxt-color-mode",
	},
	apollo: {
		autoImports: true,
		authType: "Bearer",
		authHeader: "Authorization",
		tokenStorage: "cookie",
		proxyCookies: true,
		clients: {
			default: {
				httpEndpoint: "http://127.0.0.1:8000/graphql",
			},
		},
	},
});
