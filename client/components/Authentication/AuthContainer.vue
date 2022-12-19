<script setup lang="ts">
const toggleauths = ref<boolean>(false);
</script>
<template>
    <div
        class="auth-modals fixed top-0 bottom-0 left-0 right-0 flex justify-center items-start sm:items-center z-40 bg-gray-400 bg-opacity-40 overflow-y-auto py-[4rem]"
    >
        <div class="w-[80vw] sm:w-[28rem] bg-gray-50 shadow-md rounded">
            <Transition name="slide" mode="out-in">
                <AuthenticationLoginModal v-if="toggleauths" />
                <AuthenticationRegistrationModal v-else />
            </Transition>
        </div>
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
