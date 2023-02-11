<template>
	<div class="w-full flex flex-col">
		<div
			class="w-full flex flex-col-reverse lg:grid grid-cols-2 gap-8 px-4 md:px-8 lg:px-4 py-4 ring-1 ring-neutral-200 rounded shadow-md"
		>
			<div class="flex justify-center items-center">
				<NuxtImg src="/auth.webp" class="w-full" />
			</div>
			<div class="flex flex-col gap-y-4">
				<div class="flex flex-col w-full">
					<h3 class="text-3xl uppercase text-neutral-500 font-light">
						Login to <span class="text-custom font-extrabold">Shop</span>
					</h3>
				</div>
				<div class="flex flex-col gap-y-8 w-[90%] mt-6">
					<div class="flex flex-col gap-y-1 w-full">
						<label for="email" class="text-base">Email</label>
						<input
							type="email"
							name="email"
							id="email"
							class="py-2.5 px-3 border border-neutral-200 rounded text-base hover:border-neutral-300 focus:outline-none focus:border-transparent focus:ring-1 ring-custom transition duration-200"
							placeholder="Enter your email"
						/>
					</div>
					<div class="flex flex-col gap-y-1 w-full">
						<label for="password" class="text-base">Password</label>
						<input
							type="password"
							name="password"
							id="password"
							class="py-2.5 px-3 border border-neutral-200 rounded text-base hover:border-neutral-300 focus:outline-none focus:border-transparent focus:ring-1 ring-custom transition duration-200"
							placeholder="Enter your password"
						/>
						<div class="w-full flex justify-end items-center">
							<span class="text-sm italic text-custom hover:underline cursor-pointer">forgot password?</span>
						</div>
					</div>
				</div>
				<div class="w-full flex flex-row items-center">
					<button
						class="bg-custom hover:bg-orange-500 px-14 py-3 text-xl text-gray-50 font-medium tracking-wide rounded transition-colors duration-200"
					>
						Login
					</button>
				</div>
				<div class="w-full flex flex-col items-start gap-y-4">
					<small class="text-sm text-neutral-500 font-medium">or, Login with</small>
					<button
						type="button"
						class="text-neutral-700 bg-gray-200 hover:bg-gray-300 font-medium rounded-lg text-sm px-5 py-2.5 text-center inline-flex items-center flex-row gap-x-2 focus:bg-gray-300 transition duration-200"
					>
						<NuxtImg src="/icons/google.svg" />
						Sign in with Google
					</button>
				</div>
				<div class="w-full mt-2 flex flex-row gap-x-2">
					<small class="text-base">Don't have an account,</small>
					<NuxtLink to="/auth" class="text-custom text-base hover:underline">Signup</NuxtLink>
				</div>
			</div>
		</div>
	</div>
</template>
