<template>
    <div class="w-full flex flex-col gap-y-2">
        <div class="title w-full flex flex-row items-center gap-x-2 px-3 py-2 bg-amber-500 rounded-t">
            <div class="icon w-5 text-gray-100 flex items-center pt-0.5">
                <IconsListIcon />
            </div>
            <h3 class="text-gray-100 tracking-wide text-sm 2xl:text-base font-semibold">Categories</h3>
        </div>
        <ul class="w-full flex flex-col gap-y-1 pt-2 pb-2">
            <li>
                <div class="icon w-5 text-neutral-600 flex items-center">
                    <IconsCategoriesConputersIcon />
                </div>
                <small>Computer, Office & Security</small>
                <div class="i-carbon-chevron-right absolute right-1 text-neutral-600 text-base"></div>
            </li>
            <li>
                <div class="icon w-5 text-neutral-600 flex items-center">
                    <IconsCategoriesPhonesIcon />
                </div>
                <small>Phones & Telecommunications</small>
                <div class="i-carbon-chevron-right absolute right-1 text-neutral-600 text-base"></div>
            </li>
            <li>
                <div class="icon w-5 text-neutral-600 flex items-center">
                    <IconsCategoriesTvsIcon />
                </div>
                <small>TV, Audio & Video</small>
                <div class="i-carbon-chevron-right absolute right-1 text-neutral-600 text-base"></div>
            </li>
            <li>
                <div class="icon w-5 text-neutral-600 flex items-center">
                    <IconsCategoriesHomeIcon />
                </div>
                <small>Home & Living</small>
                <div class="i-carbon-chevron-right absolute right-1 text-neutral-600 text-base"></div>
            </li>
            <li>
                <div class="icon w-5 text-neutral-600 flex items-center">
                    <IconsCategoriesClothesIcon />
                </div>
                <small>Clothes & Fashion</small>
                <div class="i-carbon-chevron-right absolute right-1 text-neutral-600 text-base"></div>
            </li>
            <li>
                <div class="icon w-5 text-neutral-600 flex items-center">
                    <IconsCategoriesBeautyIcon />
                </div>
                <small>Beauty, Health & Hair</small>
                <div class="i-carbon-chevron-right absolute right-1 text-neutral-600 text-base"></div>
            </li>
        </ul>
    </div>
</template>

<style scoped>
ul li {
    @apply flex flex-row py-2 px-3 items-center gap-x-2 relative cursor-pointer;
}
ul li small {
    @apply truncate text-xs 2xl:text-sm tracking-wide font-light text-neutral-600;
}
ul li:hover::before {
    content: '';
    @apply h-full absolute w-[2px] left-0 bg-amber-500;
}
</style>
