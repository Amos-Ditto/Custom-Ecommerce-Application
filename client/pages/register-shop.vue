<template>
	<section class="w-full flex flex-col gap-y-4 px-4 md:px-8 lg:px-20 2xl:px-44 mt-6 mb-12">
		<div class="w-full flex flex-col">
			<NuxtImg src="/seller.webp" class="w-full h-auto" />
		</div>
		<div class="w-full flex flex-col mt-12 gap-y-4">
			<h1 class="text-3xl md:text-4xl font-semibold">Register your shop</h1>
			<div class="w-full flex-col -space-y-px">
				<div class="w-full flex flex-col gap-y-6 border pt-6 pb-4 px-6 rounded-t mt-6">
					<h3 class="text-xl md:text-2xl font-semibold text-neutral-700">Personal Information</h3>
					<div class="grid gap-y-4 sm:gap-y-6 mb-6 md:grid-cols-2 gap-x-12">
						<div>
							<label for="first_name" class="block mb-2 text-sm sm:text-base font-medium text-gray-900 dark:text-white"
								>Full name</label
							>
							<input
								type="text"
								id="full_name"
								class="bg-gray-50 border border-gray-300 text-gray-900 text-sm sm:text-base rounded-lg focus:ring-custom focus:border-custom block w-full p-2.5 dark:bg-inherit dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-custom dark:focus:border-custom"
								placeholder="John Doe"
							/>
						</div>
						<div>
							<label for="email" class="block mb-2 text-sm sm:text-base font-medium text-gray-900 dark:text-white"
								>Email address</label
							>
							<input
								type="email"
								id="email"
								class="bg-gray-50 border border-gray-300 text-gray-900 text-sm sm:text-base rounded-lg focus:ring-custom focus:border-custom block w-full p-2.5 dark:bg-inherit dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-custom dark:focus:border-custom"
								placeholder="john.doe@company.com"
							/>
						</div>
						<div>
							<label for="phone" class="block mb-2 text-sm sm:text-base font-medium text-gray-900 dark:text-white"
								>Phone number</label
							>
							<input
								type="tel"
								id="phone"
								class="bg-gray-50 border border-gray-300 text-gray-900 text-sm sm:text-base rounded-lg focus:ring-custom focus:border-custom block w-full p-2.5 dark:bg-inherit dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-custom dark:focus:border-custom"
								placeholder="123-45-678"
								pattern="[0-9]{3}-[0-9]{2}-[0-9]{3}"
							/>
						</div>
						<div class="">
							<label for="password" class="block mb-2 text-sm sm:text-base font-medium text-gray-900 dark:text-white"
								>Password</label
							>
							<input
								type="password"
								id="password"
								class="bg-gray-50 border border-gray-300 text-gray-900 text-sm sm:text-base rounded-lg focus:ring-custom focus:border-custom block w-full p-2.5 dark:bg-inherit dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-custom dark:focus:border-custom"
								placeholder="•••••••••"
							/>
						</div>
					</div>
				</div>
				<div class="w-full flex flex-col gap-y-6 border pt-6 pb-2 px-6 rounded-b mt-6">
					<h3 class="text-xl md:text-2xl font-semibold text-neutral-700">Shop Information</h3>
					<div class="grid gap-y-4 sm:gap-y-6 mb-6 md:grid-cols-2 gap-x-12">
						<div>
							<label for="shop_name" class="block mb-2 text-sm sm:text-base font-medium text-gray-900 dark:text-white"
								>Shop name</label
							>
							<input
								type="text"
								id="shop_name"
								class="bg-gray-50 border border-gray-300 text-gray-900 text-sm sm:text-base rounded-lg focus:ring-custom focus:border-custom block w-full p-2.5 dark:bg-inherit dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-custom dark:focus:border-custom"
								placeholder="Shop name"
							/>
						</div>
						<div>
							<label for="shop_phone" class="block mb-2 text-sm sm:text-base font-medium text-gray-900 dark:text-white"
								>Shop Phone</label
							>
							<input
								type="tel"
								id="shop_phone"
								class="bg-gray-50 border border-gray-300 text-gray-900 text-sm sm:text-base rounded-lg focus:ring-custom focus:border-custom block w-full p-2.5 dark:bg-inherit dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-custom dark:focus:border-custom"
								placeholder="123-45-678"
								pattern="[0-9]{3}-[0-9]{2}-[0-9]{3}"
							/>
						</div>
						<div>
							<label for="shop_address" class="block mb-2 text-sm sm:text-base font-medium text-gray-900 dark:text-white"
								>Shop Address</label
							>
							<input
								type="text"
								id="shop_address"
								class="bg-gray-50 border border-gray-300 text-gray-900 text-sm sm:text-base rounded-lg focus:ring-custom focus:border-custom block w-full p-2.5 dark:bg-inherit dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-custom dark:focus:border-custom"
								placeholder="Shop Address"
							/>
						</div>
						<div class="flex items-start mb-2 md:col-span-2">
							<span class="text-sm sm:text-base font-medium text-gray-900 dark:text-gray-300"
								>By signing up you agree to our
								<a href="#" class="text-custom hover:underline">terms and conditions</a>.</span
							>
						</div>
					</div>
				</div>
			</div>
			<div class="w-full flex flex-row mt-2">
				<button class="w-full sm:w-auto px-14 py-2.5 text-base md:text-lg font-semibold bg-custom rounded text-c-base">
					Register Shop
				</button>
			</div>
		</div>
	</section>
</template>
