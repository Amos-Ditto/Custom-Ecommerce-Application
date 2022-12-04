<template>
    <div class="w-full flex flex-col gap-y-8 pt-8">
        <div class="title-context w-full flex flex-row items-center justify-center relative gap-x-2">
            <div class="_line"></div>
            <h3 class="text-lg sm:text-2xl text-dark font-semibold tracking-wide">Featured Categories</h3>
            <div class="_line"></div>
        </div>
        <div class="list grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 gap-x-4 gap-y-4 w-full">
            <div class="flex flex-col gap-y-1 ring-1 ring-neutral-200 rounded px-2 py-2">
                <h3 class="text-base font-semibold tracking-wide text-dark">Laptops</h3>
                <div class="list-images grid grid-cols-1 gap-x-1 w-full">
                    <img src="~/assets/images/categories/Laptops.webp" alt="1" />
                </div>
            </div>
            <div class="flex flex-col gap-y-1 ring-1 ring-neutral-200 rounded px-2 py-2">
                <h3 class="text-base font-semibold tracking-wide text-dark">Laptops</h3>
                <div class="list-images grid grid-cols-1 gap-x-1 w-full">
                    <img src="~/assets/images/categories/Laptops.webp" alt="1" />
                </div>
            </div>
            <div class="flex flex-col gap-y-1 ring-1 ring-neutral-200 rounded px-2 py-2">
                <h3 class="text-base font-semibold tracking-wide text-dark">Laptops</h3>
                <div class="list-images grid grid-cols-1 gap-x-1 w-full">
                    <img src="~/assets/images/categories/Laptops.webp" alt="1" />
                </div>
            </div>
            <div class="flex flex-col gap-y-1 ring-1 ring-neutral-200 rounded px-2 py-2">
                <h3 class="text-base font-semibold tracking-wide text-dark">Laptops</h3>
                <div class="list-images grid grid-cols-1 gap-x-1 w-full">
                    <img src="~/assets/images/categories/Laptops.webp" alt="1" />
                </div>
            </div>
            <div class="flex flex-col gap-y-1 ring-1 ring-neutral-200 rounded px-2 py-2">
                <h3 class="text-base font-semibold tracking-wide text-dark">Laptops</h3>
                <div class="list-images grid grid-cols-1 gap-x-1 w-full">
                    <img src="~/assets/images/categories/Laptops.webp" alt="1" />
                </div>
            </div>
            <div class="flex flex-col gap-y-1 ring-1 ring-neutral-200 rounded px-2 py-2">
                <h3 class="text-base font-semibold tracking-wide text-dark">Laptops</h3>
                <div class="list-images grid grid-cols-1 gap-x-1 w-full">
                    <img src="~/assets/images/categories/Laptops.webp" alt="1" />
                </div>
            </div>
        </div>
    </div>
</template>
<style scoped>
._line {
    border-top: 1px solid hsla(0, 0%, 59.2%, 0.3);
    @apply w-[80px] sm:w-[135px] h-[1px] mx-[8px] sm:mx-[14px];
}

.list-images img {
    @apply h-32 rounded col-span-1 p-0.5 w-full;
}
</style>
