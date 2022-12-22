<template>
    <section class="w-full flex flex-col">
        <div
            id="item-header"
            class="w-full flex flex-row gap-x-2 sm:gap-x-4 items-center border-y border-neutral-200 py-3 px-2 sm:px-4 xl:px-8 2xl:px-20"
        >
            <span>Home</span>
            <div class="i-carbon-chevron-right"></div>
            <span>Phone & Accessories</span>
            <div class="i-carbon-chevron-right"></div>
            <span>Android Phones</span>
        </div>
        <div id="item-detail" class="w-full grid grid-cols-1 sm:grid-cols-2 gap-y-5 gap-x-10 py-4 px-2 sm:px-4 xl:px-8 2xl:px-20">
            <div id="img-details" class="flex flex-col gap-y-2">
                <div id="main-img" class="w-full flex items-center justify-center">
                    <img src="~/assets/images/Products/Phone_1.webp" alt="" class="w-full rounded" />
                </div>
                <div id="more-images" class="w-full grid grid-cols-4 py-2 px-2 ring-1 ring-neutral-200">
                    <div
                        class="max-h-[8rem] flex items-center justify-center cursor-pointer hover:ring-neutral-200 ring-1 ring-transparent rounded-sm p-1"
                    >
                        <img src="~/assets/images/Products/Phone_1.webp" alt="" class="h-full" />
                    </div>
                    <div
                        class="max-h-[8rem] flex items-center justify-center cursor-pointer hover:ring-neutral-200 ring-1 ring-transparent rounded-sm p-1"
                    >
                        <img src="~/assets/images/Products/Phone_2.webp" alt="" class="h-full" />
                    </div>
                    <div
                        class="max-h-[8rem] flex items-center justify-center cursor-pointer hover:ring-neutral-200 ring-1 ring-transparent rounded-sm p-1"
                    >
                        <img src="~/assets/images/Products/Phone_3.webp" alt="" class="h-full" />
                    </div>
                    <div
                        class="max-h-[8rem] flex items-center justify-center cursor-pointer hover:ring-neutral-200 ring-1 ring-transparent rounded-sm p-1"
                    >
                        <img src="~/assets/images/Products/Lap_1.webp" alt="" class="h-full" />
                    </div>
                </div>
            </div>

            <div id="item-descriptions" class="flex flex-col gap-y-4">
                <div class="w-full">
                    <h3 class="text-2xl font-light text-dark">
                        Nokia 6.1 plus original nokia x6 octa-core 5.8 polegadas 4gb ram 64gb rom lte 16mp 2160p impressão digital
                        smartphone desbloquea
                    </h3>
                </div>
                <div id="rating" class="w-full flex flex-row items-center gap-x-4">
                    <div id="rate-stars" class="flex flex-row items-center gap-x-2">
                        <div class="icon w-4 sm:w-5 text-orange-400">
                            <IconsStarIcon />
                        </div>
                        <div class="icon w-4 sm:w-5 text-orange-400">
                            <IconsStarIcon />
                        </div>
                        <div class="icon w-4 sm:w-5 text-orange-400">
                            <IconsStarIcon />
                        </div>
                    </div>
                    <div id="rate-numbers" class="flex flex-row gap-x-2 items-center">
                        <span class="text-lg font-semibold">3.0</span>
                        <span class="text-sm text-neutral-500">(50) reviews</span>
                    </div>
                </div>
                <div id="seller-name" class="w-full flex-row flex items-center gap-x-4 py-4">
                    <p class="text-base text-neutral-600 font-light">Merchant:</p>
                    <h4 class="text-base text-neutral-600 font-semibold hover:underline cursor-pointer">Ditto Store</h4>
                </div>
                <div id="item-price" class="w-full flex flex-row items-center gap-x-4 py-2.5 px-2 bg-gray-200 rounded-sm">
                    <div id="current-price" class="text-2xl tracking-wide flex flex-row items-center gap-x-2 text-orange-500 font-semibold">
                        <span>KES</span>
                        <span>10,601.00</span>
                    </div>
                    <div id="discount" class="flex flex-row gap-x-3 items-center">
                        <small class="line-through text-xs text-neutral-600 tracking-wide">KES 13,250.00</small>
                        <button class="px-2 py-0.5 bg-tomato text-xs text-gray-50 rounded-sm">20% OFF</button>
                    </div>
                </div>

                <div id="item-variants" class="w-full flex flex-col gap-y-2 pt-8"></div>
                <div id="item-quantity" class="w-full flex flex-row items-center">
                    <div class="quantity-container flex flex-row">
                        <button
                            class="px-4 py-1 text-xl rounded-l-3xl bg-gray-200 ring-1 ring-neutral-200 hover:ring-neutral-300 transition duration-200"
                        >
                            -
                        </button>
                        <input
                            type="text"
                            name="quantity"
                            id="quantity"
                            value="1"
                            class="text-base max-w-[5rem] bg-inherit px-3 ring-1 ring-neutral-200 text-center outline-none hover:ring-neutral-300 transition duration-200"
                        />
                        <button
                            class="px-4 py-1 text-xl rounded-r-3xl bg-gray-200 ring-1 ring-neutral-200 hover:ring-neutral-300 transition duration-200"
                        >
                            +
                        </button>
                    </div>
                </div>
                <div id="purchases" class="py-2 grid grid-cols-2 gap-x-4 w-full items-center">
                    <button
                        class="px-12 py-3 rounded-sm ring-1 ring-orange-300 text-xl text-dark tracking-wide hover:ring-orange-500 transition duration-200"
                    >
                        Add to Cart
                    </button>
                    <button
                        class="px-12 py-3 rounded-sm bg-gradient-to-r hover:bg-gradient-to-l from-orange-500 to-orange-400 text-xl text-gray-50 tracking-wide"
                    >
                        Buy Now
                    </button>
                </div>
            </div>
        </div>
        <div id="store-details" class="w-full px-2 sm:px-4 xl:px-8 2xl:px-20 py-4">
            <div class="w-full grid grid-cols-10 gap-y-4 bg-gray-200 rounded-md px-4 py-4">
                <div id="merchant-status" class="col-span-3 flex flex-col gap-y-2">
                    <h3 class="font-semibold text-2xl text-dark tracking-wide">Ditto Co.</h3>
                    <div id="merchant-status" class="w-full flex flex-col items-start gap-y-4">
                        <div id="feedback" class="flex flex-row gap-x-2 items-center">
                            <span class="text-dark text-sm font-light">95.2%</span>
                            <small class="text-xs text-neutral-600 font-light">Positive Feedback</small>
                        </div>
                        <button
                            class="px-3 py-1 text-xs text-gray-50 tracking-wide bg-tomato rounded-3xl hover:bg-opacity-80 transition duration-200"
                        >
                            Visit Store
                        </button>
                    </div>
                </div>
            </div>
            <!-- <div id="store-name" class="w-full py-3 flex flex-col gap-y-2 items-center justify-center bg-gray-200 rounded-md">
                <h3 class="font-semibold text-2xl text-dark tracking-wide">Ditto Co.</h3>
                <div id="merchant-status" class="w-full flex flex-row gap-x-4 items-center justify-center">
                    <div id="feedback" class="flex flex-row gap-x-2 items-center">
                        <span class="text-dark text-sm font-light">95.2%</span>
                        <small class="text-xs text-neutral-600 font-light">Positive Feedback</small>
                    </div>
                    <button class="px-3 py-1 text-xs text-gray-50 tracking-wide bg-tomato rounded-3xl">Visit Store</button>
                </div>
            </div> -->
        </div>
    </section>
</template>

<style scoped>
#item-header span {
    @apply text-base font-semibold text-dark first:text-orange-600;
}
#item-header .i-carbon-chevron-right {
    @apply text-xl text-neutral-500;
}
</style>
