<script setup lang="ts">
import { useLayoutStore } from '~~/store/layoutStore';

// Handle opening Account SideBar
const storelayout = useLayoutStore();
const toggleAccountSideBar = (): void => {
    storelayout.toggleAccountSideBar();
};
</script>
<template>
    <nav
        class="w-full text-dark flex flex-row items-center justify-between px-4 2xl:px-6 py-1 md:py-3 lg:py-4 border-b border-neutral-300 bg-inherit z-30"
    >
        <div class="left flex flex-row gap-x-4 items-center">
            <div
                @click="toggleAccountSideBar"
                class="toggle-icon flex flex-col md:hidden gap-y-1 w-[2.1rem] py-1.5 px-1.5 hover:bg-gray-100 rounded-sm cursor-pointer"
            >
                <div class="bar"></div>
                <div class="bar"></div>
                <div class="bar"></div>
            </div>
        </div>
        <div
            class="user cursor-pointer flex flex-row items-center gap-x-2 md:px-2 py-1 hover:bg-gray-200 hover:bg-opacity-75 rounded transition-colors duration-200"
        >
            <div class="avatar rounded-full bg-gray-300 bg-opacity-75 flex items-center justify-center w-10 md:w-8 h-10 md:h-8">
                <!-- <img src="" alt="AD" class="w-full h-full rounded-full" /> -->
                <span class="text-base uppercase text-neutral-600 tracking-wide">AD</span>
            </div>
            <div class="name flex flex-row items-center">
                <small class="text-sm tracking-wide hidden md:block">Amos Ditto</small>
            </div>
        </div>
    </nav>
</template>

<style scoped>
.toggle-icon .bar {
    @apply w-full h-[2px] bg-neutral-500 rounded-lg transition duration-200;
}
.toggle-icon:hover .bar {
    @apply bg-opacity-80;
}
</style>
