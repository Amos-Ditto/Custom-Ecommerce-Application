<template>
    <div id="details" class="sm:sm:col-span-6 flex flex-col gap-y-2">
        <div class="flex flex-row gap-x-4 items-start justify-between w-full">
            <h3 class="text-base sm:text-xl sm:line-clamp-2">
                Nokia 6.1 plus original nokia x6 octa-core 5.8 polegadas 4gb ram 64gb rom lte 16mp 2160p impressão digital smartphone
                desbloquea
            </h3>
            <div id="favourite" class="hidden sm:flex items-center justify-center">
                <button class="p-4 rounded-full hover:bg-orange-400 hover:bg-opacity-20 transition duration-200">
                    <div class="icon w-5 text-amber-500">
                        <IconsHeartIcon />
                    </div>
                </button>
            </div>
        </div>
        <div id="brand" class="w-full flex flex-row gap-x-2 items-center">
            <h5 class="text-sm sm:text-base text-dark">Brand:</h5>
            <span class="text-sm sm:text-base tracking-wide text-[steelblue] hover:underline cursor-pointer">Fashion</span>
        </div>
        <div id="rating" class="w-full flex flex-row items-center gap-x-4">
            <div id="rate-stars" class="flex flex-row items-center gap-x-2">
                <div class="icon w-4 text-orange-400">
                    <IconsStarIcon />
                </div>
                <div class="icon w-4 text-orange-400">
                    <IconsStarIcon />
                </div>
                <div class="icon w-4 text-orange-400">
                    <IconsStarIcon />
                </div>
            </div>
            <div id="rate-numbers" class="flex flex-row gap-x-2 items-center">
                <span class="text-base font-semibold">3.0</span>
                <span class="text-sm text-neutral-500">(50) reviews</span>
            </div>
        </div>
        <div id="prices" class="w-full flex flex-col gap-y-0 border-t border-neutral-200 py-2">
            <div
                id="discount"
                class="flex flex-row items-center justify-between bg-tomato bg-opacity-90 text-gray-50 text-base px-2 py-2 sm:py-3 rounded-t"
            >
                <div class="flex flex-row gap-x-2 items-center">
                    <div class="icon w-5 sm:w-6 sm:scale-110 text-amber-400">
                        <IconsLabelIcon />
                    </div>
                    <span class="text-sm sm:text-base tracking-wide">Discount</span>
                </div>
            </div>
            <div id="amount" class="flex flex-col gap-y-1 border border-tomato rounded-b py-2.5 px-2">
                <div id="real-price" class="flex flex-row items-center">
                    <span class="text-xl font-semibold tracking-wide">KES 1,119</span>
                </div>
                <div id="discount" class="flex flex-row gap-x-3 items-center">
                    <small class="line-through text-xs sm:text-sm text-neutral-600 tracking-wide">KES 13,250.00</small>
                    <button class="px-2 py-0.5 bg-tomato text-xs sm:text-sm text-gray-50 rounded-sm">20% OFF</button>
                </div>
            </div>
        </div>
        <div id="variation" class="w-full flex flex-col gap-y-3 border-t border-neutral-200 py-1.5">
            <h5 class="text-sm sm:text-base tracking-wide text-neutral-500 uppercase">VARIATION AVAILABLE</h5>
            <div class="w-full flex flex-col gap-y-1">
                <span class="capitalize text-sm sm:text-base tracking-wide">color</span>
                <div class="flex flex-row gap-x-2 flex-wrap gap-y-3 w-full">
                    <button
                        class="ring-1 ring-neutral-200 px-3 py-1 rounded-sm text-xs sm:text-sm uppercase tracking-wide text-neutral-600 hover:ring-neutral-300"
                    >
                        black
                    </button>
                    <button
                        class="ring-1 ring-neutral-200 px-3 py-1 rounded-sm text-xs sm:text-sm uppercase tracking-wide text-neutral-600 hover:ring-neutral-300"
                    >
                        Blue
                    </button>
                    <button
                        class="ring-1 ring-neutral-200 px-3 py-1 rounded-sm text-xs sm:text-sm uppercase tracking-wide text-neutral-600 hover:ring-neutral-300"
                    >
                        Pink
                    </button>
                    <button
                        class="ring-1 ring-neutral-200 px-3 py-1 rounded-sm text-xs sm:text-sm uppercase tracking-wide text-neutral-600 hover:ring-neutral-300"
                    >
                        red
                    </button>
                </div>
            </div>
        </div>
        <div id="addcart" class="w-full flex flex-col mt-2">
            <button
                class="px-8 py-3 rounded-sm bg-amber-500 bg-opacity-90 hover:bg-opacity-100 text-gray-50 tracking-wide uppercase text-sm sm:text-base font-light shadow-md transition duration-200"
            >
                add to cart
            </button>
        </div>
    </div>
</template>
