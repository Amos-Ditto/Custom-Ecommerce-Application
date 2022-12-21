<script setup lang="ts">
import { useLayoutStore } from '~~/store/layoutStore';

const storelayout = useLayoutStore();
const showauthdropdown = ref<boolean>(false);
const showcartdropdown = ref<boolean>(false);

const toggleAuthDropDown = (): void => {
    showauthdropdown.value = !showauthdropdown.value;
};
const checkDropDownToggle = (): void => {
    if (showauthdropdown.value) {
        showauthdropdown.value = !showauthdropdown.value;
    } else if (showcartdropdown.value) {
        showcartdropdown.value = !showcartdropdown.value;
    } else {
        return;
    }
};

const openLogin = (): void => {
    storelayout.toggleAuthType(false);
    showauthdropdown.value = !showauthdropdown.value;
    storelayout.closeAuth(true);
};

const openSignUp = (): void => {
    storelayout.toggleAuthType(true);
    showauthdropdown.value = !showauthdropdown.value;
    storelayout.closeAuth(true);
};
</script>
<template>
    <div class="w-full grid grid-cols-10 px-2 sm:px-4 xl:px-8 2xl:px-20 py-2 sm:py-4">
        <div class="label col-span-4 md:col-span-2">
            <NuxtLink to="/" class="label flex flex-row gap-x-2 items-center col-span-8 w-full pr-2">
                <img src="~/assets/images/alt-logo.svg" alt="" class="bg-orange-400 rounded-full w-10 h-10" />
                <span class="text-dark text-xl font-semibold tracking-wide">Odaplace</span>
            </NuxtLink>
        </div>
        <div class="nav-links col-span-6 md:col-span-8 grid grid-cols-1 md:grid-cols-10 items-center pl-1">
            <fieldset class="col-span-6 search-bar hidden md:flex flex-row w-full items-center h-8">
                <input type="search" name="search" id="search" placeholder="Search for products..." />
                <button
                    class="category relative hidden lg:flex flex-row gap-x-1 lg:gap-x-2 items-center justify-between col-span-1 px-1 lg:px-2 xl:px-3 border-y border-neutral-300 hover:border-amber-500 focus:border-amber-500 transition duration-200"
                >
                    <span class="text-sm text-neutral-600 truncate tracking-wide capitalize">All Categories</span>
                    <div class="i-carbon-chevron-down text-base text-neutral-500"></div>
                </button>
                <button class="px-4 bg-amber-500 ring-1 ring-amber-500 hover:bg-orange-500 transition-colors duration-200 rounded-r-sm">
                    <div class="i-carbon-search text-base text-gray-50"></div>
                </button>
            </fieldset>
            <div class="md:col-span-4 flex flex-row items-center justify-end gap-x-0 sm:gap-x-8">
                <div class="account relative px-3 py-2">
                    <div @click="toggleAuthDropDown" class="account-display flex flex-row items-center gap-x-1 cursor-pointer">
                        <div class="icon">
                            <div class="icon w-7 sm:w-8 text-neutral-700">
                                <IconsAccountIcon />
                            </div>
                        </div>
                        <div class="flex flex-col gap-y-0">
                            <small
                                class="text-xs font-light text-neutral-500 tracking-wide flex flex-row gap-x-0.5 items-center transition-colors duration-200 truncate"
                            >
                                Sign In
                                <div
                                    class="i-carbon-chevron-down transition-transform duration-200"
                                    :class="showauthdropdown && 'rotate-180'"
                                ></div
                            ></small>
                            <small class="text-xs sm:text-sm font-bold text-dark tracking-wide">Account</small>
                        </div>
                    </div>
                    <Transition name="drop-down">
                        <DropdownsAccountDropDown v-if="showauthdropdown" @open-login="openLogin" @open-sign-up="openSignUp" />
                    </Transition>
                </div>
                <div class="cart px-3 py-2">
                    <div
                        @click="showcartdropdown = !showcartdropdown"
                        class="cart-display flex flex-row items-center gap-x-1 cursor-pointer hover:opacity-80 transition duration-200"
                    >
                        <div class="icon">
                            <div
                                class="icon w-7 sm:w-8 text-neutral-700 relative transition-colors duration-200"
                                :class="showcartdropdown && 'text-amber-500'"
                            >
                                <IconsCartIcon />
                                <div
                                    class="count -top-2 -right-0.5 absolute px-1.5 sm:px-2 py-0.5 sm:py-1 bg-orange-400 rounded-full flex items-center justify-center"
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
                            <small class="text-xs sm:text-sm font-bold text-dark tracking-wide">$ 0.0</small>
                        </div>
                    </div>
                    <Transition name="slide-right">
                        <DropdownsCartDropDown v-if="showcartdropdown" />
                    </Transition>
                </div>
            </div>
        </div>
        <div
            v-if="showauthdropdown || showcartdropdown"
            @click="checkDropDownToggle"
            class="drop-down-toggle-container fixed top-0 bottom-0 right-0 left-0 bg-gray-400 z-40"
            :class="showcartdropdown ? 'bg-opacity-20' : 'bg-opacity-0'"
        ></div>
    </div>
</template>

<style scoped>
.nav-links input[type='search'] {
    @apply w-full px-4 ring-1 ring-neutral-300 text-base text-dark tracking-wide outline-none bg-inherit rounded-l-sm hover:ring-amber-500 focus:ring-amber-500 transition duration-200;
}
.nav-links input[type='search'],
.nav-links fieldset button {
    @apply h-full box-content py-1;
}

.account-display:hover small {
    @apply first:text-amber-500;
}
.cart-display:hover .icon {
    @apply text-amber-500;
}

.drop-down-enter-from {
    @apply -translate-y-2 opacity-5;
}
.drop-down-leave-to {
    @apply opacity-0 translate-y-1;
}

.drop-down-enter-active,
.drop-down-leave-active {
    @apply transition duration-200;
}

.slide-right-enter-from {
    @apply translate-x-full opacity-5;
}
.slide-right-leave-to {
    @apply opacity-0 translate-x-full;
}

.slide-right-enter-active,
.slide-right-leave-active {
    @apply transition duration-500;
}
</style>
