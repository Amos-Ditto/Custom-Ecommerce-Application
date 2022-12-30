<script setup lang="ts">
import { useLayoutStore } from '~~/store/layoutStore';

const storelayout = useLayoutStore();
</script>
<template>
    <div class="register-container flex flex-col gap-y-2 sm:gap-y-6">
        <div class="header w-full flex flex-col gap-y-0 sm:gap-y-1 px-6 py-4 items-center justify-center">
            <h3 class="text-xl sm:text-2xl text-neutral-600 tracking-wide">Join Now</h3>
            <p class="text-base text-neutral-500">And explore products or sell!</p>
        </div>
        <div class="forms-process py-2 px-6 flex flex-col gap-y-6 sm:gap-y-12">
            <div class="email-signup w-full flex flex-col gap-y-5">
                <div class="input-fields w-full flex flex-col gap-y-6">
                    <div class="input w-full flex flex-row items-center relative">
                        <input type="email" name="mail" id="mail" placeholder="Email" />
                        <div class="icon flex items-center absolute left-2">
                            <IconsMailIcon />
                        </div>
                    </div>
                    <div class="input w-full flex flex-row items-center relative">
                        <input type="password" name="password" id="password" placeholder="Password" />
                        <div class="icon flex items-center absolute left-2">
                            <IconsLockIcon />
                        </div>
                        <div class="toggle-pass-view absolute right-3.5 flex flex-col items-center justify-center h-full">
                            <div class="icon flex items-center">
                                <IconsEyeIcon />
                            </div>
                            <div class="icon hidden items-center">
                                <IconsEyeCloseIcon />
                            </div>
                        </div>
                    </div>
                    <div class="input w-full flex flex-row items-center relative">
                        <input type="password" name="password" id="c-password" placeholder="Confirm Password" />
                        <div class="icon flex items-center absolute left-2">
                            <IconsLockIcon />
                        </div>
                        <div class="toggle-pass-view absolute right-3.5 flex flex-col items-center justify-center h-full">
                            <div class="icon flex items-center">
                                <IconsEyeIcon />
                            </div>
                            <div class="icon hidden items-center">
                                <IconsEyeCloseIcon />
                            </div>
                        </div>
                    </div>
                </div>
                <div class="submit-btn w-full flex flex-row items-center">
                    <button
                        class="w-full py-2.5 rounded-sm bg-amber-500 bg-opacity-90 hover:bg-opacity-100 text-gray-50 tracking-wide uppercase text-sm sm:text-base font-light shadow-md transition duration-200"
                    >
                        Sign Up
                    </button>
                </div>
            </div>
            <div class="social-auths w-full flex flex-col gap-y-4 sm:gap-y-6">
                <div class="or-bar w-full flex flex-row items-center justify-between">
                    <span class="h-[1px] w-[38%] sm:w-[34%] bg-neutral-300"></span>
                    <span class="text-neutral-500 text-base sm:text-lg tracking-wide">OR</span>
                    <span class="h-[1px] w-[38%] sm:w-[34%] bg-neutral-300"></span>
                </div>
                <div class="social-options w-full flex flex-col gap-y-2">
                    <button
                        class="flex flex-row items-center justify-center relative py-2.5 sm:py-3 rounded ring-1 ring-neutral-200 bg-white hover:bg-opacity-30 hover:ring-neutral-300 focus:bg-opacity-30 focus:ring-neutral-300 transition duration-200"
                    >
                        <img src="~/assets/images/Icons/G-auth.png" alt="" class="absolute left-2" />
                        <span class="text-sm sm:text-base font-light tracking-wide text-neutral-600">Sign up in with Google</span>
                    </button>
                </div>
            </div>
        </div>

        <div
            class="not-registered w-full flex flex-col items-center justify-center gap-y-3 sm:gap-y-4 py-2 sm:py-3 px-2 bg-gray-100 rounded-b"
        >
            <div class="flex flex-row gap-x-2">
                <small class="text-base text-neutral-600 font-light">Already have an account?</small>
                <span
                    @click="storelayout.toggleAuthType(true)"
                    class="text-[dodgerblue] text-base tracking-wide font-light hover:text-[steelblue] transition-colors duration-200 cursor-pointer"
                    >Log In</span
                >
            </div>
            <p class="text-xs text-neutral-500">I accept the site Terms of Service and agree to the Privacy Policy.</p>
        </div>
    </div>
</template>
<style scoped>
.input-fields .input input {
    @apply w-full text-sm sm:text-base py-2 ring-1 ring-neutral-200 rounded-sm px-9 outline-none tracking-wide bg-white hover:ring-neutral-300 focus:ring-neutral-300 transition duration-200;
}

.input .icon {
    @apply w-4 sm:w-5 text-neutral-500;
}
</style>
