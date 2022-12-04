<template>
    <header class="w-full flex flex-col gap-y-2">
        <div class="search-content-bar w-full grid grid-cols-2 items-center">
            <div class="search-text flex flex-row gap-x-3 items-center">
                <h5 class="text-dark tracking-wide text-base font-semibold hidden md:block">No search yet ...</h5>
                <button class="md:hidden flex flex-row items-center gap-x-2 ring-1 ring-neutral-300 rounded px-2 py-1">
                    <div class="flex items-center justify-center w-4 h-4 text-neutral-600">
                        <IconsFilterIcon />
                    </div>
                    <span class="text-sm tracking-wide text-neutral-700">Filters</span>
                    <div class="i-carbon-chevron-right ml-1"></div>
                </button>
            </div>
            <div class="other-menu flex flex-row items-center justify-end">
                <div class="sort-by flex flex-row items-center gap-x-2">
                    <small class="text-sm tracking-wide text-neutral-600">Sort by:</small>
                    <button class="px-3 py-1 ring-1 ring-neutral-200 rounded-sm flex flex-row gap-x-2 items-center">
                        <span class="text-base tracking-wide text-neutral-700 capitalize">Best Match</span>
                        <div class="i-carbon-chevron-down"></div>
                    </button>
                </div>
            </div>
        </div>
        <div class="filter-content overflow-x-auto w-[94vw] md:w-full flex flex-row gap-x-4 items-center justify-start py-1 pl-1 pr-3">
            <div class="filters flex flex-row items-center gap-x-3">
                <button>
                    <small class="text-neutral-600 tracking-wide text-xs xl:text-sm">Verified Sellers</small>
                    <div class="icon p-0.5 rounded-full bg-gray-200 hover:bg-gray-300 flex items-center justify-center">
                        <div class="i-carbon-close"></div>
                    </div>
                </button>
                <button>
                    <small class="text-neutral-600 tracking-wide text-xs xl:text-sm">Verified Sellers</small>
                    <div class="icon p-0.5 rounded-full bg-gray-200 hover:bg-gray-300 flex items-center justify-center">
                        <div class="i-carbon-close"></div>
                    </div>
                </button>
                <button>
                    <small class="text-neutral-600 tracking-wide text-xs xl:text-sm">Verified Sellers</small>
                    <div class="icon p-0.5 rounded-full bg-gray-200 hover:bg-gray-300 flex items-center justify-center">
                        <div class="i-carbon-close"></div>
                    </div>
                </button>
                <button>
                    <small class="text-neutral-600 tracking-wide text-xs xl:text-sm">Under - $500</small>
                    <div class="icon p-0.5 rounded-full bg-gray-200 hover:bg-gray-300 flex items-center justify-center">
                        <div class="i-carbon-close"></div>
                    </div>
                </button>
            </div>
            <div class="filters flex flex-row items-center">
                <span class="font-semibold tracking-wide capitalize text-amber-500 text-base cursor-pointer truncate"
                    >clear all filters</span
                >
            </div>
        </div>
    </header>
</template>

<style scoped>
.filters button {
    @apply px-3 xl:px-4 py-1.5 xl:py-2 ring-1 ring-neutral-300 flex flex-row gap-x-2 xl:gap-x-3 items-center rounded-3xl truncate;
}

.filter-content::-webkit-scrollbar {
    width: 0px;
    height: 0px;
}
.filter-content::-webkit-scrollbar-corner {
    background-color: #f9fbff;
}
.filter-content::-webkit-scrollbar-thumb {
    @apply bg-neutral-400;
    border-radius: 32px;
}
.filter-content::-webkit-scrollbar-track {
    background-color: #f9fbff;
}
</style>
