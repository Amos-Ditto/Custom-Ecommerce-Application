<template>
	<section class="w-full flex flex-col gap-y-4 mt-6">
		<h3 class="text-xl sm:text-2xl font-semibold text-neutral-700 dark:text-c-mode">Profile</h3>
		<div class="w-full flex flex-col gap-y-4 mt-3">
			<h4 class="text-lg sm:text-xl font-semibold dark:text-c-mode">Profile Information</h4>

			<div class="w-full flex flex-col">
				<form>
					<div class="grid gap-4 sm:gap-6 mb-6 md:grid-cols-2">
						<div>
							<label for="first_name" class="block mb-2 text-sm font-medium text-gray-900 dark:text-white">First name</label>
							<input
								type="text"
								id="first_name"
								class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-custom focus:border-custom block w-full p-2.5 dark:bg-inherit dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-custom dark:focus:border-custom"
								placeholder="John"
								required
							/>
						</div>
						<div>
							<label for="last_name" class="block mb-2 text-sm font-medium text-gray-900 dark:text-white">Last name</label>
							<input
								type="text"
								id="last_name"
								class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-custom focus:border-custom block w-full p-2.5 dark:bg-inherit dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-custom dark:focus:border-custom"
								placeholder="Doe"
								required
							/>
						</div>
						<div>
							<label for="email" class="block mb-2 text-sm font-medium text-gray-900 dark:text-white">Email address</label>
							<input
								type="email"
								id="email"
								class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-custom focus:border-custom block w-full p-2.5 dark:bg-inherit dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-custom dark:focus:border-custom"
								placeholder="john.doe@company.com"
								required
							/>
						</div>
						<div>
							<label for="phone" class="block mb-2 text-sm font-medium text-gray-900 dark:text-white">Phone number</label>
							<input
								type="tel"
								id="phone"
								class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-custom focus:border-custom block w-full p-2.5 dark:bg-inherit dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-custom dark:focus:border-custom"
								placeholder="123-45-678"
								pattern="[0-9]{3}-[0-9]{2}-[0-9]{3}"
								required
							/>
						</div>
						<div class="">
							<label for="password" class="block mb-2 text-sm font-medium text-gray-900 dark:text-white">Password</label>
							<input
								type="password"
								id="password"
								class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-custom focus:border-custom block w-full p-2.5 dark:bg-inherit dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-custom dark:focus:border-custom"
								placeholder="•••••••••"
								required
							/>
						</div>
						<div class="">
							<label for="confirm_password" class="block mb-2 text-sm font-medium text-gray-900 dark:text-white"
								>Confirm password</label
							>
							<input
								type="password"
								id="confirm_password"
								class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-custom focus:border-custom block w-full p-2.5 dark:bg-inherit dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-custom dark:focus:border-custom"
								placeholder="•••••••••"
								required
							/>
						</div>
					</div>
					<div class="w-full flex flex-col mb-4 sm:mb-6">
						<label class="block mb-2 text-sm font-medium text-gray-900 dark:text-white">Profile Image</label>

						<div
							class="w-full flex flex-col gap-y-2 items-center justify-center py-6 border border-gray-300 rounded-lg bg-inherit dark:border-neutral-700"
						>
							<NuxtImg src="/icons/male.png" class="w-44 h-44 rounded-full ring-2 ring-gray-50 dark:ring-neutral-700" />
							<button
								type="button"
								class="text-base mt-1 text-neutral-500 font-semibold px-4 py-1.5 border border-neutral-200 rounded bg-gray-100 hover:opacity-90 dark:bg-neutral-700 dark:border-neutral-600 dark:text-c-mode/75 dark:hover:opacity-80"
							>
								Select Image
							</button>
						</div>
					</div>
					<button
						type="submit"
						class="text-white bg-custom hover:bg-custom/90 focus:ring-2 outline-none focus:ring-custom/60 font-medium rounded text-base tracking-wide px-8 py-2.5 text-center"
					>
						Update
					</button>
				</form>
			</div>
		</div>

		<div class="w-full flex flex-col gap-y-4 mt-12">
			<div class="w-full flex flex-row justify-between items-center">
				<h4 class="text-lg sm:text-xl font-semibold dark:text-c-mode">Addresses</h4>
				<button
					type="button"
					class="text-white bg-custom hover:bg-custom/90 focus:ring-2 outline-none focus:ring-custom/60 font-medium rounded text-base tracking-wide px-6 py-2.5 text-center"
				>
					Add New
				</button>
			</div>
			<div class="w-full grid grid-cols-1 sm:grid-cols-2 gap-6 mt-2 sm:mt-0">
				<div class="flex flex-col gap-y-3">
					<h4 class="text-base font-semibold text-neutral-600 dark:text-c-mode/80">Default Shipping Address</h4>
					<div
						class="flex flex-col gap-y-0.5 border border-neutral-200 rounded px-4 py-5 text-sm relative dark:border-neutral-700 dark:text-c-mode"
					>
						<p class="">4471 Nutters Barn Lane Des Moines, IA 50309</p>
						<p class="">5252, Nakuru, Rift Valley</p>
						<p class="">Kenya</p>
						<p class="">0794818111</p>

						<div class="absolute top-1 right-1">
							<button
								class="w-9 sm:w-10 h-9 sm:h-10 rounded-full bg-gray-100 rotate-90 p-1.5 hover:bg-custom/20 transition-colors text-neutral-600 dark:bg-neutral-800 dark:text-c-mode/90"
							>
								<IconsDots />
							</button>
						</div>
					</div>
				</div>
			</div>
		</div>
	</section>
</template>

<style scoped>
form input {
	outline: none;
}
</style>
