<template>
    <div id="cart-sidebar" class="col-span-1 sm:col-span-3 flex flex-col gap-y-4">
        <div id="delivery-details" class="w-full flex flex-col gap-y-2 py-3 shadow bg-gray-50 rounded">
            <div class="w-full pb-1 border-b border-neutral-200 px-2">
                <h4 class="text-sm sm:text-base tracking-wide uppercase text-neutral-600">Delivery</h4>
            </div>
            <div class="w-full flex flex-col gap-y-6 sm:gap-y-4 px-2">
                <h5 class="text-sm sm:text-base text-neutral-500">Choose your location</h5>
                <div id="region" class="w-full relative">
                    <div class="absolute left-4 -top-[34%] z-10 bg-[#f5f5f5] px-2">
                        <small class="text-xs text-neutral-500">Region</small>
                    </div>
                    <button
                        class="py-2 ring-neutral-300 ring-1 rounded-sm relative flex items-center w-full px-4 sm:px-2 md:px-4 lg:px-6 hover:ring-amber-400 focus:ring-amber-400 transition duration-200"
                    >
                        <span class="text-sm sm:text-base tracking-wide truncate">Nakuru</span>
                        <div class="i-carbon-chevron-down text-neutral-500 text-base absolute right-2 peer-focus:text-amber-500"></div>
                    </button>
                </div>

                <div id="center" class="w-full relative">
                    <div class="absolute left-4 -top-[34%] z-10 bg-[#f5f5f5] px-2">
                        <small class="text-xs text-neutral-500">Station</small>
                    </div>
                    <button
                        class="py-2 ring-neutral-300 ring-1 rounded-sm relative flex items-center w-full px-4 sm:px-2 md:px-4 lg:px-6 hover:ring-amber-400 focus:ring-amber-400 transition duration-200"
                    >
                        <span class="text-sm sm:text-base tracking-wide truncate">Kiamunyi</span>
                        <div class="i-carbon-chevron-down text-neutral-500 text-base absolute right-2 peer-focus:text-amber-500"></div>
                    </button>
                </div>

                <div id="fee" class="w-full flex flex-row flex-wrap gap-x-2 gap-y-2">
                    <small class="text-xs sm:text-sm text-neutral-500"
                        >+ delivery from KSh 92 (free delivery if order above KSh 1,999) to CBD - UON/Globe/Koja/River Road</small
                    >
                </div>
            </div>
            <div id="buy" class="w-full flex flex-row items-center px-2 mt-2">
                <button
                    class="px-8 py-2 rounded-sm ring-amber-500 ring-1 uppercase text-amber-600 tracking-wide text-sm sm:text-base w-full sm:w-auto"
                >
                    buy now
                </button>
            </div>
        </div>

        <div id="seller-details" class="w-full flex flex-col gap-y-2 py-3 shadow bg-gray-50 rounded">
            <div class="w-full pb-1 border-b border-neutral-200 px-2 relative flex items-center cursor-pointer">
                <h4 class="text-sm sm:text-base tracking-wide uppercase text-neutral-600">Seller Information</h4>
                <div class="i-carbon-chevron-right absolute right-2"></div>
            </div>
            <div id="merchant-details" class="w-full px-2 flex flex-col gap-y-2">
                <h3 class="font-semibold text-xl text-dark tracking-wide">Ditto Co.</h3>
                <div class="w-full flex flex-col gap-y-4 items-start">
                    <div id="feedback" class="flex flex-row gap-x-2 items-center">
                        <span class="text-dark text-sm font-light">95.2%</span>
                        <small class="text-xs text-neutral-600 font-light">Positive Feedback</small>
                    </div>
                    <button
                        class="px-8 py-1.5 sm:py-2 text-sm text-gray-50 tracking-wide bg-tomato rounded-3xl hover:bg-opacity-80 transition duration-200"
                    >
                        Visit Store
                    </button>
                </div>
            </div>
        </div>
    </div>
</template>
