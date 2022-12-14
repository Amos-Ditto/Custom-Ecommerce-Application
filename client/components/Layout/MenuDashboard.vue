<template>
    <div class="w-full py-3.5 px-2 sm:px-4 xl:px-8 2xl:px-12 border-b border-neutral-300 flex flex-row items-center justify-start">
        <div
            class="menu-drop-down relative flex flex-row gap-x-3 items-center pr-4 xs:pr-6 cursor-pointer hover:opacity-75 transition duration-200"
        >
            <div class="icon pt-0.5 w-5 sm:w-6 h-2 text-neutral-500 flex items-center">
                <IconsListIcon />
            </div>
            <div class="menu-text flex flex-row items-center gap-x-1 xs:gap-x-2">
                <span class="text-dark font-light tracking-wide text-sm xl:text-base">Categories</span>
                <div class="i-carbon-chevron-down text-dark text-sm sm:text-base"></div>
            </div>
        </div>
        <fieldset class="col-span-5 search-bar md:hidden flex flex-row w-full items-center h-6 pl-4">
            <input type="search" name="search" id="search" placeholder="Search for products..." />
            <!-- <button
                    class="category relative hidden lg:flex flex-row gap-x-1 lg:gap-x-2 items-center justify-between col-span-1 px-1 lg:px-2 xl:px-3 transition duration-200 border-y border-neutral-300 hover:border-amber-500 focus:border-amber-500"
                >
                    <span class="text-sm text-neutral-600 truncate tracking-wide capitalize">All Categories</span>
                    <div class="i-carbon-chevron-down text-base text-neutral-500"></div>
                </button> -->
            <button class="px-3 bg-amber-500 ring-1 ring-amber-500 hover:bg-orange-500 transition-colors duration-200 rounded-r-sm block">
                <div class="i-carbon-search text-base text-gray-50"></div>
            </button>
        </fieldset>
        <div class="other-links hidden sm:flex flex-row gap-x-8 items-center px-3 ml-4">
            <div class="link">
                <span>Sell on Odaplace</span>
                <div class="i-carbon-chevron-down"></div>
            </div>
            <div class="link">
                <span>Help</span>
                <div class="i-carbon-chevron-down"></div>
            </div>
        </div>
    </div>
</template>

<style scoped>
.menu-drop-down::before {
    content: '';
    @apply absolute right-0 h-3/4 w-[1px] bg-neutral-400;
}
.other-links .link {
    @apply flex flex-row gap-x-0.5 items-center cursor-pointer hover:opacity-75;
}
.other-links .link span {
    @apply text-sm xl:text-base tracking-wide text-dark transition-colors duration-200;
}
.other-links .link .i-carbon-chevron-down {
    @apply text-base text-dark transition duration-200;
}

fieldset input[type='search'] {
    @apply w-full px-2 ring-1 ring-neutral-300 text-sm text-dark tracking-wide outline-none bg-inherit rounded-l-sm hover:ring-amber-500 focus:ring-amber-500 transition duration-200;
}
fieldset input[type='search'],
fieldset button {
    @apply h-full box-content py-1;
}
</style>
