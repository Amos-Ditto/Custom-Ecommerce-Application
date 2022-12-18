<template>
    <main>
        <NuxtPage />
        <div
            class="auth-modals fixed top-0 bottom-0 left-0 right-0 flex justify-center z-40 bg-gray-400 bg-opacity-40 overflow-y-auto py-[4rem]"
        >
            <div class="login-container w-[30rem] bg-gray-50 shadow-md rounded min-h-[20rem] px-[1.8rem] py-[1.8rem] flex flex-col gap-y-3">
                <div class="email-signup w-full flex flex-col gap-y-8">
                    <div class="input-fields w-full flex flex-col gap-y-6">
                        <div class="input w-full flex flex-row items-center relative">
                            <input type="email" name="mail" id="mail" placeholder="Email" />
                            <div class="icon w-5 text-neutral-600 flex items-center absolute left-2">
                                <IconsMailIcon />
                            </div>
                        </div>
                        <div class="input w-full flex flex-row items-center relative">
                            <input type="password" name="password" id="password" placeholder="Password" />
                            <div class="icon w-5 text-neutral-600 flex items-center absolute left-2">
                                <IconsLockIcon />
                            </div>
                        </div>
                        <div class="more-actions w-full flex flex-row items-center justify-end">
                            <small class="text-[dodgerblue] text-sm">Forgot Password?</small>
                        </div>
                    </div>
                </div>
            </div>
        </div>
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

.input-fields .input input {
    @apply w-full py-2 ring-1 ring-neutral-200 rounded-sm pl-9 pr-4 outline-none tracking-wide bg-white hover:ring-neutral-300 focus:ring-neutral-300 transition duration-200;
}
</style>
