<template>
    <div
        class="cart-dropdown flex flex-col min-w-[22rem] max-w-[12vw] w-auto min-h-[10rem] max-h-[100vh] overflow-y-auto bg-white shadow rounded z-50 px-2 absolute top-0 right-0 text-dark"
    >
        <div class="cart-header flex flex-row items-center justify-between px-2 py-3 border-b border-neutral-200 sticky top-0 bg-white">
            <div class="cart-title flex flex-row gap-x-2 items-center text-neutral-600">
                <h3 class="text-lg font-bold">My Cart</h3>
                <span class="text-base tracking-wide font-bold">(1)</span>
            </div>
            <div
                class="redirect-cart flex flex-row gap-x-1 items-center text-[dodgerblue] hover:text-[steelblue] transition-colors duration-200 cursor-pointer"
            >
                <span class="text-base">View</span>
                <div class="i-carbon-arrow-right text-base transition-transform duration-200"></div>
            </div>
        </div>
        <ul class="flex flex-col w-full gap-y-1 pb-3">
            <li>
                <div class="img col-span-3 flex justify-center items-start">
                    <img src="~/assets/images/Products/Mens_1.webp" alt="" />
                </div>
                <div class="item-details col-span-7 flex flex-col gap-y-1">
                    <div class="item-category flex flex-row w-full">
                        <small class="text-sm uppercase font-light text-neutral-400 tracking-wide truncate">Men's Clothe</small>
                    </div>
                    <div class="item-name flex flex-row w-full">
                        <p class="text-sm uppercase text-neutral-600 tracking-wide font-semibold truncate">Unisex Sherpa Denim Jacket</p>
                    </div>
                    <div class="item-discounts w-full flex flex-row flex-wrap gap-x-2 gap-y-1 items-center">
                        <button class="text-xs capitalize bg-blue-400 bg-opacity-20 text-[dodgerblue] px-1.5 py-0.5 rounded-sm">
                            free shipping
                        </button>
                    </div>
                    <div class="item-quantity flex flex-row items-center justify-between py-2">
                        <div class="quantity flex flex-row gap-x-2.5 items-center">
                            <button
                                class="px-2.5 py-[1px] rounded-sm bg-gray-100 hover:bg-gray-200 text-neutral-600 text-lg transition-colors duration-200"
                            >
                                -
                            </button>
                            <span class="text-sm text-dark">1</span>
                            <button
                                class="px-2.5 py-[1px] rounded-sm bg-gray-100 hover:bg-gray-200 text-neutral-600 text-lg transition-colors duration-200"
                            >
                                +
                            </button>
                        </div>
                        <div class="price flex flex-col gap-y-1 justify-end">
                            <span class="actual-price text-base font-semibold text-dark">$ 76.00</span>
                        </div>
                    </div>
                    <div class="cart-actions w-full flex flex-row items-center justify-end gap-x-3">
                        <button class="text-neutral-600 text-sm px-2 py-0.5 hover:bg-gray-200 rounded-sm transition-colors duration-200">
                            Move to Favorites
                        </button>
                        <span class="w-[1px] h-[60%] bg-gray-300"></span>
                        <button class="text-neutral-600 text-base px-1 py-0.5 hover:bg-gray-200 rounded-sm transition-colors duration-200">
                            <div class="i-carbon-delete"></div>
                        </button>
                    </div>
                </div>
            </li>

            <li>
                <div class="img col-span-3 flex justify-center items-start">
                    <img src="~/assets/images/Products/Lap_1.webp" alt="" />
                </div>
                <div class="item-details col-span-7 flex flex-col gap-y-1">
                    <div class="item-category flex flex-row w-full">
                        <small class="text-sm uppercase font-light text-neutral-400 tracking-wide truncate">Laptops</small>
                    </div>
                    <div class="item-name flex flex-row w-full">
                        <p class="text-sm uppercase text-neutral-600 tracking-wide font-semibold truncate">
                            Laptop 15.6-inch IPS Screen 16GB RAM 256GB SSD Intel Celeron N5095 Business Netbook Windows 10 11 Gaming
                            Notebook Pc Portable
                        </p>
                    </div>
                    <div class="item-discounts w-full flex flex-row flex-wrap gap-x-2 gap-y-1 items-center">
                        <button class="text-xs capitalize bg-blue-400 bg-opacity-20 text-[dodgerblue] px-1.5 py-0.5 rounded-sm">
                            free shipping
                        </button>
                    </div>
                    <div class="item-quantity flex flex-row items-center justify-between py-2">
                        <div class="quantity flex flex-row gap-x-2.5 items-center">
                            <button
                                class="px-2.5 py-[1px] rounded-sm bg-gray-100 hover:bg-gray-200 text-neutral-600 text-lg transition-colors duration-200"
                            >
                                -
                            </button>
                            <span class="text-sm text-dark">1</span>
                            <button
                                class="px-2.5 py-[1px] rounded-sm bg-gray-100 hover:bg-gray-200 text-neutral-600 text-lg transition-colors duration-200"
                            >
                                +
                            </button>
                        </div>
                        <div class="price flex flex-col gap-y-1 justify-end">
                            <span class="discount text-xs line-through text-neutral-500">$ 40.00</span>
                            <span class="actual-price text-base font-semibold text-dark">$ 34.00</span>
                        </div>
                    </div>
                    <div class="cart-actions w-full flex flex-row items-center justify-end gap-x-3">
                        <button class="text-neutral-600 text-sm px-2 py-0.5 hover:bg-gray-200 rounded-sm transition-colors duration-200">
                            Move to Favorites
                        </button>
                        <span class="w-[1px] h-[60%] bg-gray-300"></span>
                        <button class="text-neutral-600 text-base px-1 py-0.5 hover:bg-gray-200 rounded-sm transition-colors duration-200">
                            <div class="i-carbon-delete"></div>
                        </button>
                    </div>
                </div>
            </li>
            <li>
                <div class="img col-span-3 flex justify-center items-start">
                    <img src="~/assets/images/Products/Mens_1.webp" alt="" />
                </div>
                <div class="item-details col-span-7 flex flex-col gap-y-1">
                    <div class="item-category flex flex-row w-full">
                        <small class="text-sm uppercase font-light text-neutral-400 tracking-wide truncate">Men's Clothe</small>
                    </div>
                    <div class="item-name flex flex-row w-full">
                        <p class="text-sm uppercase text-neutral-600 tracking-wide font-semibold truncate">Unisex Sherpa Denim Jacket</p>
                    </div>
                    <div class="item-discounts w-full flex flex-row flex-wrap gap-x-2 gap-y-1 items-center">
                        <button class="text-xs capitalize bg-blue-400 bg-opacity-20 text-[dodgerblue] px-1.5 py-0.5 rounded-sm">
                            free shipping
                        </button>
                    </div>
                    <div class="item-quantity flex flex-row items-center justify-between py-2">
                        <div class="quantity flex flex-row gap-x-2.5 items-center">
                            <button
                                class="px-2.5 py-[1px] rounded-sm bg-gray-100 hover:bg-gray-200 text-neutral-600 text-lg transition-colors duration-200"
                            >
                                -
                            </button>
                            <span class="text-sm text-dark">1</span>
                            <button
                                class="px-2.5 py-[1px] rounded-sm bg-gray-100 hover:bg-gray-200 text-neutral-600 text-lg transition-colors duration-200"
                            >
                                +
                            </button>
                        </div>
                        <div class="price flex flex-col gap-y-1 justify-end">
                            <span class="actual-price text-base font-semibold text-dark">$ 76.00</span>
                        </div>
                    </div>
                    <div class="cart-actions w-full flex flex-row items-center justify-end gap-x-3">
                        <button class="text-neutral-600 text-sm px-2 py-0.5 hover:bg-gray-200 rounded-sm transition-colors duration-200">
                            Move to Favorites
                        </button>
                        <span class="w-[1px] h-[60%] bg-gray-300"></span>
                        <button class="text-neutral-600 text-base px-1 py-0.5 hover:bg-gray-200 rounded-sm transition-colors duration-200">
                            <div class="i-carbon-delete"></div>
                        </button>
                    </div>
                </div>
            </li>

            <li>
                <div class="img col-span-3 flex justify-center items-start">
                    <img src="~/assets/images/Products/Lap_1.webp" alt="" />
                </div>
                <div class="item-details col-span-7 flex flex-col gap-y-1">
                    <div class="item-category flex flex-row w-full">
                        <small class="text-sm uppercase font-light text-neutral-400 tracking-wide truncate">Laptops</small>
                    </div>
                    <div class="item-name flex flex-row w-full">
                        <p class="text-sm uppercase text-neutral-600 tracking-wide font-semibold truncate">
                            Laptop 15.6-inch IPS Screen 16GB RAM 256GB SSD Intel Celeron N5095 Business Netbook Windows 10 11 Gaming
                            Notebook Pc Portable
                        </p>
                    </div>
                    <div class="item-discounts w-full flex flex-row flex-wrap gap-x-2 gap-y-1 items-center">
                        <button class="text-xs capitalize bg-blue-400 bg-opacity-20 text-[dodgerblue] px-1.5 py-0.5 rounded-sm">
                            free shipping
                        </button>
                    </div>
                    <div class="item-quantity flex flex-row items-center justify-between py-2">
                        <div class="quantity flex flex-row gap-x-2.5 items-center">
                            <button
                                class="px-2.5 py-[1px] rounded-sm bg-gray-100 hover:bg-gray-200 text-neutral-600 text-lg transition-colors duration-200"
                            >
                                -
                            </button>
                            <span class="text-sm text-dark">1</span>
                            <button
                                class="px-2.5 py-[1px] rounded-sm bg-gray-100 hover:bg-gray-200 text-neutral-600 text-lg transition-colors duration-200"
                            >
                                +
                            </button>
                        </div>
                        <div class="price flex flex-col gap-y-1 justify-end">
                            <span class="discount text-xs line-through text-neutral-500">$ 40.00</span>
                            <span class="actual-price text-base font-semibold text-dark">$ 34.00</span>
                        </div>
                    </div>
                    <div class="cart-actions w-full flex flex-row items-center justify-end gap-x-3">
                        <button class="text-neutral-600 text-sm px-2 py-0.5 hover:bg-gray-200 rounded-sm transition-colors duration-200">
                            Move to Favorites
                        </button>
                        <span class="w-[1px] h-[60%] bg-gray-300"></span>
                        <button class="text-neutral-600 text-base px-1 py-0.5 hover:bg-gray-200 rounded-sm transition-colors duration-200">
                            <div class="i-carbon-delete"></div>
                        </button>
                    </div>
                </div>
            </li>
            <li>
                <div class="img col-span-3 flex justify-center items-start">
                    <img src="~/assets/images/Products/Mens_1.webp" alt="" />
                </div>
                <div class="item-details col-span-7 flex flex-col gap-y-1">
                    <div class="item-category flex flex-row w-full">
                        <small class="text-sm uppercase font-light text-neutral-400 tracking-wide truncate">Men's Clothe</small>
                    </div>
                    <div class="item-name flex flex-row w-full">
                        <p class="text-sm uppercase text-neutral-600 tracking-wide font-semibold truncate">Unisex Sherpa Denim Jacket</p>
                    </div>
                    <div class="item-discounts w-full flex flex-row flex-wrap gap-x-2 gap-y-1 items-center">
                        <button class="text-xs capitalize bg-blue-400 bg-opacity-20 text-[dodgerblue] px-1.5 py-0.5 rounded-sm">
                            free shipping
                        </button>
                    </div>
                    <div class="item-quantity flex flex-row items-center justify-between py-2">
                        <div class="quantity flex flex-row gap-x-2.5 items-center">
                            <button
                                class="px-2.5 py-[1px] rounded-sm bg-gray-100 hover:bg-gray-200 text-neutral-600 text-lg transition-colors duration-200"
                            >
                                -
                            </button>
                            <span class="text-sm text-dark">1</span>
                            <button
                                class="px-2.5 py-[1px] rounded-sm bg-gray-100 hover:bg-gray-200 text-neutral-600 text-lg transition-colors duration-200"
                            >
                                +
                            </button>
                        </div>
                        <div class="price flex flex-col gap-y-1 justify-end">
                            <span class="actual-price text-base font-semibold text-dark">$ 76.00</span>
                        </div>
                    </div>
                    <div class="cart-actions w-full flex flex-row items-center justify-end gap-x-3">
                        <button class="text-neutral-600 text-sm px-2 py-0.5 hover:bg-gray-200 rounded-sm transition-colors duration-200">
                            Move to Favorites
                        </button>
                        <span class="w-[1px] h-[60%] bg-gray-300"></span>
                        <button class="text-neutral-600 text-base px-1 py-0.5 hover:bg-gray-200 rounded-sm transition-colors duration-200">
                            <div class="i-carbon-delete"></div>
                        </button>
                    </div>
                </div>
            </li>

            <li>
                <div class="img col-span-3 flex justify-center items-start">
                    <img src="~/assets/images/Products/Lap_1.webp" alt="" />
                </div>
                <div class="item-details col-span-7 flex flex-col gap-y-1">
                    <div class="item-category flex flex-row w-full">
                        <small class="text-sm uppercase font-light text-neutral-400 tracking-wide truncate">Laptops</small>
                    </div>
                    <div class="item-name flex flex-row w-full">
                        <p class="text-sm uppercase text-neutral-600 tracking-wide font-semibold truncate">
                            Laptop 15.6-inch IPS Screen 16GB RAM 256GB SSD Intel Celeron N5095 Business Netbook Windows 10 11 Gaming
                            Notebook Pc Portable
                        </p>
                    </div>
                    <div class="item-discounts w-full flex flex-row flex-wrap gap-x-2 gap-y-1 items-center">
                        <button class="text-xs capitalize bg-blue-400 bg-opacity-20 text-[dodgerblue] px-1.5 py-0.5 rounded-sm">
                            free shipping
                        </button>
                    </div>
                    <div class="item-quantity flex flex-row items-center justify-between py-2">
                        <div class="quantity flex flex-row gap-x-2.5 items-center">
                            <button
                                class="px-2.5 py-[1px] rounded-sm bg-gray-100 hover:bg-gray-200 text-neutral-600 text-lg transition-colors duration-200"
                            >
                                -
                            </button>
                            <span class="text-sm text-dark">1</span>
                            <button
                                class="px-2.5 py-[1px] rounded-sm bg-gray-100 hover:bg-gray-200 text-neutral-600 text-lg transition-colors duration-200"
                            >
                                +
                            </button>
                        </div>
                        <div class="price flex flex-col gap-y-1 justify-end">
                            <span class="discount text-xs line-through text-neutral-500">$ 40.00</span>
                            <span class="actual-price text-base font-semibold text-dark">$ 34.00</span>
                        </div>
                    </div>
                    <div class="cart-actions w-full flex flex-row items-center justify-end gap-x-3">
                        <button class="text-neutral-600 text-sm px-2 py-0.5 hover:bg-gray-200 rounded-sm transition-colors duration-200">
                            Move to Favorites
                        </button>
                        <span class="w-[1px] h-[60%] bg-gray-300"></span>
                        <button class="text-neutral-600 text-base px-1 py-0.5 hover:bg-gray-200 rounded-sm transition-colors duration-200">
                            <div class="i-carbon-delete"></div>
                        </button>
                    </div>
                </div>
            </li>
        </ul>
    </div>
</template>

<style scoped>
.cart-dropdown ul li {
    @apply py-1 px-1 grid grid-cols-10 gap-x-1 border-b border-neutral-200 last:border-b-0;
}

.redirect-cart:hover .i-carbon-arrow-right {
    @apply translate-x-0.5;
}
</style>
