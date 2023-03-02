<script setup lang="ts">
definePageMeta({
	layout: false,
});
</script>
<template>
	<div class="w-full flex flex-col z-0">
		<NuxtLayout name="empty">
			<section class="w-full flex flex-col relative items-center justify-center px-8 pt-28 sm:pt-44">
				<div class="absolute left-0 top-0 right-0 h-screen -z-10">
					<NuxtImg src="/seller-auth.webp" class="w-full h-full" />
				</div>
				<div
					class="w-full sm:w-[80%] md:w-[60%] lg:w-[50%] xl:w-[40%] flex flex-col gap-y-4 rounded shadow items-center justify-center bg-c-base/70 z-0 px-4 py-4"
				>
					<div class="flex flex-col items-center py-4 w-full border-b border-gray-100">
						<NuxtImg src="/logo.png" class="w-12 h-12 rounded" />
					</div>
					<div class="flex flex-col">
						<h3 class="text-4xl uppercase text-custom font-medium">Welcome</h3>
						<p class="text-lg leading-tight">Login to your account</p>
					</div>
					<div class="flex flex-col gap-y-4 w-full mt-6 px-2">
						<div class="flex flex-col gap-y-1 w-full">
							<label for="email" class="text-base">Email</label>
							<input
								type="email"
								name="email"
								id="email"
								class="py-3 px-3 border border-neutral-200 bg-white rounded text-base hover:border-neutral-300 focus:outline-none focus:border-transparent focus:ring-1 ring-custom transition duration-200"
								placeholder="Enter your email"
							/>
						</div>
						<div class="flex flex-col gap-y-1 w-full">
							<label for="password" class="text-base">Password</label>
							<input
								type="password"
								name="password"
								id="password"
								class="py-3 px-3 border border-neutral-200 bg-white rounded text-base hover:border-neutral-300 focus:outline-none focus:border-transparent focus:ring-1 ring-custom transition duration-200"
								placeholder="Enter your password"
							/>
							<div class="w-full flex justify-between items-center py-3">
								<div class="flex items-start">
									<div class="flex items-center h-5">
										<input
											id="remember"
											type="checkbox"
											value=""
											class="w-4 h-4 border border-gray-300 rounded bg-white focus:ring-3 focus:ring-blue-300 dark:bg-gray-700 dark:border-gray-600 dark:focus:ring-blue-600 dark:ring-offset-gray-800 dark:focus:ring-offset-gray-800"
											required
										/>
									</div>
									<label for="remember" class="ml-2 text-base font-medium">Remember me</label>
								</div>
								<div class="">
									<span class="text-base hover:underline cursor-pointer">forgot password?</span>
								</div>
							</div>
						</div>
						<div class="w-full flex flex-col pb-10">
							<button
								class="bg-custom hover:bg-orange-500 px-14 py-3 text-xl text-gray-50 font-medium tracking-wide rounded transition-colors duration-200"
							>
								Login
							</button>
						</div>
					</div>
				</div>
			</section>
		</NuxtLayout>
	</div>
</template>
