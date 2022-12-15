<script setup lang="ts">
import { useLayoutStore } from '~~/store/layoutStore';

const storelayout = useLayoutStore();

// Mobile Side Bar toggling
const toggleAccountSideBar = (): void => {
    storelayout.toggleAccountSideBar();
};
</script>
<template>
    <main class="w-full grid grid-cols-1 md:grid-cols-10 gap-x-0 grid-rows-1 h-screen overflow-y-auto">
        <aside class="col-span-2 sticky top-0 hidden md:flex flex-col py-2 border-r border-neutral-300">
            <LayoutAccountSidebar />
        </aside>
        <div class="body-context md:col-span-8 py-0 flex flex-col min-h-screen overflow-y-auto">
            <LayoutAccountTopBar class="sticky top-0 bg-[#f5f5f5] bg-opacity-[0.95] z-30" />
            <slot />
        </div>
        <!-- Mobile Side Bar -->
        <Transition>
            <aside
                v-if="storelayout.account_side_toggle"
                class="w-screen z-40 fixed top-0 bottom-0 left-0 right-0 md:hidden py-2 border-r border-neutral-300 h-full grid grid-cols-10 grid-rows-1"
            >
                <LayoutAccountSidebar class="col-span-8 bg-gray-50" />
                <div @click="toggleAccountSideBar" class="closing-toggle col-span-2 bg-gray-400 opacity-5"></div>
                <div
                    @click="toggleAccountSideBar"
                    class="close p-2 rounded-full bg-gray-300 bg-opacity-90 hover:bg-opacity-75 cursor-pointer flex items-center justify-center absolute right-[11%] top-[10%]"
                >
                    <div class="i-carbon-close text-2xl text-neutral-700"></div>
                </div>
            </aside>
        </Transition>
    </main>
</template>

<style scoped>
/* we will explain what these classes do next! */
.v-enter-active,
.v-leave-active {
    transition: opacity 0.15s ease, right 0.25s ease, left 0.25s ease;
}

.v-enter-from,
.v-leave-to {
    /* opacity: 0;
    transform: translateX(0%); */
    @apply opacity-5 right-full -left-full top-0 bottom-0;
}
</style>
