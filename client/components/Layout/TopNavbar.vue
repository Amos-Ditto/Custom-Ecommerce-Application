<template>
    <div class="w-full grid grid-cols-10 px-2 sm:px-4 xl:px-8 2xl:px-12 py-2.5 sm:py-4 border-b border-neutral-300">
        <div class="left col-span-3 sm:col-span-7 2xl:col-span-6 grid grid-cols-8 lg:grid-cols-6 gap-x-3 items-center">
            <NuxtLink to="/" class="label flex flex-row gap-x-2 items-center col-span-8 md:col-span-1">
                <img src="@/assets/images/Logo.webp" alt="" class="w-12 lg:w-14 h-10 lg:h-12 p-1" />
                <span class="text-dark text-lg lg:text-xl font-semibold tracking-wide">Odaplace</span>
            </NuxtLink>
            <div
                class="search col-span-7 lg:col-span-5 hidden md:grid grid-cols-10 gap-x-2 w-full ml-16 rounded-3xl ring-1 ring-neutral-300 px-0.5 py-0.5 2xl:py-1"
            >
                <div
                    class="location col-span-2 flex flex-row justify-between items-center relative px-2 xl:px-3 hover:opacity-75 transition duration-200 cursor-pointer"
                >
                    <div class="w-4 xl:w-5 h-4 xl:h-5 items-center flex justify-center text-neutral-500">
                        <IconsLeafletIcon />
                    </div>
                    <span class="text-xs xl:text-sm text-neutral-500 tracking-wide flex truncate">All places</span>
                    <div class="i-carbon-chevron-down text-sm xl:text-base text-neutral-500"></div>
                </div>
                <div class="input flex flex-row items-center col-span-6 lg:col-span-5">
                    <input type="search" name="search-bar" id="search-bar" placeholder="Search for products ..." />
                </div>
                <div class="submit col-span-2 lg:col-span-3 relative grid grid-cols-1 lg:grid-cols-2 px-1 items-center justify-end">
                    <div
                        class="category relative hidden lg:flex flex-row gap-x-1 lg:gap-x-2 items-center justify-between col-span-1 px-1 lg:px-2 xl:px-3 cursor-pointer hover:opacity-75 transition duration-200"
                    >
                        <span class="text-xs xl:text-sm text-neutral-600 truncate capitalize">Category</span>
                        <div class="i-carbon-chevron-down text-base text-neutral-500"></div>
                    </div>
                    <div class="search-btn col-span-1 flex items-center flex-row justify-end">
                        <button
                            class="bg-orange-500 hover:opacity-80 px-2.5 xl:px-4 py-1.5 text-gray-50 tracking-wide text-sm xl:text-base rounded-2xl flex flex-row items-center gap-x-1 xl:gap-x-2 transition duration-200"
                        >
                            <div class="i-carbon-search"></div>
                            Search
                        </button>
                    </div>
                </div>
            </div>
        </div>
        <div class="right col-span-7 sm:col-span-3 2xl:col-span-4 flex flex-row gap-x-2 items-center justify-end">
            <div class="nav-actions flex flex-row gap-x-4 lg:gap-x-8 px-3 sm:mr-2 items-center">
                <div
                    class="cart flex flex-row items-center justify-center relative cursor-pointer rounded-full p-1 hover:bg-gray-200 transition duration-200"
                >
                    <div class="icon w-6 h-6 text-neutral-700">
                        <IconsCartIcon />
                    </div>
                    <div
                        class="cart-count absolute -right-[15%] -top-1/4 py-0.5 px-1.5 rounded-full bg-orange-500 flex items-center justify-center"
                    >
                        <small class="text-xs text-gray-50">0</small>
                    </div>
                </div>
            </div>
            <div class="account flex flex-row items-center gap-x-1 relative pl-2 lg:pl-3 cursor-pointer">
                <div class="icon">
                    <div class="icon w-10 text-neutral-700">
                        <IconsAccountIcon />
                    </div>
                </div>
                <div class="flex flex-col gap-y-0">
                    <small
                        class="text-xs font-light text-neutral-500 tracking-wide flex flex-row gap-x-0.5 items-center transition-colors duration-200"
                        >Sign in
                        <div class="i-carbon-chevron-down"></div
                    ></small>
                    <small class="text-base font-bold text-dark tracking-wide">Account</small>
                </div>
            </div>
        </div>
    </div>
</template>

<style scoped>
.account:hover small {
    @apply first:text-amber-600;
}
.account::before {
    content: '';
    @apply absolute left-0 h-3/4 w-[1px] bg-gray-400;
}
.location::before {
    content: '';
    @apply absolute right-0 h-3/4 w-[1px] bg-neutral-300;
}
.submit::before {
    content: '';
    @apply absolute left-0 h-3/4 w-[1px] bg-neutral-300;
}

.category::after {
    content: '';
    @apply absolute right-1.5 h-3/4 w-[1px] bg-neutral-300;
}

.search input {
    @apply px-1 lg:px-3 text-dark tracking-wider text-base py-1.5 outline-none bg-inherit w-full;
}
</style>
