<template>
    <main class="w-full">
        <NuxtLayout name="home">
            <section class="hero w-full grid grid-cols-1 md:grid-cols-10 px-2 sm:px-4 xl:px-8 2xl:px-20 gap-x-8">
                <aside class="col-span-2 hidden md:flex flex-col">
                    <div class="w-full h-full rounded bg-gray-50 shadow-sm min-h-[10rem]">
                        <LayoutCategoriesSideBar />
                    </div>
                </aside>
                <div class="hero w-full flex flex-col gap-x-1 gap-y-3 col-span-1 md:col-span-8 border-t border-neutral-300">
                    <div class="hero-links w-full flex flex-row justify-end items-center gap-x-3 md:gap-x-8">
                        <NuxtLink to="/splash">Home</NuxtLink>
                        <NuxtLink to="/splash">Trending Products</NuxtLink>
                        <NuxtLink to="/splash">Merchants</NuxtLink>
                    </div>
                    <div class="grid grid-cols-1 md:grid-cols-10 gap-y-6 md:gap-x-3 w-full">
                        <div
                            class="carousel md:col-span-7 min-h-[16rem] md:min-h-[24rem] bg-[url('assets/images/Banner.webp')] bg-no-repeat bg-top object-cover rounded"
                        ></div>
                        <div class="other-descriptions col-span-3 grid md:grid-rows-2 grid-cols-1 gap-y-3">
                            <div class="shop px-2 py-2 bg-orange-600 flex flex-col-reverse gap-y-4 justify-center items-center rounded">
                                <article class="w-full flex flex-col text-center items-center gap-y-2.5">
                                    <p class="text-lg font-bold text-gray-100 font-hand">Sell fast with less work</p>
                                    <button
                                        class="text-base md:text-lg ring-1 ring-gray-100 tracking-wide text-gray-100 px-12 py-0.5 rounded-sm flex flex-row items-center gap-x-4 md:gap-x-2"
                                    >
                                        <span class="">Sell</span>
                                        <div class="i-carbon-arrow-right transition-transform duration-200"></div>
                                    </button>
                                </article>
                                <div class="banner w-full flex items-center justify-center">
                                    <img src="~/assets/images/trade_in_banner_icons_white.webp" alt="" class="max-h-[65px]" />
                                </div>
                            </div>
                            <div class="shop bg-purple-900 rounded"></div>
                        </div>
                    </div>
                </div>
            </section>
            <main></main>
        </NuxtLayout>
    </main>
</template>

<style scoped>
.hero-links a {
    @apply text-base tracking-wide text-dark first:text-amber-600 font-light pt-3 pb-1 px-2;
    background-image: linear-gradient(currentColor, currentColor);
    background-position: 50% 100%;
    background-repeat: no-repeat;
    background-size: 0% 1px;
    transition: background-size 0.2s;
}
.hero-links a:hover,
.hero-links a:focus {
    background-size: 100% 1px;
}

article button:hover .i-carbon-arrow-right {
    @apply translate-x-1;
}
</style>
