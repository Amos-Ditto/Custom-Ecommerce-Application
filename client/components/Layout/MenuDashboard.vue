<template>
    <div class="w-full py-3 px-12 border-b border-neutral-300 flex flex-row items-center justify-start">
        <div
            class="menu-drop-down relative flex flex-row gap-x-3 items-center pr-6 cursor-pointer hover:opacity-75 transition duration-200"
        >
            <div class="icon w-6 h-2 text-neutral-500 flex items-center">
                <IconsListIcon />
            </div>
            <div class="menu-text flex flex-row items-center gap-x-2">
                <span class="text-dark font-light tracking-wide">Categories</span>
                <div class="i-carbon-chevron-down text-dark text-base"></div>
            </div>
        </div>
    </div>
</template>

<style scoped>
.menu-drop-down::before {
    content: '';
    @apply absolute right-0 h-3/4 w-[1px] bg-neutral-400;
}
</style>
