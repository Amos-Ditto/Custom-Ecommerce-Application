<!-- <script setup lang="ts">
defineProps<{
    img: string
}>()
</script> -->

<template>
    <div class="w-full min-h-[14rem] max-h-[22rem] grid grid-rows-3 rounded-md ring-1 ring-neutral-200">
        <div class="image w-full bg-neutral-200 flex items-center justify-center row-span-2 border-b border-neutral-200 cursor-pointer">
            <slot name="image"></slot>
        </div>
        <div class="card-body w-full row-span-1 flex flex-col gap-y-0.5 px-3 py-1 bg-gray-50">
            <div class="price w-full flex flex-row items-center gap-x-2">
                <small class="text-base tracking-wide text-dark">$1,854</small>
                <small class="text-sm line-through text-neutral-500">$1,914</small>
            </div>
            <div class="name w-full">
                <p class="line-clamp-2 text-dark text-xs">
                    Laptop 15.6-inch IPS Screen 16GB RAM 256GB SSD Intel Celeron N5095 Business Netbook Windows 10 11 Gaming Notebook Pc
                    Portable
                </p>
            </div>
            <div class="actions w-full flex flex-row justify-between items-center pt-0.5">
                <button class="flex flex-row items-center px-2 py-0.5 gap-x-1.5 rounded-2xl bg-amber-400">
                    <div class="icon w-4 h-4 text-gray-50 flex items-center justify-center">
                        <IconsStarIcon />
                    </div>
                    <span class="text-gray-50 tracking-wide text-sm">5.0</span>
                </button>
                <button class="py-1 px-1.5 items-center justify-center flex rounded-full bg-orange-500">
                    <div class="icon w-4 h-4 text-gray-200 flex items-center justify-center">
                        <IconsCartIcon />
                    </div>
                </button>
            </div>
            <div class="seller-label w-full flex flex-row items-center justify-start pt-1 gap-x-2">
                <div class="flex items-center justify-center w-4 h-4 text-[dodgerblue]">
                    <IconsVerifiedIcon />
                </div>
                <small class="text-xs text-neutral-500 tracking-wide">Verified</small>
            </div>
        </div>
    </div>
</template>
