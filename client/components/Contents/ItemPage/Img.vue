<template>
    <div id="img-display" class="col-span-4 hidden sm:flex flex-col gap-y-2">
        <div id="full-image" class="w-full flex items-center justify-center">
            <img src="~/assets/images/Products/Phone_2.webp" alt="" class="w-full rounded-sm" />
        </div>
        <div id="img-list" class="w-full flex flex-row flex-wrap gap-x-2 items-center">
            <div
                id="img-small"
                class="h-[50px] w-[50px] flex items-center justify-center ring-1 ring-transparent hover:ring-neutral-200 rounded transition duration-200 cursor-pointer"
            >
                <img src="~/assets/images/Products/Lap_4.webp" alt="" class="h-full" />
            </div>
            <div
                id="img-small"
                class="h-[50px] w-[50px] flex items-center justify-center ring-1 ring-transparent hover:ring-neutral-200 rounded transition duration-200 cursor-pointer"
            >
                <img src="~/assets/images/Products/Phone_1.webp" alt="" class="h-full" />
            </div>
            <div
                id="img-small"
                class="h-[50px] w-[50px] flex items-center justify-center ring-1 ring-transparent hover:ring-neutral-200 rounded transition duration-200 cursor-pointer"
            >
                <img src="~/assets/images/Products/Mens_1.webp" alt="" class="h-full" />
            </div>
            <div
                id="img-small"
                class="h-[50px] w-[50px] flex items-center justify-center ring-1 ring-transparent hover:ring-neutral-200 rounded transition duration-200 cursor-pointer"
            >
                <img src="~/assets/images/Products/Lap_2.webp" alt="" class="h-full" />
            </div>
        </div>
        <div id="share" class="w-full flex flex-col gap-y-3 border-t border-neutral-200 py-1 mt-2">
            <h4 class="text-base tracking-wide text-neutral-500">SHARE THIS PRODUCT</h4>
            <div id="socials-links" class="flex flex-row items-center w-full justify-start gap-x-3">
                <span
                    class="w-9 h-9 flex justify-center items-center rounded-full ring-1 ring-transparent hover:ring-neutral-400 p-2 transition duration-200 cursor-pointer"
                >
                    <img src="~/assets/images/Icons/linkedin.svg" alt="" class="w-full h-full" />
                </span>

                <span
                    class="w-9 h-9 flex justify-center items-center rounded-full ring-1 ring-transparent hover:ring-neutral-400 p-2 transition duration-200 cursor-pointer"
                >
                    <img src="~/assets/images/Icons/twitter.png" alt="" class="w-full h-full" />
                </span>
            </div>
        </div>
    </div>
</template>
