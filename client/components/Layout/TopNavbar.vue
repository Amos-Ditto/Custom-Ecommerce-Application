<template>
    <div class="w-full grid grid-cols-10 px-12 py-3 border-b border-neutral-300">
        <div class="left col-span-6 grid grid-cols-6 gap-x-3 items-center">
            <NuxtLink to="/" class="label flex flex-row gap-x-2 items-center col-span-1">
                <img src="@/assets/images/Logo.webp" alt="" class="w-14 h-12 p-1" />
                <span class="text-dark text-xl font-semibold tracking-wide">Odaplace</span>
            </NuxtLink>
            <div class="search col-span-5 grid grid-cols-10 gap-x-2 w-full ml-16 rounded-3xl ring-1 ring-neutral-300 px-0.5 py-1">
                <div
                    class="location col-span-2 flex flex-row gap-x-2 justify-between items-center relative px-3 hover:opacity-75 transition duration-200 cursor-pointer"
                >
                    <div class="w-5 h-5 items-center flex justify-center text-neutral-500">
                        <IconsLeafletIcon />
                    </div>
                    <span class="text-sm text-neutral-500 tracking-wide">All places</span>
                    <div class="i-carbon-chevron-down text-base text-neutral-500"></div>
                </div>
                <div class="input flex flex-row items-center col-span-5">
                    <input type="search" name="search-bar" id="search-bar" placeholder="Search for products ..." />
                </div>
                <div class="submit col-span-3 relative grid grid-cols-2 px-1 items-center">
                    <div
                        class="category relative flex flex-row gap-x-2 items-center justify-between col-span-1 px-3 cursor-pointer hover:opacity-75 transition duration-200"
                    >
                        <span class="text-sm text-neutral-600">Category</span>
                        <div class="i-carbon-chevron-down text-base text-neutral-500"></div>
                    </div>
                    <div class="search-btn col-span-1 flex items-center flex-row justify-end">
                        <button
                            class="bg-orange-500 hover:opacity-80 px-4 py-1.5 text-gray-50 tracking-wide text-base rounded-2xl flex flex-row items-center gap-x-2 transition duration-200"
                        >
                            <div class="i-carbon-search"></div>
                            Search
                        </button>
                    </div>
                </div>
            </div>
        </div>
        <div class="right col-span-4 flex flex-row gap-x-2 items-center justify-end">
            <div class="nav-actions flex flex-row gap-x-8 px-3 mr-2 items-center">
                <div
                    class="notification flex flex-row items-center justify-center relative cursor-pointer hover:opacity-70 transition duration-200"
                >
                    <div class="icon w-6 h-6 text-neutral-700">
                        <IconsBellIcon />
                    </div>
                    <!-- <div
                        class="cart-count absolute -right-1/4 -top-1/2 py-0.5 px-1.5 rounded-full bg-orange-500 flex items-center justify-center"
                    >
                        <small class="text-xs text-gray-50">0</small>
                    </div> -->
                </div>
                <div
                    class="cart flex flex-row items-center justify-center relative cursor-pointer hover:opacity-70 transition duration-200"
                >
                    <div class="icon w-6 h-6 text-neutral-700">
                        <IconsCartIcon />
                    </div>
                    <div
                        class="cart-count absolute -right-1/4 -top-1/2 py-0.5 px-1.5 rounded-full bg-orange-500 flex items-center justify-center"
                    >
                        <small class="text-xs text-gray-50">0</small>
                    </div>
                </div>
            </div>
            <div class="account flex flex-row items-center gap-x-2 relative px-6">
                <!-- <div class="user-image w-8 h-8 p-0.5 bg-gray-200 ring-1 ring-gray-400 text-gray-500 rounded-full">
                    <IconsUserIcon />
                </div> -->
                <div
                    class="name px-3 py-0.5 rounded-2xl ring-1 ring-gray-500 shadow flex flex-row justify-center items-center gap-x-3 cursor-pointer hover:opacity-70 duration-200 transition"
                >
                    <small class="text-sm tracking-wide text-dark">Amos</small>
                    <div class="i-carbon-chevron-down text-sm"></div>
                </div>
            </div>
        </div>
    </div>
</template>

<style scoped>
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
    @apply absolute right-0 h-3/4 w-[1px] bg-neutral-300;
}

.search input {
    @apply px-3 text-dark tracking-wider text-base py-1.5 outline-none bg-inherit w-full;
}
</style>
