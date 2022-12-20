<script setup lang="ts">
import { useLayoutStore } from '~~/store/layoutStore';

const storelayout = useLayoutStore();
</script>
<template>
    <div
        class="auth-modals fixed top-0 bottom-0 left-0 right-0 flex justify-center items-start sm:items-center z-40 overflow-y-auto py-[4rem]"
    >
        <div class="w-[80vw] sm:w-[28rem] bg-gray-50 shadow-md rounded z-40">
            <Transition name="slide" mode="out-in">
                <AuthenticationLoginModal v-if="storelayout.toggleauths" />
                <AuthenticationRegistrationModal v-else />
            </Transition>
        </div>
        <div
            class="close-auth absolute top-0 bottom-0 left-0 right-0 bg-gray-400 bg-opacity-40 z-30"
            @click="storelayout.closeAuth(false)"
        ></div>
    </div>
</template>

<style scoped>
.slide-enter-active,
.slide-leave-active {
    transition: all 0.25s ease-out;
}

.slide-enter-from {
    opacity: 0;
    transform: translateX(30px);
}

.slide-leave-to {
    opacity: 0;
    transform: translateX(-30px);
}
</style>
