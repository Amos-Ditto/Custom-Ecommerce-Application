<script setup lang="ts">
import { useAuthStore } from "../../../stores/authStore";
import { GetToken } from "../../../graphql/schema";
import { IRefreshToken } from "../../../types";

interface ILoginDetail {
	email: string;
	password: string;
}
const form_details = ref<ILoginDetail>({
	email: "",
	password: "",
});

const { mutate: postAuthDetails, loading, error: submitError, onDone } = useMutation(GetToken);
const authStore = useAuthStore();
const router = useRouter();
const { onLogin } = useApollo();

const today = new Date();
const user_payload = useCookie("user_payload", {
	expires: new Date(today.getTime() + 7 * 24 * 60 * 60 * 1000 - 2 * 60 * 1000),
	sameSite: true,
});
const refresh_token = useCookie<IRefreshToken>("user_refresh_token", {
	expires: new Date(today.getTime() + 7 * 24 * 60 * 60 * 1000 - 2 * 60 * 1000),
	sameSite: true,
});

const submitDetails = (): void => {
	postAuthDetails(form_details.value);
	onDone((data) => {
		if (!submitError.value) {
			authStore.updateUserPayload(data.data.tokenAuth.payload);
			user_payload.value = data.data.tokenAuth.payload;
			refresh_token.value = {
				refreshExpiresIn: data.data.tokenAuth.refreshExpiresIn,
				refreshToken: data.data.tokenAuth.refreshToken,
			};
			onLogin(data.data.tokenAuth.token);
			router.go(-1);
		}
	});
};
</script>
<template>
	<div class="w-full flex flex-col bg-white dark:bg-alt-dark relative">
		<Transition name="show-error">
			<div v-if="submitError" class="absolute top-0 -translate-y-1/2 left-1/2 lg:left-0 -translate-x-1/2 lg:translate-x-1/2">
				<div
					id="toast-danger"
					class="flex items-center w-full max-w-xs py-3 px-4 text-white bg-[tomato] rounded-lg shadow dark:text-white dark:bg-[tomato]"
					role="alert"
				>
					<div
						class="inline-flex items-center justify-center flex-shrink-0 w-7 h-7 text-white bg-red-300 rounded-lg dark:bg-red-300 dark:text-white"
					>
						<Icon name="mdi:close" class="text-lg" />
						<span class="sr-only">Error icon</span>
					</div>
					<div class="ml-3 text-sm font-normal">{{ submitError.message }}.</div>
				</div>
			</div>
		</Transition>
		<div
			class="w-full flex flex-col lg:grid grid-cols-2 gap-8 px-4 md:px-8 lg:px-8 py-6 ring-1 ring-neutral-200 rounded dark:ring-neutral-700"
		>
			<div class="flex flex-col gap-y-4 w-full justify-center items-center">
				<div class="w-[90%] flex flex-col gap-y-6">
					<div class="flex flex-col w-full">
						<h1 class="mb-2 text-2xl lg:text-3xl text-neutral-600 font-[600] dark:text-c-base">Welcome back</h1>
						<h2 class="text-sm sm:text-base font-medium text-neutral-600 dark:text-[#bbb]">Sign in to your account</h2>
					</div>
					<div class="flex flex-col gap-y-6 w-full mt-2 sm:mt-4">
						<div class="flex flex-col gap-y-1 w-full">
							<label for="email" class="text-sm sm:text-base dark:text-c-base">Email</label>
							<input v-model="form_details.email" type="email" name="email" id="email" placeholder="Enter your email" />
						</div>
						<div class="flex flex-col gap-y-1 w-full">
							<div class="flex flex-row justify-between items-center">
								<label for="password" class="text-sm sm:text-base dark:text-c-base">Password</label>

								<span role="button" class="text-sm sm:text-base capitalize text-neutral-600 dark:text-[#bbb]"
									>forgot password</span
								>
							</div>
							<input
								v-model="form_details.password"
								type="password"
								name="password"
								id="password"
								placeholder="Enter your password"
							/>
						</div>
					</div>
					<div class="flex flex-col mt-2">
						<button
							@click="submitDetails"
							class="bg-custom hover:bg-orange-400 py-2.5 text-lg text-gray-50 font-[600] rounded transition-colors duration-200"
						>
							<Transition mode="out-in">
								<span v-if="!loading">Login</span>
								<UtilsSpinner v-else :size="'w-6 h-6'" />
							</Transition>
						</button>
					</div>
					<div class="w-full flex flex-col items-start gap-y-6 mt-4">
						<div class="relative w-full">
							<div class="absolute inset-0 flex items-center">
								<div class="w-full border-t border-neutral-300 dark:border-[#3e3e3e]"></div>
							</div>
							<div class="relative flex justify-center text-sm">
								<span class="px-2 text-sm bg-white dark:bg-alt-dark text-neutral-600 dark:text-[#ededed]">or</span>
							</div>
						</div>
						<div class="w-full flex flex-col">
							<button
								type="button"
								class="text-neutral-700 bg-gray-200 hover:bg-gray-300 font-medium rounded border border-neutral-300 text-sm px-5 py-2 text-center flex items-center justify-center flex-row gap-x-2 focus:bg-gray-300 transition duration-200 dark:bg-[#1c1c1c] dark:border-neutral-600 dark:focus:border-neutral-500"
							>
								<NuxtImg src="/icons/google.svg" />
								<span>Continue with Google</span>
							</button>
						</div>
					</div>
					<div class="mt-4 flex flex-row items-center justify-center gap-x-2">
						<small class="text-sm sm:text-base text-neutral-500 dark:text-c-base">Don't have an account?</small>
						<NuxtLink to="/auth/register" class="text-neutral-900 text-sm sm:text-base underline">Signup Up Now</NuxtLink>
					</div>
				</div>
			</div>
			<div class="hidden md:flex justify-center items-center">
				<NuxtImg src="/auth.webp" class="w-full rounded" />
			</div>
		</div>
	</div>
</template>

<style scoped>
input {
	@apply py-2.5 px-3 bg-white dark:bg-c-dark border border-neutral-300 rounded text-sm sm:text-base hover:border-neutral-300 focus:outline-none focus:border-transparent focus:ring-1 ring-custom transition duration-200 dark:bg-inherit dark:border-neutral-600 dark:focus:border-custom dark:text-c-mode;
}
.show-error-enter-from,
.show-error-leave-to {
	@apply scale-50 opacity-0;
}
.show-error-enter-active,
.show-error-leave-active {
	transition: transform 250ms ease, opacity 250ms ease;
}
</style>
