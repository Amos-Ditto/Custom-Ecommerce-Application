/** @type {import('tailwindcss').Config} */

const colors = require('tailwindcss/colors');

module.exports = {
    content: [
        './components/**/*.{js,vue,ts}',
        './layouts/**/*.vue',
        './pages/**/*.vue',
        './plugins/**/*.{js,ts}',
        './nuxt.config.{js,ts}',
        './src/**/*.{html,js}',
        './node_modules/tw-elements/dist/js/**/*.js',
        './node_modules/flowbite/**/*.js',
    ],
    theme: {
        extend: {
            colors: {
                dark: 'rgb(12 12 13 / 1)',
                tate: '#130912',
                tomato: 'tomato',
                super: '#e74142',
            },
        },
        screens: {
            xs: '400px',
            sm: '640px',
            md: '768px',
            lg: '1024px',
            xl: '1280px',
            '2xl': '1536px',
        },
        fontFamily: {
            sans: ['Nunito', 'sans-serif'],
            hand: ['Permanent Marker', 'cursive'],
        },
    },
    darkMode: 'class',
    plugins: [require('@tailwindcss/line-clamp'), require('tw-elements/dist/plugin'), require('flowbite/plugin')],
};
