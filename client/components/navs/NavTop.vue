<template>
	<nav class="w-full flex flex-col z-20 sticky top-0">
		<ContentsTopNav />
		<div class="w-full flex flex-col px-4 md:px-8 lg:px-20 2xl:px-44 pt-2 md:pt-3 backdrop-blur-[100px] bg-c-base/80 dark:bg-c-dark/90">
			<div class="w-full flex flex-row justify-between">
				<NuxtLink to="/" class="flex flex-row items-center">
					<NuxtImg src="/logo.png" class="mr-3 max-h-[2.2rem] sm:max-h-[2.6rem] rounded-lg shadow opacity-90" />
					<small class="text-xl sm:text-2xl tracking-wide font-bold dark:text-c-mode"
						><span class="text-custom">S</span>hop</small
					>
				</NuxtLink>
				<!-- Search input -->
				<div class="hidden md:block w-[50%] lg:w-[40%]">
					<label for="search" class="text-sm font-medium text-gray-900 sr-only dark:text-white">Search</label>
					<div class="relative flex flex-row items-center">
						<div class="absolute inset-y-0 left-0 flex items-center pl-3 pointer-events-none">
							<svg
								aria-hidden="true"
								class="w-5 h-5 text-gray-500 dark:text-gray-400"
								fill="none"
								stroke="currentColor"
								viewBox="0 0 24 24"
								xmlns="http://www.w3.org/2000/svg"
							>
								<path
									stroke-linecap="round"
									stroke-linejoin="round"
									stroke-width="2"
									d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z"
								></path>
							</svg>
						</div>
						<input
							type="search"
							id="search"
							class="block w-full py-2 lg:py-3 pl-10 pr-24 text-base text-gray-800 border border-gray-300 rounded-lg bg-gray-50 focus:outline-none dark:bg-inherit dark:border-neutral-600 dark:text-c-base"
							placeholder="Search products, brands and categories"
							required
						/>
						<button
							type="submit"
							class="text-white absolute right-1.5 bg-custom hover:bg-opacity-90 focus:bg-opacity-90 focus:outline-none font-medium rounded-md text-base px-4 py-1.5 lg:py-2.5"
						>
							Search
						</button>
					</div>
				</div>

				<!-- Toggle auth btns -->
				<div class="flex flex-row items-center gap-x-2 text-neutral-500 dark:text-neutral-400">
					<div class="w-6 lg:w-7 h-6 lg:h-7">
						<IconsUser />
					</div>
					<div class="flex flex-row items-center gap-x-1 lg:gap-x-2">
						<NuxtLink
							to="/auth"
							class="text-base lg:text-lg font-semibold text-neutral-600 px-3 py-0.5 hover:bg-gray-100 rounded-sm dark:text-neutral-400 dark:hover:bg-inherit dark:hover:text-neutral-300 transition-colors duration-200"
						>
							Login
						</NuxtLink>
						<span class="text-sm font-normal">or</span>
						<NuxtLink
							to="/auth/register"
							class="text-base lg:text-lg font-semibold text-neutral-600 px-3 py-0.5 hover:bg-gray-100 rounded-sm dark:text-neutral-400 dark:hover:bg-inherit dark:hover:text-neutral-300 transition-colors duration-200"
						>
							Register
						</NuxtLink>
					</div>
				</div>
			</div>
			<div class="w-full mt-3 sm:mt-4 border-b border-neutral-200 dark:border-neutral-600">
				<div id="nav-links" class="w-full hidden md:flex flex-row items-center justify-center gap-x-4 lg:gap-x-6">
					<NuxtLink :to="{ name: 'Home' }">
						<span> Home </span>
					</NuxtLink>
					<NuxtLink :to="{ name: 'Products' }">
						<span> All Products </span>
					</NuxtLink>
					<NuxtLink to="/shops">
						<span> Shops </span>
					</NuxtLink>
					<button>
						<span> Offers </span>
					</button>
					<button>
						<span> Men Clothing & Fashion </span>
					</button>
					<button>
						<span> Computer & Accessories </span>
					</button>
				</div>
			</div>
		</div>
	</nav>
</template>

<style scoped>
#nav-links button,
#nav-links a {
	@apply font-semibold text-neutral-700 px-2 py-2.5 hover:text-custom dark:text-neutral-200 transition-colors duration-300;
}

#nav-links a.router-link-active {
	@apply text-custom;
}

#nav-links a.router-link-active {
	background-image: linear-gradient(#dd9933, #dd9933);
	background-position: 0% 100%;
	background-repeat: no-repeat;
	background-size: 100% 2px;
	transition: background-size 0.2s, padding 0.2s;
}
#nav-links button span,
#nav-links a span {
	@apply text-sm lg:text-base;
}
#nav-links button,
#nav-links a {
	@apply pr-3 cursor-pointer;
	background-image: linear-gradient(#dd9933, #dd9933);
	background-position: 0% 100%;
	background-repeat: no-repeat;
	background-size: 0% 2px;
	transition: background-size 0.2s, padding 0.2s;
}
#nav-links button:hover,
#nav-links a:hover {
	background-size: 100% 2px;
}
</style>
