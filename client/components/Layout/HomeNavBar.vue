<template>
    <div class="w-full grid grid-cols-10 px-2 sm:px-4 xl:px-8 2xl:px-20 py-2.5 sm:py-4">
        <div class="label col-span-2">
            <NuxtLink to="/" class="label flex flex-row gap-x-2 items-center col-span-8 w-full pr-2">
                <img src="@/assets/images/Logo.webp" alt="" class="w-12 lg:w-14 h-10 lg:h-12 p-1" />
                <span class="text-dark text-lg lg:text-xl font-semibold tracking-wide">Odaplace</span>
            </NuxtLink>
        </div>
        <div class="nav-links col-span-8 grid grid-cols-10 items-center pl-1">
            <fieldset class="col-span-6 search-bar flex flex-row w-full items-center h-8">
                <input type="search" name="search" id="search" placeholder="Search for products..." />
                <button
                    class="category relative hidden lg:flex flex-row gap-x-1 lg:gap-x-2 items-center justify-between col-span-1 px-1 lg:px-2 xl:px-3 hover:opacity-75 transition duration-200 border-y border-neutral-300"
                >
                    <span class="text-base text-neutral-600 truncate capitalize">All Categories</span>
                    <div class="i-carbon-chevron-down text-base text-neutral-500"></div>
                </button>
                <button class="px-4 bg-amber-500 ring-1 ring-amber-500 hover:bg-orange-500 transition-colors duration-200">
                    <div class="i-carbon-search text-base text-gray-50"></div>
                </button>
            </fieldset>
            <div class="col-span-4 flex flex-row items-center justify-end gap-x-8">
                <div class="account flex flex-row items-center gap-x-1 relative pl-2 lg:pl-3 cursor-pointer">
                    <div class="icon">
                        <div class="icon w-10 text-neutral-700">
                            <IconsAccountIcon />
                        </div>
                    </div>
                    <div class="flex flex-col gap-y-0">
                        <small
                            class="text-xs font-light text-neutral-500 tracking-wide flex flex-row items-center transition-colors duration-200"
                            >Sign in
                            <div class="i-carbon-chevron-down"></div
                        ></small>
                        <small class="text-base font-bold text-dark tracking-wide">Account</small>
                    </div>
                </div>
                <div class="cart flex flex-row items-center gap-x-1 relative pl-2 lg:pl-3 cursor-pointer">
                    <div class="icon">
                        <div class="icon w-10 text-neutral-700 relative">
                            <IconsCartIcon />
                            <div
                                class="count -top-2 -right-0.5 absolute px-2 py-1 bg-orange-400 rounded-full flex items-center justify-center"
                            >
                                <small class="text-xs text-gray-50">0</small>
                            </div>
                        </div>
                    </div>
                    <div class="flex flex-col gap-y-0">
                        <small
                            class="text-xs font-light text-neutral-500 tracking-wide flex flex-row items-center transition-colors duration-200"
                            >Total</small
                        >
                        <small class="text-base font-bold text-dark tracking-wide">$ 0.0</small>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<style scoped>
.nav-links input[type='search'] {
    @apply w-full px-4 ring-1 ring-neutral-300 text-base text-dark tracking-wide outline-none bg-inherit;
}
.nav-links input[type='search'],
.nav-links button {
    @apply h-full box-content py-1;
}

.account:hover small {
    @apply first:text-amber-600;
}
</style>
