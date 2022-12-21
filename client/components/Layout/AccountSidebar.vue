<template>
    <div class="w-full flex flex-col gap-y-3 relative h-full shadow-md">
        <div
            class="user-display w-full px-2 lg:px-4 2xl:px-6 py-3 md:py-2 flex flex-row justify-between items-center border-b border-neutral-300 cursor-pointer hover:opacity-80"
        >
            <div class="user-name flex flex-row gap-x-2 items-center">
                <img src="~/assets/images/alt-logo.svg" alt="" class="bg-orange-400 rounded-full w-10 h-10" />
                <small class="text-xl 2xl:text-xl text-dark tracking-wide font-bold">Odaplace</small>
            </div>
        </div>
        <div class="menu-context flex flex-col gap-y-2 px-2 2xl:px-3">
            <div class="user-display w-full px-1 lg:px-3 py-2 flex flex-row justify-between items-center">
                <span class="text-neutral-500 text-base uppercase tracking-wide">menu</span>
                <div class="i-carbon-add text-neutral-600 text-lg"></div>
            </div>
            <ul class="w-full flex flex-col gap-y-3">
                <li>
                    <NuxtLink :to="{ name: 'Account-Dashboard' }">
                        <div class="icon w-5 text-neutral-700">
                            <IconsDashboardIcon />
                        </div>
                        <span>Dashboard</span>
                    </NuxtLink>
                </li>
                <li>
                    <NuxtLink :to="{ name: 'Products' }">
                        <div class="icon w-5 text-neutral-700">
                            <IconsLabelIcon />
                        </div>
                        <span>Products</span>
                    </NuxtLink>
                </li>

                <li>
                    <NuxtLink :to="{ name: 'Orders' }">
                        <div class="icon w-5 text-neutral-700">
                            <IconsListIcon />
                        </div>
                        <span>Orders</span>
                    </NuxtLink>
                </li>

                <li>
                    <NuxtLink :to="{ name: 'Customers' }">
                        <div class="icon w-5 text-neutral-700">
                            <IconsUsersIcon />
                        </div>
                        <span>Customers</span>
                    </NuxtLink>
                </li>

                <li>
                    <NuxtLink :to="{ name: 'Discounts' }">
                        <div class="icon w-5 text-neutral-700">
                            <IconsDiscountIcon />
                        </div>
                        <span>Discounts</span>
                    </NuxtLink>
                </li>
            </ul>
        </div>
        <div class="settings w-full absolute left-0 bottom-2 px-4 flex flex-col gap-y-4 border-t border-neutral-300 py-3">
            <h4 class="text-base text-neutral-500 tracking-wide uppercase">setting</h4>
            <div class="setting-links w-full flex flex-col lg:flex-row gap-y-2 gap-x-3">
                <NuxtLink
                    :to="{ name: 'Home' }"
                    class="set w-full flex flex-row items-center gap-x-3 px-2 py-2 cursor-pointer hover:bg-gray-200 hover:ring-1 ring-neutral-300 rounded transition duration-200"
                >
                    <div class="icon w-4 text-neutral-700">
                        <IconsHomeIcon />
                    </div>
                    <span class="text-sm text-neutral-700 tracking-wide">Home</span>
                </NuxtLink>
                <div
                    class="set w-full flex flex-row items-center gap-x-3 px-2 py-2 cursor-pointer hover:bg-gray-200 hover:ring-1 ring-neutral-300 rounded transition duration-200"
                >
                    <div class="icon w-4 text-neutral-700">
                        <IconsAccountIcon />
                    </div>
                    <span class="text-sm text-neutral-700 tracking-wide transition-colors duration-200">Profile</span>
                </div>
            </div>
        </div>
    </div>
</template>

<style scoped>
.menu-context ul li a {
    @apply px-2 lg:px-4 py-2 flex flex-row gap-x-3 items-center hover:ring-1 ring-neutral-200 hover:bg-gray-100 cursor-pointer transition duration-200 rounded-sm;
}
.menu-context ul li .router-link-exact-active {
    @apply ring-1 bg-gray-100;
}
.menu-context ul li span {
    @apply tracking-wide text-sm text-neutral-700 transition-colors duration-200;
}
.menu-context ul li:hover span,
.menu-context ul li:hover .icon {
    @apply text-orange-500;
}
.menu-context ul li .router-link-exact-active {
    @apply ring-1 bg-gray-100;
}
.menu-context ul li .router-link-exact-active span,
.menu-context ul li .router-link-exact-active .icon {
    @apply text-orange-500;
}
.menu-context ul li span,
.menu-context ul li .icon {
    @apply transition-colors duration-200;
}

.setting-links .set:hover span,
.setting-links .set:hover .icon {
    @apply text-dark;
}
.icon {
    @apply transition-colors duration-200;
}
</style>
