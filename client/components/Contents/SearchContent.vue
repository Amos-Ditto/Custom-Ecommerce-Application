<template>
    <div class="w-full flex flex-col gap-y-2">
        <div class="search-content-bar w-full grid grid-cols-2 items-center">
            <div class="search-text flex flex-row gap-x-3 items-center">
                <h5 class="text-dark tracking-wide text-base font-semibold">No search yet ...</h5>
            </div>
        </div>
        <div class="filter-content w-full flex flex-row gap-x-4 items-center justify-start py-1">
            <div class="filters flex flex-row items-center gap-x-3">
                <button>
                    <small class="text-neutral-600 tracking-wide text-sm">Verified Sellers</small>
                    <div class="icon p-0.5 rounded-full bg-gray-300 flex items-center justify-center">
                        <div class="i-carbon-close"></div>
                    </div>
                </button>
                <button>
                    <small class="text-neutral-600 tracking-wide text-sm">Under - $500</small>
                    <div class="icon p-0.5 rounded-full bg-gray-300 flex items-center justify-center">
                        <div class="i-carbon-close"></div>
                    </div>
                </button>
            </div>
            <clear class="filters flex flex-row items-center">
                <span class="font-semibold tracking-wide capitalize text-amber-500 text-base cursor-pointer">clear all filters</span>
            </clear>
        </div>
    </div>
</template>

<style scoped>
.filters button {
    @apply px-4 py-2 ring-1 ring-neutral-300 flex flex-row gap-x-3 items-center rounded-3xl;
}
</style>
