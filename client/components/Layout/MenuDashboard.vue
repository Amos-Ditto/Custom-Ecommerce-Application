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
</style>
