<template>
    <div
        class="w-full min-h-[10rem] xs:min-h-[12rem] sm:min-h-[14rem] max-h-[19.5rem] xs:max-h-[21rem] sm:max-h-[22rem] grid grid-rows-3 rounded-md ring-1 ring-neutral-200"
    >
        <div class="image w-full bg-neutral-200 flex items-center justify-center row-span-2 border-b border-neutral-200 cursor-pointer">
            <slot name="image"></slot>
        </div>
        <div class="card-body w-full row-span-1 flex flex-col gap-y-0.5 px-3 py-1 bg-gray-50">
            <div class="price w-full flex flex-row items-center gap-x-2">
                <small class="text-sm xs:text-base tracking-wide text-dark">$1,854</small>
                <small class="text-xs xs:text-sm line-through text-neutral-500">$1,914</small>
            </div>
            <div class="name w-full">
                <p class="line-clamp-2 text-dark text-xs">
                    Laptop 15.6-inch IPS Screen 16GB RAM 256GB SSD Intel Celeron N5095 Business Netbook Windows 10 11 Gaming Notebook Pc
                    Portable
                </p>
            </div>
            <div class="actions w-full flex flex-row justify-between items-center">
                <button class="flex flex-row items-center gap-x-1 rounded-2xl">
                    <div class="icon w-3.5 xs:w-4 h-3.5 xs:h-4 text-orange-500 flex items-center justify-center">
                        <IconsStarIcon />
                    </div>
                    <span class="text-neutral-700 tracking-wide text-xs sm:text-sm">5.0</span>
                </button>
                <button
                    class="p-[1px] items-center justify-center flex rounded-full bg-orange-500 hover:bg-opacity-80 transition-colors duration-200"
                >
                    <div class="i-carbon-add text-gray-50 text-xl xl:text-2xl"></div>
                </button>
            </div>
            <div class="seller-label w-full grid grid-cols-2 items-center pt-0.5 xs:pt-1">
                <div class="seller-name flex flex-row items-center justify-start">
                    <small class="text-xs text-neutral-500 tracking-wide truncate">Ditto Co. Ditto Co. Ditto Co. Ditto Co.</small>
                </div>
                <div class="label flex flex-row justify-end items-center gap-x-1">
                    <div class="flex items-center justify-center w-3.5 xs:w-4 h-3.5 xs:h-4 text-[dodgerblue]">
                        <IconsVerifiedIcon />
                    </div>
                    <small class="text-xs text-neutral-500 tracking-wide">Verified</small>
                </div>
            </div>
        </div>
    </div>
</template>
