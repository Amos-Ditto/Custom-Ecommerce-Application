<template>
	<section class="w-full flex flex-col gap-y-2">
		<div class="promo-banner w-full flex flex-col">
			<NuxtImg src="/ad-shops.webp" class="w-full" />
		</div>
		<div class="w-full px-4 md:px-8 lg:px-20 2xl:px-44 py-4 flex flex-col mt-3">
			<div class="w-full grid grid-cols-1 gap-y-6 sm:grid-cols-3 lg:grid-cols-2 sm:items-center">
				<div class="">
					<h3 class="text-2xl font-semibold">All Shops</h3>
				</div>
				<div class="col-span- sm:col-span-2 lg:col-span-1 flex flex-row items-center justify-between sm:justify-end gap-x-6">
					<div class="relative w-full lg:w-[45%]">
						<button
							class="w-full flex flex-row items-center justify-between gap-x-1 px-4 py-3.5 border border-neutral-200 rounded text-base focus:border-custom transition-colors duration-200"
						>
							<span class="tracking-wide font-medium text-neutral-500">Sort by category </span>
							<div class="w-5 h-5 ml-2 text-neutral-500">
								<IconsChevronRight class="rotate-90" />
							</div>
						</button>
					</div>
					<div class="relative w-full lg:w-[45%]">
						<button
							class="w-full flex flex-row items-center justify-between gap-x-1 px-4 py-3.5 border border-neutral-200 rounded text-base focus:border-custom transition-colors duration-200"
						>
							<span class="tracking-wide font-medium text-neutral-500">Sort by brand </span>
							<div class="w-5 h-5 ml-2 text-neutral-500">
								<IconsChevronRight class="rotate-90" />
							</div>
						</button>
					</div>
				</div>
			</div>

			<div class="w-full grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 xl:grid-cols-4 gap-x-6 gap-y-8 mt-10 sm:mt-6">
				<ListShowShopCard />
				<ListShowShopCard />
				<ListShowShopCard />
				<ListShowShopCard />
				<ListShowShopCard />
				<ListShowShopCard />
				<ListShowShopCard />
				<ListShowShopCard />
			</div>
			<div class="w-full flex flex-row items-center justify-between justify-center py-4 mt-4">
				<ul class="inline-flex items-center -space-x-px">
					<li>
						<button
							class="block px-3 py-2 ml-0 leading-tight text-gray-500 bg-white border border-gray-300 rounded-l-lg hover:bg-gray-100 hover:text-gray-700 dark:bg-gray-800 dark:border-gray-700 dark:text-gray-400 dark:hover:bg-gray-700 dark:hover:text-white"
						>
							<span class="sr-only">Previous</span>
							<svg
								aria-hidden="true"
								class="w-5 h-5"
								fill="currentColor"
								viewBox="0 0 20 20"
								xmlns="http://www.w3.org/2000/svg"
							>
								<path
									fill-rule="evenodd"
									d="M12.707 5.293a1 1 0 010 1.414L9.414 10l3.293 3.293a1 1 0 01-1.414 1.414l-4-4a1 1 0 010-1.414l4-4a1 1 0 011.414 0z"
									clip-rule="evenodd"
								></path>
							</svg>
						</button>
					</li>
					<li>
						<button
							class="px-3 py-2 leading-tight text-base text-gray-500 bg-white border border-gray-300 hover:bg-gray-100 hover:text-gray-700 dark:bg-gray-800 dark:border-gray-700 dark:text-gray-400 dark:hover:bg-gray-700 dark:hover:text-white"
						>
							1
						</button>
					</li>
					<li>
						<button
							class="px-3 py-2 leading-tight text-base text-gray-500 bg-white border border-gray-300 hover:bg-gray-100 hover:text-gray-700 dark:bg-gray-800 dark:border-gray-700 dark:text-gray-400 dark:hover:bg-gray-700 dark:hover:text-white"
						>
							2
						</button>
					</li>
					<li>
						<button
							class="z-10 px-3 py-2 leading-tight text-blue-600 border border-blue-300 bg-blue-50 hover:bg-blue-100 hover:text-blue-700 dark:border-gray-700 dark:bg-gray-700 dark:text-white"
						>
							3
						</button>
					</li>
					<li>
						<button
							class="px-3 py-2 leading-tight text-base text-gray-500 bg-white border border-gray-300 hover:bg-gray-100 hover:text-gray-700 dark:bg-gray-800 dark:border-gray-700 dark:text-gray-400 dark:hover:bg-gray-700 dark:hover:text-white"
						>
							4
						</button>
					</li>
					<li>
						<button
							class="px-3 py-2 leading-tight text-base text-gray-500 bg-white border border-gray-300 hover:bg-gray-100 hover:text-gray-700 dark:bg-gray-800 dark:border-gray-700 dark:text-gray-400 dark:hover:bg-gray-700 dark:hover:text-white"
						>
							5
						</button>
					</li>
					<li>
						<button
							class="block px-3 py-2 leading-tight text-gray-500 bg-white border border-gray-300 rounded-r-lg hover:bg-gray-100 hover:text-gray-700 dark:bg-gray-800 dark:border-gray-700 dark:text-gray-400 dark:hover:bg-gray-700 dark:hover:text-white"
						>
							<span class="sr-only">Next</span>
							<svg
								aria-hidden="true"
								class="w-5 h-5"
								fill="currentColor"
								viewBox="0 0 20 20"
								xmlns="http://www.w3.org/2000/svg"
							>
								<path
									fill-rule="evenodd"
									d="M7.293 14.707a1 1 0 010-1.414L10.586 10 7.293 6.707a1 1 0 011.414-1.414l4 4a1 1 0 010 1.414l-4 4a1 1 0 01-1.414 0z"
									clip-rule="evenodd"
								></path>
							</svg>
						</button>
					</li>
				</ul>
			</div>
		</div>
	</section>
</template>
