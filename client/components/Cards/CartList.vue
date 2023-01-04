<template>
    <li>
        <div class="img col-span-3 flex justify-center items-start">
            <img src="~/assets/images/Products/Mens_1.webp" alt="" />
        </div>
        <div class="item-details col-span-7 flex flex-col gap-y-1">
            <div class="item-category flex flex-row w-full">
                <small class="text-xs sm:text-sm uppercase font-light text-neutral-400 tracking-wide truncate">Men's Clothe</small>
            </div>
            <div class="item-name flex flex-row w-full">
                <p class="text-sm capitalize text-neutral-600 tracking-wide font-light line-clamp-1">
                    Unisex Sherpa Denim Jacket Unisex Sherpa Denim Jacket
                </p>
            </div>
            <div class="item-discounts w-full flex flex-row flex-wrap gap-x-2 gap-y-1 items-center">
                <button class="text-xs capitalize bg-blue-400 bg-opacity-20 text-[dodgerblue] px-1.5 py-0.5 rounded-sm">
                    free shipping
                </button>
                <button class="text-xs uppercase bg-tomato bg-opacity-80 text-white px-1.5 py-0.5 rounded-sm">20% off</button>
            </div>
            <div class="item-quantity flex flex-row items-center justify-between py-2">
                <div class="quantity flex flex-row gap-x-2.5 items-center">
                    <button
                        class="px-2.5 py-[1px] rounded-sm bg-gray-100 hover:bg-gray-200 text-neutral-600 text-base sm:text-lg transition-colors duration-200"
                    >
                        -
                    </button>
                    <span class="text-xs sm:text-sm text-dark">1</span>
                    <button
                        class="px-2.5 py-[1px] rounded-sm bg-gray-100 hover:bg-gray-200 text-neutral-600 text-base sm:text-lg transition-colors duration-200"
                    >
                        +
                    </button>
                </div>
                <div class="price flex flex-col gap-y-1 justify-end">
                    <span class="actual-price text-sm sm:text-base font-semibold text-dark">$ 76.00</span>
                </div>
            </div>
            <div class="cart-actions w-full flex flex-row items-center justify-end gap-x-3">
                <button class="text-neutral-600 text-xs sm:text-sm px-2 py-0.5 hover:bg-gray-200 rounded-sm transition-colors duration-200">
                    Move to Favorites
                </button>
                <span class="w-[1px] h-[60%] bg-gray-300"></span>
                <button class="text-neutral-600 text-base px-1 py-0.5 hover:bg-gray-200 rounded-sm transition-colors duration-200">
                    <div class="i-carbon-delete"></div>
                </button>
            </div>
        </div>
    </li>
</template>

<style scoped>
li {
    @apply py-1 px-1 grid grid-cols-10 gap-x-1 border-b border-neutral-200 last:border-b-0;
}
</style>
