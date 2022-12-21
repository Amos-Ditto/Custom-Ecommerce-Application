<script setup lang="ts">
import { useLayoutStore } from './store/layoutStore';

const storelayout = useLayoutStore();
</script>
<template>
    <main>
        <NuxtPage />
        <Transition name="auth-pop-up">
            <AuthenticationAuthContainer v-if="storelayout.showauth" />
        </Transition>
    </main>
</template>

<style>
body {
    line-height: 1.5;
    font-family: 'Nunito', sans-serif;
    display: flex;
    flex-direction: column;
    position: relative;
    padding: 0;
    margin: 0;
    box-sizing: border-box;
    -webkit-tap-highlight-color: transparent;
    outline: none;
    @apply bg-[#f5f5f5];
}

.page-enter-active,
.page-leave-active {
    transition: all 0.4s;
}
.page-enter-from {
    opacity: 0;
    @apply -translate-y-0.5;
}
.page-leave-to {
    opacity: 0;
}

.auth-pop-up-enter-active,
.auth-pop-up-leave-active {
    transition: all 0.4s;
}
.auth-pop-up-enter-from {
    opacity: 0;
    @apply scale-50;
}
.auth-pop-up-leave-to {
    opacity: 0;
}

::-webkit-scrollbar {
    width: 5px;
    height: 5px;
    border-radius: 32px;
}
::-webkit-scrollbar-corner {
    background-color: #f9fbff;
}
::-webkit-scrollbar-thumb {
    @apply bg-neutral-400;
    border-radius: 32px;
}
::-webkit-scrollbar-track {
    background-color: #f9fbff;
}
</style>
