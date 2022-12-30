<template>
    <ul id="mobile-item-img-view" class="w-[90vw] flex flex-row sm:hidden gap-x-2 overflow-x-auto py-0.5">
        <li class="flex items-center justify-center">
            <img src="~/assets/images/Products/Phone_2.webp" alt="" class="rounded-sm h-[56vh] min-w-[85vw]" />
        </li>
        <li class="flex items-center justify-center">
            <img src="~/assets/images/Products/Phone_1.webp" alt="" class="rounded-sm h-[56vh] min-w-[85vw]" />
        </li>
        <li class="flex items-center justify-center">
            <img src="~/assets/images/Products/Mens_1.webp" alt="" class="rounded-sm h-[56vh] min-w-[85vw]" />
        </li>
    </ul>
</template>

<style scoped>
#mobile-item-img-view::-webkit-scrollbar {
    width: 0px;
    height: 1px;
    border-radius: 32px;
}
#mobile-item-img-view::-webkit-scrollbar-thumb {
    @apply bg-neutral-400;
    border-radius: 32px;
}
#mobile-item-img-view::-webkit-scrollbar-track {
    background-color: #f9fbff;
}
</style>
