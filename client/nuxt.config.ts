// https://nuxt.com/docs/api/configuration/nuxt-config
export default defineNuxtConfig({
	css: ["~/assets/css/tailwind.css", "~/assets/css/global.css"],
	modules: ["@nuxtjs/tailwindcss", "@pinia/nuxt", "@nuxt/image-edge"],
	app: {
		head: {
			charset: "utf-16",
			title: "Ecommerce",
			meta: [{ name: "description", content: "Full app ecommerce" }],
			link: [{ rel: "stylesheet", href: 'https://fonts.googleapis.com/css2?family=Inter&display=swap" rel="stylesheet' }],
		},
		pageTransition: { name: "page", mode: "out-in" },
	},
});
