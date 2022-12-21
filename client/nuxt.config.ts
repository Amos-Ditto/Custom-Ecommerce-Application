import presetIcons from '@unocss/preset-icons';

export default defineNuxtConfig({
    css: ['~/assets/css/tailwind.css'],
    modules: ['@nuxtjs/tailwindcss', '@unocss/nuxt', '@nuxtjs/color-mode', '@pinia/nuxt'],
    colorMode: {
        classSuffix: '',
    },
    app: {
        head: {
            charset: 'utf-16',
            title: 'Market',
            meta: [
                { name: 'description', content: 'Buy or Sell products' },
                { name: 'viewport', content: 'width=device-width, initial-scale=1.0' },
            ],
        },
        pageTransition: { name: 'page', mode: 'out-in' },
    },
    unocss: {
        icons: true,
        presets: [presetIcons({})],
    },
});
