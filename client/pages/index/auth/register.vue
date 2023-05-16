<script setup lang="ts">
import { RegisterUser } from "~~/graphql/schema";
import { useAuthStore } from "~~/stores/authStore";

interface IUserDetails {
	email: String;
	fullName: String;
	password1: String;
	password2: String;
}

const user_details = ref<IUserDetails>({
	email: "",
	fullName: "",
	password1: "",
	password2: "",
});
interface IValidation {
	email: boolean;
	name: boolean;
	password: boolean;
}
const validation_errors = ref<IValidation>({
	email: false,
	name: false,
	password: false,
});

const { mutate: postUserDetials, loading, error, onDone } = useMutation(RegisterUser);
const router = useRouter();
const { $validEmail } = useNuxtApp();
const authStore = useAuthStore();

interface IError {
	field: String;
	messages: [String];
}
const errors = ref<IError[]>([]);

function resetValidationErrors() {
	validation_errors.value = {
		email: false,
		name: false,
		password: false,
	};
}
const submitDetails = (): void => {
	errors.value = [];
	resetValidationErrors();
	if (!$validEmail(user_details.value.email as string)) {
		validation_errors.value.email = true;
		return;
	}
	if (user_details.value.password1 != user_details.value.password2) {
		validation_errors.value.password = true;
		return;
	}
	postUserDetials(user_details.value);
	onDone((data) => {
		if (data.data.registerUser?.errors.length === 0) {
			authStore.updateFromRegistration();
			router.push({ name: "Login" });
		}
		errors.value = data.data.registerUser.errors as unknown as IError[];
	});
};
</script>
<template>
	<div class="w-full flex flex-col bg-white dark:bg-alt-dark relative">
		<Transition name="show-error">
			<div v-if="errors.length != 0" class="absolute top-0 -translate-y-1/2 left-1/2 lg:left-0 -translate-x-1/2 lg:translate-x-1/2">
				<div
					id="toast-danger"
					class="flex flex-col gap-y-1 w-full max-w-xs py-3 px-4 text-white bg-[tomato] rounded-lg shadow dark:text-white dark:bg-[tomato]"
					role="alert"
				>
					<div v-for="error in errors" class="flex flex-row w-full">
						<div
							class="inline-flex items-center justify-center flex-shrink-0 w-7 h-7 text-white bg-red-300 rounded-lg dark:bg-red-300 dark:text-white"
						>
							<Icon name="mdi:close" class="text-lg" />
							<span class="sr-only">Error icon</span>
						</div>
						<div class="ml-3 text-sm font-normal">{{ error?.messages[0] }}</div>
					</div>
				</div>
			</div>
		</Transition>
		<div
			class="w-full flex flex-col lg:grid grid-cols-2 gap-8 px-4 md:px-8 lg:px-8 py-6 ring-1 ring-neutral-200 rounded dark:ring-neutral-700"
		>
			<div class="flex flex-col gap-y-4 w-full justify-center items-center">
				<div class="w-[90%] flex flex-col gap-y-6">
					<div class="flex flex-col w-full">
						<h1 class="mb-2 text-2xl lg:text-3xl text-neutral-600 font-[600] dark:text-c-base">Get started</h1>
						<h2 class="text-sm sm:text-base font-medium text-neutral-600 dark:text-[#bbb]">Create a new account</h2>
						{{ error }}
					</div>
					<div class="flex flex-col gap-y-6 w-full mt-2 sm:mt-4">
						<div class="flex flex-col gap-y-1 w-full">
							<label for="email" class="text-sm sm:text-base dark:text-c-base">Email</label>
							<input type="email" name="email" id="email" placeholder="Enter your email" v-model="user_details.email" />
							<small v-if="validation_errors.email" class="text-sm text-[tomato] dark:text-[tomato]"
								>Please enter valid email</small
							>
						</div>
						<div class="flex flex-col gap-y-1 w-full">
							<label for="fullname" class="text-sm sm:text-base dark:text-c-base">Name</label>
							<input
								type="text"
								name="fullname"
								id="fullname"
								placeholder="Enter your Name"
								v-model="user_details.fullName"
							/>
							<small v-if="validation_errors.name" class="text-sm text-[tomato] dark:text-[tomato]"
								>Please enter valid Name</small
							>
						</div>
						<div class="flex flex-col gap-y-1 w-full">
							<label for="password" class="text-sm sm:text-base dark:text-c-base">Password</label>
							<input
								type="password"
								name="password"
								id="password"
								placeholder="Enter your password"
								v-model="user_details.password1"
							/>
						</div>
						<div class="flex flex-col gap-y-1 w-full">
							<label for="c_password" class="text-sm sm:text-base dark:text-c-base">Confirm Password</label>
							<input
								type="password"
								name="c_password"
								id="c_password"
								placeholder="Enter your password"
								v-model="user_details.password2"
							/>
							<small v-if="validation_errors.password" class="text-sm text-[tomato] dark:text-[tomato]"
								>Passwords doesn't match</small
							>
						</div>
					</div>
					<div class="flex flex-col mt-2">
						<button
							@click="submitDetails"
							class="bg-custom hover:bg-orange-400 py-2.5 text-lg text-gray-50 font-[600] rounded transition-colors duration-200"
						>
							<Transition mode="out-in">
								<span v-if="!loading">Sign Up</span>
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
						<small class="text-sm sm:text-base font-medium text-neutral-500 dark:text-c-base"
							>Have an account?
							<NuxtLink to="/auth" class="text-neutral-900 text-sm sm:text-base font-medium underline"
								>Signup In Now</NuxtLink
							></small
						>
					</div>
					<div
						class="mt-4 w-full flex flex-row items-center justify-center gap-x-1 text-center dark:text-c-base text-neutral-600"
					>
						<span class="text-sm sm:text-base font-medium"
							>By signing up you agree to our
							<small class="text-sm sm:text-base font-medium underline cursor-pointer">Terms of Service</small></span
						>
					</div>
				</div>
			</div>
			<div class="hidden md:flex justify-center items-center">
				<NuxtImg src="/register.webp" class="w-full" />
			</div>
		</div>
	</div>
</template>
<style scoped>
input {
	@apply py-2.5 px-3 bg-white dark:bg-c-dark border border-neutral-300 rounded text-sm sm:text-base hover:border-neutral-300 focus:outline-none focus:border-transparent focus:ring-1 focus:ring-custom transition duration-200 dark:bg-inherit dark:border-neutral-600 dark:focus:border-custom dark:text-c-mode;
}
</style>
