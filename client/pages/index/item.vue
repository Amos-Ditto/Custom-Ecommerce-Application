<template>
    <section class="w-full flex flex-col">
        <div
            id="item-header"
            class="w-full hidden sm:flex flex-row gap-x-2 sm:gap-x-4 items-center border-y border-neutral-200 py-3 px-2 sm:px-4 xl:px-8 2xl:px-20"
        >
            <span>Home</span>
            <div class="i-carbon-chevron-right"></div>
            <span>Phone & Accessories</span>
            <div class="i-carbon-chevron-right"></div>
            <span>Android Phones</span>
        </div>
        <div id="details-container" class="w-full py-4 px-2 sm:px-4 xl:px-8 2xl:px-20 grid grid-cols-10 gap-x-4 gap-y-8">
            <div id="body-details" class="col-span-7 grid grid-cols-10 gap-x-4 gap-y-2 bg-gray-50 shadow-sm rounded-sm px-3 py-3">
                <div id="img-display" class="col-span-4 flex flex-col gap-y-2">
                    <div id="full-image" class="w-full flex items-center justify-center">
                        <img src="~/assets/images/Products/Phone_2.webp" alt="" class="w-full rounded-sm" />
                    </div>
                    <div id="img-list" class="w-full flex flex-row flex-wrap gap-x-2 items-center">
                        <div
                            id="img-small"
                            class="h-[50px] w-[50px] flex items-center justify-center ring-1 ring-transparent hover:ring-neutral-200 rounded transition duration-200 cursor-pointer"
                        >
                            <img src="~/assets/images/Products/Lap_4.webp" alt="" class="h-full" />
                        </div>
                        <div
                            id="img-small"
                            class="h-[50px] w-[50px] flex items-center justify-center ring-1 ring-transparent hover:ring-neutral-200 rounded transition duration-200 cursor-pointer"
                        >
                            <img src="~/assets/images/Products/Phone_1.webp" alt="" class="h-full" />
                        </div>
                        <div
                            id="img-small"
                            class="h-[50px] w-[50px] flex items-center justify-center ring-1 ring-transparent hover:ring-neutral-200 rounded transition duration-200 cursor-pointer"
                        >
                            <img src="~/assets/images/Products/Mens_1.webp" alt="" class="h-full" />
                        </div>
                        <div
                            id="img-small"
                            class="h-[50px] w-[50px] flex items-center justify-center ring-1 ring-transparent hover:ring-neutral-200 rounded transition duration-200 cursor-pointer"
                        >
                            <img src="~/assets/images/Products/Lap_2.webp" alt="" class="h-full" />
                        </div>
                    </div>
                    <div id="share" class="w-full flex flex-col gap-y-3 border-t border-neutral-200 py-1 mt-2">
                        <h4 class="text-base tracking-wide text-neutral-500">SHARE THIS PRODUCT</h4>
                        <div id="socials-links" class="flex flex-row items-center w-full justify-start gap-x-3">
                            <span
                                class="w-9 h-9 flex justify-center items-center rounded-full ring-1 ring-transparent hover:ring-neutral-400 p-2 transition duration-200 cursor-pointer"
                            >
                                <img src="~/assets/images/Icons/linkedin.svg" alt="" class="w-full h-full" />
                            </span>

                            <span
                                class="w-9 h-9 flex justify-center items-center rounded-full ring-1 ring-transparent hover:ring-neutral-400 p-2 transition duration-200 cursor-pointer"
                            >
                                <img src="~/assets/images/Icons/twitter.png" alt="" class="w-full h-full" />
                            </span>
                        </div>
                    </div>
                </div>

                <div id="details" class="col-span-6 flex flex-col gap-y-2">
                    <div class="flex flex-row gap-x-4 items-start justify-between w-full">
                        <h3 class="text-xl line-clamp-2">
                            Nokia 6.1 plus original nokia x6 octa-core 5.8 polegadas 4gb ram 64gb rom lte 16mp 2160p impressão digital
                            smartphone desbloquea
                        </h3>
                        <div id="favourite" class="flex items-center justify-center">
                            <button class="p-4 rounded-full hover:bg-orange-400 hover:bg-opacity-20 transition duration-200">
                                <div class="icon w-5 text-amber-500">
                                    <IconsHeartIcon />
                                </div>
                            </button>
                        </div>
                    </div>
                    <div id="brand" class="w-full flex flex-row gap-x-2 items-center">
                        <h5 class="text-base text-dark">Brand:</h5>
                        <span class="text-base tracking-wide text-[steelblue] hover:underline cursor-pointer">Fashion</span>
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
                            class="w-full flex flex-row items-center justify-between bg-tomato bg-opacity-90 text-gray-50 text-base px-2 py-3 rounded-t"
                        >
                            <div class="flex flex-row gap-x-2 items-center">
                                <div class="icon w-6 scale-110 text-amber-400">
                                    <IconsLabelIcon />
                                </div>
                                <span>Discount</span>
                            </div>
                        </div>
                        <div id="amount" class="flex flex-col gap-y-1 border border-tomato rounded-b py-2.5 px-2">
                            <div id="real-price" class="flex flex-row items-center">
                                <span class="text-xl font-semibold tracking-wide">KES 1,119</span>
                            </div>
                            <div id="discount" class="flex flex-row gap-x-3 items-center">
                                <small class="line-through text-sm text-neutral-600 tracking-wide">KES 13,250.00</small>
                                <button class="px-2 py-0.5 bg-tomato text-sm text-gray-50 rounded-sm">20% OFF</button>
                            </div>
                        </div>
                    </div>
                    <div id="variation" class="w-full flex flex-col gap-y-3 border-t border-neutral-200 py-1.5">
                        <h5 class="text-base tracking-wide text-neutral-500 uppercase">VARIATION AVAILABLE</h5>
                        <div class="w-full flex flex-col gap-y-1">
                            <span class="capitalize text-base tracking-wide">color</span>
                            <div class="flex flex-row gap-x-2 flex-wrap gap-y-3 w-full">
                                <button
                                    class="ring-1 ring-neutral-200 px-3 py-1 rounded-sm text-sm uppercase tracking-wide text-neutral-600 hover:ring-neutral-300"
                                >
                                    black
                                </button>
                                <button
                                    class="ring-1 ring-neutral-200 px-3 py-1 rounded-sm text-sm uppercase tracking-wide text-neutral-600 hover:ring-neutral-300"
                                >
                                    Blue
                                </button>
                                <button
                                    class="ring-1 ring-neutral-200 px-3 py-1 rounded-sm text-sm uppercase tracking-wide text-neutral-600 hover:ring-neutral-300"
                                >
                                    Pink
                                </button>
                                <button
                                    class="ring-1 ring-neutral-200 px-3 py-1 rounded-sm text-sm uppercase tracking-wide text-neutral-600 hover:ring-neutral-300"
                                >
                                    red
                                </button>
                            </div>
                        </div>
                    </div>
                    <div id="addcart" class="w-full flex flex-col mt-2">
                        <button
                            class="px-8 py-3 rounded-sm bg-amber-500 bg-opacity-90 hover:bg-opacity-100 text-gray-50 tracking-wide uppercase text-base font-light shadow-md transition duration-200"
                        >
                            add to cart
                        </button>
                    </div>
                </div>
            </div>
            <div id="cart-sidebar" class="col-span-3 flex flex-col gap-y-4">
                <div id="delivery-details" class="w-full flex flex-col gap-y-2 py-3 shadow bg-gray-50 rounded">
                    <div class="w-full pb-1 border-b border-neutral-200 px-2">
                        <h4 class="text-base tracking-wide uppercase text-neutral-600">Delivery</h4>
                    </div>
                    <div class="w-full flex flex-col gap-y-4 px-2">
                        <h5 class="text-base text-neutral-500">Choose your location</h5>
                        <div id="region" class="w-full relative">
                            <div class="absolute left-4 -top-[34%] z-10 bg-[#f5f5f5] px-2">
                                <small class="text-xs text-neutral-500">Region</small>
                            </div>
                            <button
                                class="py-2 ring-neutral-300 ring-1 rounded-sm relative flex items-center w-full px-2 md:px-4 lg:px-6 hover:ring-amber-400 focus:ring-amber-400 transition duration-200"
                            >
                                <span class="text-base tracking-wide truncate">Nakuru</span>
                                <div
                                    class="i-carbon-chevron-down text-neutral-500 text-base absolute right-2 peer-focus:text-amber-500"
                                ></div>
                            </button>
                        </div>

                        <div id="center" class="w-full relative">
                            <div class="absolute left-4 -top-[34%] z-10 bg-[#f5f5f5] px-2">
                                <small class="text-xs text-neutral-500">Station</small>
                            </div>
                            <button
                                class="py-2 ring-neutral-300 ring-1 rounded-sm relative flex items-center w-full px-2 md:px-4 lg:px-6 hover:ring-amber-400 focus:ring-amber-400 transition duration-200"
                            >
                                <span class="text-base tracking-wide truncate">Kiamunyi</span>
                                <div
                                    class="i-carbon-chevron-down text-neutral-500 text-base absolute right-2 peer-focus:text-amber-500"
                                ></div>
                            </button>
                        </div>

                        <div id="fee" class="w-full flex flex-row flex-wrap gap-x-2 gap-y-2">
                            <small class="text-sm text-neutral-500"
                                >+ delivery from KSh 92 (free delivery if order above KSh 1,999) to CBD - UON/Globe/Koja/River Road</small
                            >
                        </div>
                    </div>
                    <div id="buy" class="w-full flex flex-row items-center px-2 mt-2">
                        <button class="px-8 py-2 rounded-sm ring-amber-500 ring-1 uppercase text-amber-600 tracking-wide">buy now</button>
                    </div>
                </div>

                <div id="seller-details" class="w-full flex flex-col gap-y-2 py-3 shadow bg-gray-50 rounded">
                    <div class="w-full pb-1 border-b border-neutral-200 px-2 relative flex items-center cursor-pointer">
                        <h4 class="text-base tracking-wide uppercase text-neutral-600">Seller Information</h4>
                        <div class="i-carbon-chevron-right absolute right-2"></div>
                    </div>
                    <div
                        id="merchant-details"
                        class="w-full px-2 flex flex-col gap-y-2 items-center sm:items-start justify-center sm:justify-start"
                    >
                        <h3 class="font-semibold text-xl text-dark tracking-wide">Ditto Co.</h3>
                        <div class="w-full flex flex-col justify-center items-center sm:items-start gap-y-4">
                            <div id="feedback" class="flex flex-row gap-x-2 items-center">
                                <span class="text-dark text-sm font-light">95.2%</span>
                                <small class="text-xs text-neutral-600 font-light">Positive Feedback</small>
                            </div>
                            <button
                                class="px-6 sm:px-3 py-1 text-xs text-gray-50 tracking-wide bg-tomato rounded-3xl hover:bg-opacity-80 transition duration-200"
                            >
                                Visit Store
                            </button>
                        </div>
                    </div>
                </div>
            </div>
            <div id="recommended-items" class="col-span-10 lg:col-span-7 flex flex-col gap-y-2 bg-gray-50 shadow-sm rounded-sm px-3 py-3">
                <div class="w-full pb-1 border-b border-neutral-200 px-2">
                    <h4 class="text-lg tracking-wide capitalize text-neutral-600">Customers who viewed this also viewed</h4>
                </div>
                <ul id="recommended-list" class="w-full grid grid-cols-6 gap-x-4 gap-y-4">
                    <li class="flex flex-col gap-y-2 hover:shadow px-2 py-1 cursor-pointer transition duration-200">
                        <div class="w-full max-h-[12rem] flex items-center justify-center">
                            <img src="~/assets/images/Products/Lap_4.webp" alt="" class="rounded-sm h-full" />
                        </div>
                        <div class="w-full flex flex-col gap-y-1">
                            <small class="line-clamp-1 text-neutral-600 text-sm"
                                >Nokia 6.1 plus original nokia x6 octa-core 5.8 polegadas 4gb ram 64gb rom lte 16mp 2160p impressão digital
                                smartphone desbloquea</small
                            >
                            <div class="text-sm tracking-wide flex flex-row items-center gap-x-0.5 text-dark">
                                <span>KES</span>
                                <span>10,601.00</span>
                            </div>
                        </div>
                    </li>
                    <li class="flex flex-col gap-y-2 hover:shadow px-2 py-1 cursor-pointer transition duration-200">
                        <div class="w-full max-h-[12rem] flex items-center justify-center">
                            <img src="~/assets/images/Products/Phone_1.webp" alt="" class="rounded-sm h-full" />
                        </div>
                        <div class="w-full flex flex-col gap-y-1">
                            <small class="line-clamp-1 text-neutral-600 text-sm"
                                >Nokia 6.1 plus original nokia x6 octa-core 5.8 polegadas 4gb ram 64gb rom lte 16mp 2160p impressão digital
                                smartphone desbloquea</small
                            >
                            <div class="text-sm tracking-wide flex flex-row items-center gap-x-0.5 text-dark">
                                <span>KES</span>
                                <span>10,601.00</span>
                            </div>
                        </div>
                    </li>
                    <li class="flex flex-col gap-y-2 hover:shadow px-2 py-1 cursor-pointer transition duration-200">
                        <div class="w-full max-h-[12rem] flex items-center justify-center">
                            <img src="~/assets/images/Products/Lap_1.webp" alt="" class="rounded-sm h-full" />
                        </div>
                        <div class="w-full flex flex-col gap-y-1">
                            <small class="line-clamp-1 text-neutral-600 text-sm"
                                >Nokia 6.1 plus original nokia x6 octa-core 5.8 polegadas 4gb ram 64gb rom lte 16mp 2160p impressão digital
                                smartphone desbloquea</small
                            >
                            <div class="text-sm tracking-wide flex flex-row items-center gap-x-0.5 text-dark">
                                <span>KES</span>
                                <span>10,601.00</span>
                            </div>
                        </div>
                    </li>
                    <li class="flex flex-col gap-y-2 hover:shadow px-2 py-1 cursor-pointer transition duration-200">
                        <div class="w-full max-h-[12rem] flex items-center justify-center">
                            <img src="~/assets/images/Products/Mens_1.webp" alt="" class="rounded-sm h-full" />
                        </div>
                        <div class="w-full flex flex-col gap-y-1">
                            <small class="line-clamp-1 text-neutral-600 text-sm"
                                >Nokia 6.1 plus original nokia x6 octa-core 5.8 polegadas 4gb ram 64gb rom lte 16mp 2160p impressão digital
                                smartphone desbloquea</small
                            >
                            <div class="text-sm tracking-wide flex flex-row items-center gap-x-0.5 text-dark">
                                <span>KES</span>
                                <span>10,601.00</span>
                            </div>
                        </div>
                    </li>
                    <li class="flex flex-col gap-y-2 hover:shadow px-2 py-1 cursor-pointer transition duration-200">
                        <div class="w-full max-h-[12rem] flex items-center justify-center">
                            <img src="~/assets/images/Products/Phone_2.webp" alt="" class="rounded-sm h-full" />
                        </div>
                        <div class="w-full flex flex-col gap-y-1">
                            <small class="line-clamp-1 text-neutral-600 text-sm"
                                >Nokia 6.1 plus original nokia x6 octa-core 5.8 polegadas 4gb ram 64gb rom lte 16mp 2160p impressão digital
                                smartphone desbloquea</small
                            >
                            <div class="text-sm tracking-wide flex flex-row items-center gap-x-0.5 text-dark">
                                <span>KES</span>
                                <span>10,601.00</span>
                            </div>
                        </div>
                    </li>
                    <li class="flex flex-col gap-y-2 hover:shadow px-2 py-1 cursor-pointer transition duration-200">
                        <div class="w-full max-h-[12rem] flex items-center justify-center">
                            <img src="~/assets/images/Products/Lap_2.webp" alt="" class="rounded-sm h-full" />
                        </div>
                        <div class="w-full flex flex-col gap-y-1">
                            <small class="line-clamp-1 text-neutral-600 text-sm"
                                >Nokia 6.1 plus original nokia x6 octa-core 5.8 polegadas 4gb ram 64gb rom lte 16mp 2160p impressão digital
                                smartphone desbloquea</small
                            >
                            <div class="text-sm tracking-wide flex flex-row items-center gap-x-0.5 text-dark">
                                <span>KES</span>
                                <span>10,601.00</span>
                            </div>
                        </div>
                    </li>
                </ul>
            </div>

            <div id="item-description" class="col-span-10 lg:col-span-7 flex flex-col gap-y-2 bg-gray-50 shadow-sm rounded-sm px-3 py-3">
                <div class="nav-description w-full flex flex-row justify-start items-center gap-x-3 md:gap-x-8 border-b border-neutral-200">
                    <button>Description</button>
                    <button>Customer Reviews (0)</button>
                </div>
                <div id="description-body" class="w-full flex flex-col py-2">
                    <p class="text-dark text-base break-words">
                        Feature: Brand Name: LetvItem Condition: UsedTouch Screen: YesFast Charging: Nonsupport3.5mm Headphone Port:
                        YESOperation System: AndroidRear Camera Pixel: 16MPDisplay Resolution: 2280x1080Front Camera Pixel: 16MPDesign:
                        barBattery Type: Not DetachableCharging Power: 18WFront Camera Quantity: 1Language:
                        English,Russian,German,French,Spanish,Polish,Portuguese,Italian,Turkish,Norwegian,Korean,Japanese,ArabicRAM: 4GBRear
                        Camera Quantity: 2Display Size: 5.8Screen Type: Full ScreenROM: 64GOrigin: Mainland ChinaBiometrics Technology:
                        Rear-mountedBattery Capacity(mAh): 3060Charging Interface Type: Type-CWireless Charging: NOSIM Card Quantity: 2 SIM
                        CardNFC: YESCPU Core Quantity: Octa CoreCPU Model: qualcommQualcomm Model: Snapdragon 636Cellular:
                        GSM,WCDMA,LTEStandby Time: Up To 48 HoursBrand: NokiaNokia: X6
                    </p>
                </div>
            </div>
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

.nav-description button {
    @apply text-base tracking-wide text-dark first:text-amber-600 font-light pt-3 pb-1 px-2;
    background-image: linear-gradient(currentColor, currentColor);
    background-position: 50% 100%;
    background-repeat: no-repeat;
    background-size: 0% 1px;
    transition: background-size 0.2s;
}
.nav-description button:hover,
.nav-description button:focus {
    background-size: 100% 1px;
}
</style>
