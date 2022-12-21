<template>
    <div
        class="min-w-[12rem] max-h-[18.5rem] xs:max-h-[19rem] sm:max-h-[20rem] grid grid-rows-3 rounded-md ring-1 ring-neutral-200 hover:shadow-md hover:ring-orange-200 transition duration-200"
    >
        <div
            id="image-slot"
            class="row-span-2 w-full bg-neutral-200 flex items-center justify-center border-b border-neutral-200 cursor-pointer"
        >
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
