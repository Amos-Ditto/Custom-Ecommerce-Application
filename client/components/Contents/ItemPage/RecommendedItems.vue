<template>
    <div
        id="recommended-items"
        class="col-span-1 sm:col-span-10 lg:col-span-7 flex flex-col gap-y-2 bg-gray-50 shadow-sm rounded-sm sm:px-3 py-3"
    >
        <div class="w-full pb-1 border-b border-neutral-200 px-2">
            <h4 class="text-base sm:text-lg tracking-wide capitalize text-neutral-600">Customers who viewed this also viewed</h4>
        </div>
        <ul id="recommended-list" class="w-[90vw] sm:w-full flex flex-row overflow-x-auto sm:grid grid-cols-6 gap-x-4 gap-y-4 px-1">
            <li class="flex flex-col gap-y-2 hover:shadow px-2 py-1 cursor-pointer transition duration-200">
                <div class="w-full h-[8rem] min-w-[8rem] flex items-center justify-center">
                    <img src="~/assets/images/Products/Lap_4.webp" alt="" class="rounded-sm h-full w-full" />
                </div>
                <div class="w-full flex flex-col gap-y-1">
                    <small class="line-clamp-1 text-neutral-600 text-xs sm:text-sm"
                        >Nokia 6.1 plus original nokia x6 octa-core 5.8 polegadas 4gb ram 64gb rom lte 16mp 2160p impressão digital
                        smartphone desbloquea</small
                    >
                    <div class="text-xs sm:text-sm tracking-wide flex flex-row items-center gap-x-0.5 text-dark">
                        <span>KES</span>
                        <span>10,601.00</span>
                    </div>
                </div>
            </li>
            <li class="flex flex-col gap-y-2 hover:shadow px-2 py-1 cursor-pointer transition duration-200">
                <div class="w-full h-[8rem] min-w-[8rem] flex items-center justify-center">
                    <img src="~/assets/images/Products/Phone_1.webp" alt="" class="rounded-sm h-full w-full" />
                </div>
                <div class="w-full flex flex-col gap-y-1">
                    <small class="line-clamp-1 text-neutral-600 text-sm"
                        >Nokia 6.1 plus original nokia x6 octa-core 5.8 polegadas 4gb ram 64gb rom lte 16mp 2160p impressão digital
                        smartphone desbloquea</small
                    >
                    <div class="text-xs sm:text-sm tracking-wide flex flex-row items-center gap-x-0.5 text-dark">
                        <span>KES</span>
                        <span>10,601.00</span>
                    </div>
                </div>
            </li>
            <li class="flex flex-col gap-y-2 hover:shadow px-2 py-1 cursor-pointer transition duration-200">
                <div class="w-full h-[8rem] min-w-[8rem] flex items-center justify-center">
                    <img src="~/assets/images/Products/Lap_1.webp" alt="" class="rounded-sm h-full w-full" />
                </div>
                <div class="w-full flex flex-col gap-y-1">
                    <small class="line-clamp-1 text-neutral-600 text-sm"
                        >Nokia 6.1 plus original nokia x6 octa-core 5.8 polegadas 4gb ram 64gb rom lte 16mp 2160p impressão digital
                        smartphone desbloquea</small
                    >
                    <div class="text-xs sm:text-sm tracking-wide flex flex-row items-center gap-x-0.5 text-dark">
                        <span>KES</span>
                        <span>10,601.00</span>
                    </div>
                </div>
            </li>
            <li class="flex flex-col gap-y-2 hover:shadow px-2 py-1 cursor-pointer transition duration-200">
                <div class="w-full h-[8rem] min-w-[8rem] flex items-center justify-center">
                    <img src="~/assets/images/Products/Mens_1.webp" alt="" class="rounded-sm h-full w-full" />
                </div>
                <div class="w-full flex flex-col gap-y-1">
                    <small class="line-clamp-1 text-neutral-600 text-sm"
                        >Nokia 6.1 plus original nokia x6 octa-core 5.8 polegadas 4gb ram 64gb rom lte 16mp 2160p impressão digital
                        smartphone desbloquea</small
                    >
                    <div class="text-xs sm:text-sm tracking-wide flex flex-row items-center gap-x-0.5 text-dark">
                        <span>KES</span>
                        <span>10,601.00</span>
                    </div>
                </div>
            </li>
            <li class="flex flex-col gap-y-2 hover:shadow px-2 py-1 cursor-pointer transition duration-200">
                <div class="w-full h-[8rem] min-w-[8rem] flex items-center justify-center">
                    <img src="~/assets/images/Products/Phone_2.webp" alt="" class="rounded-sm h-full w-full" />
                </div>
                <div class="w-full flex flex-col gap-y-1">
                    <small class="line-clamp-1 text-neutral-600 text-sm"
                        >Nokia 6.1 plus original nokia x6 octa-core 5.8 polegadas 4gb ram 64gb rom lte 16mp 2160p impressão digital
                        smartphone desbloquea</small
                    >
                    <div class="text-xs sm:text-sm tracking-wide flex flex-row items-center gap-x-0.5 text-dark">
                        <span>KES</span>
                        <span>10,601.00</span>
                    </div>
                </div>
            </li>
            <li class="flex flex-col gap-y-2 hover:shadow px-2 py-1 cursor-pointer transition duration-200">
                <div class="w-full h-[8rem] min-w-[8rem] flex items-center justify-center">
                    <img src="~/assets/images/Products/Lap_2.webp" alt="" class="rounded-sm h-full w-full" />
                </div>
                <div class="w-full flex flex-col gap-y-1">
                    <small class="line-clamp-1 text-neutral-600 text-sm"
                        >Nokia 6.1 plus original nokia x6 octa-core 5.8 polegadas 4gb ram 64gb rom lte 16mp 2160p impressão digital
                        smartphone desbloquea</small
                    >
                    <div class="text-xs sm:text-sm tracking-wide flex flex-row items-center gap-x-0.5 text-dark">
                        <span>KES</span>
                        <span>10,601.00</span>
                    </div>
                </div>
            </li>
        </ul>
    </div>
</template>

<style scoped>
#recommended-list::-webkit-scrollbar {
    width: 0px;
    height: 1px;
    border-radius: 32px;
}
#recommended-list::-webkit-scrollbar-thumb {
    @apply bg-neutral-400;
    border-radius: 32px;
}
#recommended-list::-webkit-scrollbar-track {
    background-color: #f9fbff;
}
</style>
