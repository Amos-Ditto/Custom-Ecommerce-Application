<script setup lang="ts">
const emits = defineEmits<{
    (e: 'openLogin'): void;
    (e: 'openSignUp'): void;
}>();
</script>
<template>
    <div
        class="account-dropdown flex flex-col min-w-[13.5rem] w-auto min-h-[10rem] bg-white shadow rounded z-50 py-3 absolute top-[102%] right-0"
    >
        <div class="sign-auth flex flex-col gap-y-2.5 px-3 pb-2 border-b border-neutral-200 w-full">
            <small class="text-base font-light text-neutral-600">Welcome to Odaplace!</small>
            <div class="auth-options flex flex-row justify-between gap-x-2 items-center">
                <button
                    @click="emits('openLogin')"
                    class="px-5 py-1.5 text-sm tracking-wide rounded-sm bg-orange-500 bg-opacity-80 hover:bg-opacity-100 text-gray-50 font-semibold transition duration-200"
                >
                    Sign Up
                </button>
                <button
                    @click="emits('openSignUp')"
                    class="px-5 py-1.5 text-sm tracking-wide rounded-sm bg-orange-600 bg-opacity-10 font-semibold hover:bg-opacity-20 transition duration-200"
                >
                    Login
                </button>
            </div>
        </div>
        <ul class="w-full flex flex-col gap-y-1">
            <li>
                <div class="w-4 scale-110 text-neutral-700">
                    <IconsBoxIcon />
                </div>
                <span>My Orders</span>
            </li>
            <li>
                <div class="w-4 scale-110 text-neutral-700">
                    <IconsHeartIcon />
                </div>
                <span>My Favorite</span>
            </li>
            <li>
                <div class="w-4 scale-110 text-neutral-700">
                    <IconsUserIcon />
                </div>
                <span>My Account</span>
            </li>

            <li>
                <div class="w-4 scale-110 text-neutral-700">
                    <IconsHomeCogIcon />
                </div>
                <span>Merchant</span>
            </li>
        </ul>
    </div>
</template>

<style scoped>
.account-dropdown ul li {
    @apply flex flex-row gap-x-2 items-center px-3 py-2 hover:bg-gray-200 transition duration-200 cursor-pointer;
}
.account-dropdown ul li span {
    @apply text-sm font-light tracking-wide text-neutral-700;
}
</style>
