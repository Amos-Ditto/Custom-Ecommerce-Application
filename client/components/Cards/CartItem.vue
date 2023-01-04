<template>
    <div class="w-full flex flex-col py-3 px-6 bg-gray-50 rounded-sm shadow-sm">
        <div class="w-full flex flex-row justify-between items-center py-3 border-b border-neutral-200">
            <div class="flex items-center flex-row gap-x-2">
                <input
                    id="seller"
                    type="checkbox"
                    value=""
                    class="w-4 h-4 text-amber-500 bg-gray-100 border-gray-300 rounded focus:ring-amber-500 focus:ring-2"
                />
                <label for="seller" class="text-base font-extralight text-gray-800"> Ditto Co.</label>
            </div>
        </div>
        <div class="w-full flex flex-col gap-y-3">
            <div class="cart-item">
                <div class="h-full flex items-center justify-start col-span-1">
                    <input
                        type="checkbox"
                        value=""
                        class="w-4 h-4 text-amber-500 bg-gray-100 border-gray-300 rounded focus:ring-amber-500 focus:ring-2"
                    />
                </div>
                <div class="col-span-9 grid grid-cols-10 gap-x-4 py-2">
                    <div class="col-span-3">
                        <img src="~/assets/images/Products/Lap_1.webp" alt="" class="w-full h-auto" />
                    </div>
                    <div class="col-span-7 flex flex-col gap-y-2">
                        <div class="w-full flex flex-row justify-between items-center gap-x-1">
                            <div class="">
                                <h3 class="text-base font-light tracking-wide line-clamp-1">
                                    Nokia 6.1 plus original nokia x6 octa-core 5.8 polegadas 4gb ram 64gb rom lte 16mp 2160p impressão
                                    digital smartphone desbloquea
                                </h3>
                            </div>
                            <div class="flex flex-row gap-x-3 items-center justify-end">
                                <div class="">
                                    <div
                                        class="w-4 h-4 flex items-center justify-center text-neutral-600 hover:text-amber-400 cursor-pointer transition-colors duration-200"
                                    >
                                        <IconsHeartIcon />
                                    </div>
                                </div>
                                <div class="w-4 h-4 flex items-center justify-center">
                                    <div
                                        class="i-carbon-delete text-lg text-neutral-600 hover:text-amber-400 cursor-pointer transition-colors duration-200"
                                    ></div>
                                </div>
                            </div>
                        </div>
                        <div class="flex flex-row items-center w-full">
                            <button class="text-neutral-800 px-3 py-1 text-sm bg-gray-100 rounded-sm flex flex-row gap-x-2 items-center">
                                variants
                                <div class="i-carbon-chevron-right text-base text-neutral-600"></div>
                            </button>
                        </div>
                        <div class="w-full flex flex-row justify-between items-center pt-8 pb-1">
                            <div class="flex flex-row gap-x-3 items-center">
                                <span class="text-base font-semibold tracking-wide">KES 427.00</span>
                                <span class="text-sm font-light line-through tracking-wide text-neutral-500">KES 427.00</span>
                            </div>
                            <div class="quantity flex flex-row gap-x-2.5 items-center justify-end">
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
                        </div>
                        <div class="w-full flex flex-row gap-x-3 items-center">
                            <div class="item-discounts w-full flex flex-row flex-wrap gap-x-2 gap-y-1 items-center">
                                <button class="text-sm capitalize bg-blue-400 bg-opacity-20 text-[dodgerblue] px-1.5 py-0.5 rounded-sm">
                                    free shipping
                                </button>
                                <button class="text-sm uppercase bg-tomato bg-opacity-80 text-white px-1.5 py-0.5 rounded-sm">
                                    20% off
                                </button>
                            </div>
                        </div>
                    </div>
                </div>
            </div>

            <div class="cart-item">
                <div class="h-full flex items-center justify-start col-span-1">
                    <input
                        type="checkbox"
                        value=""
                        class="w-4 h-4 text-amber-500 bg-gray-100 border-gray-300 rounded focus:ring-amber-500 focus:ring-2"
                    />
                </div>
                <div class="col-span-9 grid grid-cols-10 gap-x-4 py-2">
                    <div class="col-span-3">
                        <img src="~/assets/images/Products/Lap_1.webp" alt="" class="w-full h-auto" />
                    </div>
                    <div class="col-span-7 flex flex-col gap-y-2">
                        <div class="w-full flex flex-row justify-between items-center gap-x-1">
                            <div class="">
                                <h3 class="text-base font-light tracking-wide line-clamp-1">
                                    Nokia 6.1 plus original nokia x6 octa-core 5.8 polegadas 4gb ram 64gb rom lte 16mp 2160p impressão
                                    digital smartphone desbloquea
                                </h3>
                            </div>
                            <div class="flex flex-row gap-x-3 items-center justify-end">
                                <div class="">
                                    <div
                                        class="w-4 h-4 flex items-center justify-center text-neutral-600 hover:text-amber-400 cursor-pointer transition-colors duration-200"
                                    >
                                        <IconsHeartIcon />
                                    </div>
                                </div>
                                <div class="w-4 h-4 flex items-center justify-center">
                                    <div
                                        class="i-carbon-delete text-lg text-neutral-600 hover:text-amber-400 cursor-pointer transition-colors duration-200"
                                    ></div>
                                </div>
                            </div>
                        </div>
                        <div class="flex flex-row items-center w-full">
                            <button class="text-neutral-800 px-3 py-1 text-sm bg-gray-100 rounded-sm flex flex-row gap-x-2 items-center">
                                variants
                                <div class="i-carbon-chevron-right text-base text-neutral-600"></div>
                            </button>
                        </div>
                        <div class="w-full flex flex-row justify-between items-center pt-8 pb-1">
                            <div class="flex flex-row gap-x-3 items-center">
                                <span class="text-base font-semibold tracking-wide">KES 427.00</span>
                                <span class="text-sm font-light line-through tracking-wide text-neutral-500">KES 427.00</span>
                            </div>
                            <div class="quantity flex flex-row gap-x-2.5 items-center justify-end">
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
                        </div>
                        <div class="w-full flex flex-row gap-x-3 items-center">
                            <div class="item-discounts w-full flex flex-row flex-wrap gap-x-2 gap-y-1 items-center">
                                <button class="text-sm capitalize bg-blue-400 bg-opacity-20 text-[dodgerblue] px-1.5 py-0.5 rounded-sm">
                                    free shipping
                                </button>
                                <button class="text-sm uppercase bg-tomato bg-opacity-80 text-white px-1.5 py-0.5 rounded-sm">
                                    20% off
                                </button>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<style scoped>
.cart-item {
    @apply w-full grid grid-cols-10 border-b last:border-none border-neutral-200 py-2;
}
</style>
