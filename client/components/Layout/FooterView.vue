<template>
    <div
        class="w-full min-h-[5rem] grid grid-cols-2 md:grid-cols-3 lg:grid-cols-4 gap-y-4 gap-x-3 bg-gray-200 px-4 lg:px-4 xl:px-8 2xl:px-20 pt-3 pb-8"
    >
        <div id="company" class="flex flex-col gap-y-4">
            <h3 class="text-dark text-base sm:text-lg">Company</h3>
            <ul class="flex flex-col gap-y-2 w-full">
                <li>Home</li>
                <li>Trending Products</li>
                <li>Merchants</li>
            </ul>
        </div>
        <div id="resources" class="flex flex-col gap-y-4">
            <h3 class="text-dark text-base sm:text-lg">Resources</h3>
            <ul class="flex flex-col gap-y-2 w-full">
                <li>Sell Products</li>
                <li>Search products</li>
                <li>Track Orders</li>
            </ul>
        </div>

        <div id="contacts" class="col-span-2 md:col-span-1 flex flex-col gap-y-4">
            <h3 class="text-dark text-base sm:text-lg">Contact</h3>
            <ul class="flex flex-col gap-y-4 w-full">
                <li>
                    <div
                        class="icon w-7 sm:w-9 p-1.5 text-neutral-700 bg-gray-100 rounded-full items-center flex justify-center ring-1 ring-gray-300"
                    >
                        <IconsPhoneIcon />
                    </div>
                    <div id="call-details" class="flex flex-row items-center gap-x-2 sm:gap-x-3">
                        <small class="text-sm sm:text-base text-neutral-700 tracking-wide">CALL</small>
                        <small class="text-xs sm:text-sm text-neutral-700 tracking-wide">+254794818111</small>
                    </div>
                </li>
                <li>
                    <div
                        class="icon w-7 sm:w-9 p-1.5 text-neutral-700 bg-gray-100 rounded-full items-center flex justify-center ring-1 ring-gray-300"
                    >
                        <IconsMailIcon />
                    </div>
                    <div id="call-details" class="flex flex-row items-center gap-x-2 sm:gap-x-3">
                        <small class="text-sm sm:text-base text-neutral-700 tracking-wide">EMAIL</small>
                        <small class="text-xs sm:text-sm text-neutral-700 tracking-wide underline">amosk7793@gmail.com</small>
                    </div>
                </li>
            </ul>
        </div>

        <div id="socials" class="col-span-2 md:col-span-3 lg:col-span-1 flex flex-col gap-y-4">
            <div id="logo-footer" class="w-full hidden lg:flex items-center justify-center flex-col gap-y-1">
                <!-- <img src="~/assets/images/alt-logo.svg" alt="" class="bg-orange-400 w-16 h-16 rounded-full" /> -->
                <span class="text-2xl tracking-wide text-dark">Odaplace</span>
            </div>
            <div id="socials-links" class="flex flex-row items-center w-full justify-center gap-x-6">
                <span
                    class="w-8 sm:w-10 h-8 sm:h-10 flex justify-center items-center rounded-full ring-1 ring-transparent hover:ring-neutral-400 p-2 transition duration-200 cursor-pointer"
                >
                    <img src="~/assets/images/Icons/linkedin.svg" alt="" class="w-full h-full" />
                </span>
                <span
                    class="w-8 sm:w-10 h-8 sm:h-10 flex justify-center items-center rounded-full ring-1 ring-transparent hover:ring-neutral-400 p-2 transition duration-200 cursor-pointer"
                >
                    <img src="~/assets/images/Icons/github.svg" alt="" class="w-full h-full" />
                </span>

                <span
                    class="w-8 sm:w-10 h-8 sm:h-10 flex justify-center items-center rounded-full ring-1 ring-transparent hover:ring-neutral-400 p-2 transition duration-200 cursor-pointer"
                >
                    <img src="~/assets/images/Icons/twitter.png" alt="" class="w-full h-full" />
                </span>
            </div>
        </div>
    </div>
</template>

<style scoped>
#company ul li,
#resources ul li {
    @apply w-full text-xs sm:text-sm font-light text-neutral-700 py-1 tracking-wide;
}

#contacts ul li {
    @apply flex flex-row items-center gap-x-3;
}
</style>
