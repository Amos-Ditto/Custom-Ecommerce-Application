<template>
    <div class="w-full flex flex-col gap-y-8 pt-8">
        <div class="title-context w-full flex flex-row items-center justify-center relative gap-x-2">
            <div class="_line"></div>
            <h3 class="text-sm xs:text-base sm:text-2xl text-dark font-semibold tracking-wide">Featured Categories</h3>
            <div class="_line"></div>
        </div>
        <div
            class="list grid grid-rows-1 md:grid-flow-row grid-flow-col md:grid-cols-3 py-0.5 px-0.5 gap-x-4 gap-y-4 w-full overflow-x-auto"
        >
            <div
                class="flex flex-col w-full gap-y-1 ring-1 ring-neutral-200 rounded px-2 py-2 min-w-[75vw] md:min-w-0 hover:shadow-2xl transition duration-200 cursor-pointer"
            >
                <h3 class="text-xs xs:text-sm sm:text-base font-semibold tracking-wide text-dark">Laptops</h3>
                <div class="images w-full grid grid-cols-3 gap-x-1">
                    <img src="~/assets/images/Products/Lap_1.webp" alt="" />
                    <img src="~/assets/images/Products/Lap_2.webp" alt="" />
                    <img src="~/assets/images/Products/Lap_4.webp" alt="" />
                </div>
            </div>
            <div
                class="flex flex-col w-full gap-y-1 ring-1 ring-neutral-200 rounded px-2 py-2 min-w-[75vw] md:min-w-0 hover:shadow-2xl transition duration-200 cursor-pointer"
            >
                <h3 class="text-xs xs:text-sm sm:text-base font-semibold tracking-wide text-dark">Mens Fashion</h3>
                <div class="images w-full grid grid-cols-3 gap-x-1">
                    <img src="~/assets/images/categories/men_1.webp" alt="" />
                    <img src="~/assets/images/categories/men_2.webp" alt="" />
                    <img src="~/assets/images/categories/men_3.webp" alt="" />
                </div>
            </div>
            <div
                class="flex flex-col w-full gap-y-1 ring-1 ring-neutral-200 rounded px-2 py-2 min-w-[75vw] md:min-w-0 hover:shadow-2xl transition duration-200 cursor-pointer"
            >
                <h3 class="text-xs xs:text-sm sm:text-base font-semibold tracking-wide text-dark">Phones</h3>
                <div class="images w-full grid grid-cols-3 gap-x-1">
                    <img src="~/assets/images/Products/Phone_1.webp" alt="" />
                    <img src="~/assets/images/Products/Phone_2.webp" alt="" />
                    <img src="~/assets/images/Products/Phone_3.webp" alt="" />
                </div>
            </div>
        </div>
    </div>
</template>
<style scoped>
._line {
    border-top: 1px solid hsla(0, 0%, 59.2%, 0.3);
    @apply w-[70px] sm:w-[135px] h-[1px] mx-[8px] sm:mx-[14px];
}

.list-images img {
    @apply h-24 sm:h-32 rounded col-span-1 p-0.5 w-full;
}
.list .featured {
    @apply flex flex-col gap-y-1 ring-1 ring-neutral-200 rounded px-2 py-2 min-w-[60vw] md:min-w-0 hover:shadow-2xl transition duration-200 cursor-pointer;
}

.images img {
    @apply h-24 sm:h-32 rounded col-span-1 p-0.5 w-full;
}

.list::-webkit-scrollbar {
    width: 0px;
    height: 0px;
}
.list::-webkit-scrollbar-corner {
    background-color: #f9fbff;
}
.list::-webkit-scrollbar-thumb {
    @apply bg-neutral-400;
    border-radius: 32px;
}
.list::-webkit-scrollbar-track {
    background-color: #f9fbff;
}
</style>
