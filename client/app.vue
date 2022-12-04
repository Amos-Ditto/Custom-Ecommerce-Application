<template>
    <main>
        <NuxtPage />
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
