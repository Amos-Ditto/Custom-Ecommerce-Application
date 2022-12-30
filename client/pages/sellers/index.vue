<template>
    <main class="w-full overflow-x-hidden">
        <NuxtLayout name="home">
            <section class="w-full flex flex-col gap-y-0">
                <div
                    id="nav-header"
                    class="w-full py-3 px-2 sm:px-4 xl:px-8 2xl:px-20 flex items-center justify-center sm:border-y border-neutral-200"
                >
                    <div id="merchant-username" class="flex items-center justify-center">
                        <h4 class="text-xl sm:text-2xl font-semibold tracking-wide text-dark">Ditto Sellers Co.</h4>
                    </div>
                </div>
                <div id="dashboard" class="w-full flex flex-row items-center justify-center gap-x-4 bg-dark px-2 sm:px-4 xl:px-8 2xl:px-20">
                    <div class="link">
                        <span>Home</span>
                    </div>
                    <div class="link">
                        <span>Products</span>
                    </div>
                    <div class="link">
                        <span>Feedback</span>
                    </div>
                </div>
                <div id="body-section" class="w-full py-3 flex flex-col gap-y-6">
                    <div id="cover-image" class="w-full flex flex-row gap-x-1 overflow-x-auto px-0.5 sm:px-4 xl:px-8 2xl:px-20">
                        <img src="~/assets/images/c-bg.webp" alt="" class="w-full max-h-[50vh]" />
                    </div>
                    <SellersProducts />
                </div>
            </section>
        </NuxtLayout>
    </main>
</template>

<style scoped>
#dashboard .link {
    @apply px-4 text-gray-50 text-sm sm:text-base tracking-wide py-2 sm:py-2.5 hover:bg-neutral-700 transition-colors duration-200 cursor-pointer first:bg-neutral-700;
}
</style>
