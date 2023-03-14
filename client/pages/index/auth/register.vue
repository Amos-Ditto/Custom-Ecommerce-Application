<template>
	<div class="w-full flex flex-col bg-white dark:bg-alt-dark">
		<div
			class="w-full flex flex-col-reverse lg:grid grid-cols-2 gap-8 px-4 md:px-8 lg:px-4 py-4 ring-1 ring-neutral-200 rounded dark:ring-neutral-700"
		>
			<div class="flex justify-center items-start">
				<NuxtImg src="/register.webp" class="w-full" />
			</div>
			<div class="flex flex-col gap-y-4">
				<div class="flex flex-col w-full">
					<h3 class="text-3xl uppercase text-neutral-500 font-medium dark:text-c-base">
						Welcome to
						<span class="text-custom font-extrabold">The Shop</span>
					</h3>
				</div>
				<div class="flex flex-col gap-y-2 sm:gap-y-4 w-full sm:w-[90%] mt-2">
					<div class="flex flex-col gap-y-1 w-full">
						<label for="f_name" class="text-base font-medium dark:text-c-base">Full Name</label>
						<input type="text" name="f_name" id="f_name" placeholder="Full Name" />
					</div>
					<div class="flex flex-col gap-y-1 w-full">
						<label for="phone" class="text-base font-medium dark:text-c-base">Phone Number</label>
						<input type="text" name="phone" id="phone" placeholder="phone number" />
					</div>
					<div class="flex flex-col gap-y-1 w-full">
						<label for="email" class="text-base font-medium dark:text-c-base">Email</label>
						<input type="email" name="email" id="email" placeholder="Enter your email" />
					</div>
					<div class="flex flex-col gap-y-1 w-full">
						<label for="password" class="text-base font-medium dark:text-c-base">Password</label>
						<input type="password" name="password" id="password" placeholder="Enter your password" />
					</div>
					<div class="flex flex-col gap-y-1 w-full">
						<label for="c_password" class="text-base font-medium dark:text-c-base">Confirm Password</label>
						<input type="password" name="c_password" id="c_password" placeholder="Enter your password" />
					</div>
				</div>
				<div class="w-full flex flex-col sm:flex-row gap-x-1 sm:items-center">
					<span class="text-base font-medium dark:text-c-base">By signing up you agree to our</span>
					<small class="text-base font-medium text-custom underline cursor-pointer">terms and conditions</small>
				</div>
				<div class="w-full flex flex-col sm:flex-row sm:items-center">
					<button
						class="bg-custom hover:bg-orange-500 px-10 py-3 text-xl text-gray-50 font-medium tracking-wide rounded transition-colors duration-200"
					>
						Create Account
					</button>
				</div>
				<div class="w-full flex flex-col items-start gap-y-4">
					<div class="w-[90%] flex justify-between flex-row items-center gap-x-2">
						<small class="text-sm text-neutral-500 font-medium dark:text-c-base">Or</small>
						<span class="w-[92%] h-[1px] bg-neutral-200 dark:bg-neutral-600"></span>
					</div>
					<button
						type="button"
						class="w-full sm:w-auto text-neutral-700 bg-gray-200 hover:bg-gray-300 font-medium rounded-lg text-sm px-5 py-2.5 text-center inline-flex items-center flex-row gap-x-2 focus:bg-gray-300 transition duration-200"
					>
						<NuxtImg src="/icons/google.svg" />
						Sign in with Google
					</button>
				</div>
				<div class="w-full mt-2 flex flex-row gap-x-2">
					<small class="text-base font-medium dark:text-c-base">Already have an account,</small>
					<NuxtLink to="/auth" class="text-[steelblue] text-base hover:underline">Login</NuxtLink>
				</div>
			</div>
		</div>
	</div>
</template>
<style scoped>
input {
	@apply py-2.5 px-3 border border-neutral-200 rounded text-base hover:border-neutral-300 focus:outline-none focus:border-transparent focus:ring-1 ring-custom transition duration-200 dark:bg-inherit dark:border-neutral-600 dark:focus:border-custom dark:text-c-mode;
}
</style>
