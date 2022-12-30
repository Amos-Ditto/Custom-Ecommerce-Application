<template>
    <section class="w-full flex flex-col">
        <div
            id="item-header"
            class="w-full hidden sm:flex flex-row gap-x-2 sm:gap-x-4 items-center border-y border-neutral-200 py-3 px-2 sm:px-4 xl:px-8 2xl:px-20"
        >
            <span>Home</span>
            <div class="i-carbon-chevron-right"></div>
            <span>Phone & Accessories</span>
            <div class="i-carbon-chevron-right"></div>
            <span>Android Phones</span>
        </div>
        <div
            id="details-container"
            class="w-full py-4 px-2 sm:px-4 xl:px-8 2xl:px-20 flex flex-col sm:grid sm:grid-cols-10 gap-x-4 gap-y-8"
        >
            <div
                id="body-details"
                class="col-span-1 sm:col-span-7 grid sm:grid-cols-10 gap-x-4 gap-y-2 bg-gray-50 shadow-sm rounded-sm px-1 sm:px-3 py-3"
            >
                <ContentsItemPageImgMobile />
                <ContentsItemPageImg />

                <ContentsItemPageDetails />
            </div>
            <ContentsItemPageOtherActions />

            <ContentsItemPageRecommendedItems />
            <div
                id="item-description"
                class="col-span-1 sm:col-span-10 lg:col-span-7 flex flex-col gap-y-2 bg-gray-50 shadow-sm rounded-sm px-3 py-3"
            >
                <div class="nav-description w-full flex flex-row justify-start items-center gap-x-3 md:gap-x-8 border-b border-neutral-200">
                    <button class="text-sm sm:text-base">Description</button>
                    <button class="text-sm sm:text-base">Customer Reviews (0)</button>
                </div>
                <div id="description-body" class="w-full flex flex-col py-2">
                    <p class="text-dark text-xs sm:text-base flex-wrap flex break-words">
                        Feature: Brand Name: LetvItem Condition: UsedTouch Screen: YesFast Charging: Nonsupport3.5mm Headphone Port:
                    </p>
                </div>
            </div>
        </div>
    </section>
</template>

<style scoped>
#item-header span {
    @apply text-base font-semibold text-dark first:text-orange-600;
}
#item-header .i-carbon-chevron-right {
    @apply text-xl text-neutral-500;
}

.nav-description button {
    @apply text-base tracking-wide text-dark first:text-amber-600 font-light pt-3 pb-1 px-2;
    background-image: linear-gradient(currentColor, currentColor);
    background-position: 50% 100%;
    background-repeat: no-repeat;
    background-size: 0% 1px;
    transition: background-size 0.2s;
}
.nav-description button:hover,
.nav-description button:focus {
    background-size: 100% 1px;
}
</style>
