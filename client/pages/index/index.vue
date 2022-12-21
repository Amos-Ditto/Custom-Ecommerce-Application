<template>
    <main class="w-full flex flex-col gap-y-10">
        <section class="hero w-full grid grid-cols-1 md:grid-cols-10 px-2 sm:px-4 xl:px-8 2xl:px-20 gap-x-4 lg:gap-x-8">
            <aside class="col-span-2 hidden md:flex flex-col">
                <div class="w-full h-full rounded bg-gray-50 shadow-sm min-h-[10rem]">
                    <LayoutCategoriesSideBar />
                </div>
            </aside>
            <div class="hero w-full flex flex-col gap-x-1 gap-y-3 col-span-1 md:col-span-8 border-t border-neutral-300">
                <div class="hero-links w-full flex flex-row justify-end items-center gap-x-3 md:gap-x-8">
                    <NuxtLink to="/">Home</NuxtLink>
                    <NuxtLink :to="{ name: 'HomeSearch' }">Trending Products</NuxtLink>
                    <NuxtLink to="/">Merchants</NuxtLink>
                </div>
                <div class="flex flex-col gap-y-6 md:gap-x-3 w-full">
                    <div class="h-[18rem] md:-h-[22rem] xl:h-[24rem] rounded w-full">
                        <HeroCarousel />
                    </div>
                </div>
            </div>
        </section>
        <ContentsHomeProducts />
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
