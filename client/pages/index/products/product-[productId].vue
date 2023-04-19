<template>
	<section class="w-full flex flex-col py-4 px-4 md:px-8 lg:px-20 2xl:px-44">
		<div class="w-full grid grid-cols-1 xl:grid-cols-12 gap-x-6 gap-y-12">
			<div class="xl:col-span-9 flex flex-col gap-y-4">
				<div class="w-full grid grid-cols-1 md:grid-cols-10 gap-x-4 gap-y-8 pb-8">
					<div class="md:col-span-4 flex flex-col gap-y-4">
						<ul class="w-full flex overflow-x-auto">
							<li class="w-full flex flex-col border border-neutral-200 rounded">
								<NuxtImg src="/items/phone.png" class="w-full rounded" />
							</li>
						</ul>
						<ul class="w-full flex flex-row gap-x-2 overflow-x-auto items-center">
							<li class="">
								<button
									class="w-24 h-24 p-1 border border-neutral-200 focus:border-custom rounded flex flex-col items-center justify-center dark:border-neutral-700 dark:focus:border-custom"
								>
									<NuxtImg src="/items/phone.png" class="h-full rounded-sm" />
								</button>
							</li>
							<li class="">
								<button
									class="w-24 h-24 p-1 border border-neutral-200 focus:border-custom rounded flex flex-col items-center justify-center dark:border-neutral-700 dark:focus:border-custom"
								>
									<NuxtImg src="/items/keyboard.png" class="h-full rounded-sm" />
								</button>
							</li>
							<li class="">
								<button
									class="w-24 h-24 p-1 border border-neutral-200 focus:border-custom rounded flex flex-col items-center justify-center dark:border-neutral-700 dark:focus:border-custom"
								>
									<NuxtImg src="/items/tecno.jpg" class="h-full rounded-sm" />
								</button>
							</li>
						</ul>
					</div>
					<div class="md:col-span-6 flex flex-col gap-y-4">
						<div
							class="title w-full flex flex-col gap-y-2 pb-2 px-2 sm:px-0 border-b border-neutral-200 dark:border-neutral-600"
						>
							<h2 class="text-xl sm:text-2xl font-normal leading-none line-clamp-2 text-neutral-700 dark:text-neutral-200">
								ASUS ROG Phone 5 Dual Sim S888 Phantom
							</h2>
							<div class="w-full flex flex-row items-center justify-between py-1">
								<div class="">
									<ContentsRatings />
								</div>
							</div>
						</div>
						<div class="brand w-full flex flex-row gap-x-4 items-center px-2 sm:px-0">
							<div class="w-16 h-16 flex items-center justify-center border border-neutral-200 rounded">
								<NuxtImg src="/items/phone.png" class="h-full w-auto" />
							</div>
							<div class="flex flex-col text-neutral-600 dark:text-neutral-200">
								<small class="text-sm leading-none">Brand</small>
								<span class="text-base font-semibold uppercase text-neutral-800 dark:text-neutral-200">Hermes</span>
								<button class="text-sm leading-none">View other products</button>
							</div>
						</div>
						<div class="w-full flex flex-col gap-y-2.5 px-2 sm:px-0 border-b border-neutral-200 py-3.5 dark:border-neutral-600">
							<div class="flex flex-row items-center gap-x-4">
								<span class="text-2xl font-semibold dark:text-neutral-100">$351.00</span>
								<div class="flex flex-row items-center gap-x-4 mt-1">
									<span class="text-base text-neutral-500 font-medium line-through dark:text-neutral-200">$351.00</span>
									<div class="flex flex-row gap-x-2 items-center">
										<button class="px-2 py-0.5 rounded-sm bg-[tomato] text-white uppercase text-xs">off 5%</button>
									</div>
								</div>
							</div>
						</div>
						<div class="w-full flex flex-col gap-y-2 py-1 px-2 sm:px-0">
							<div class="w-full flex flex-row items-center gap-x-2">
								<Icon name="mdi:check-circle" class="text-lg text-emerald-600" />
								<span class="text-sm text-neutral-600 dark:text-neutral-100">In stock</span>
							</div>
							<div class="w-full flex flex-row items-center gap-x-2">
								<Icon name="mdi:plus" class="text-base text-neutral-600 dark:text-neutral-100" />
								<span class="text-sm text-neutral-600 dark:text-neutral-200"
									>Shipping to Anywhere from <span class="text-sm text-neutral-800 dark:text-white">Nakuru</span>
								</span>
							</div>
						</div>
						<div class="variant w-full flex flex-col gap-y-4 py-1 px-2 sm:px-0">
							<h4 class="text-base uppercase dark:text-neutral-100">Variants Available</h4>
							<div class="w-full grid grid-cols-12 gap-x-4 items-center">
								<div class="col-span-2">
									<small class="text-sm text-neutral-500 dark:text-neutral-100">Memory</small>
								</div>
								<div class="col-span-10 flex flex-row items-center gap-x-4 flex-wrap">
									<button
										class="px-3.5 py-0.5 border border-neutral-200 rounded text-sm text-neutral-700 focus:border-custom font-semibold dark:border-neutral-700 dark:text-neutral-100"
									>
										16 GB
									</button>
									<button
										class="px-3.5 py-0.5 border border-neutral-200 rounded text-sm text-neutral-700 focus:border-custom font-semibold dark:border-neutral-700 dark:text-neutral-100"
									>
										32 GB
									</button>
									<button
										class="px-3.5 py-0.5 border border-neutral-200 rounded text-sm text-neutral-700 focus:border-custom font-semibold dark:border-neutral-700 dark:text-neutral-100"
									>
										256 GB
									</button>
								</div>
							</div>
							<div class="w-full grid grid-cols-12 gap-x-4 items-center">
								<div class="col-span-2">
									<small class="text-sm text-neutral-500 dark:text-neutral-100">Color</small>
								</div>
								<div class="col-span-10 flex flex-row items-center gap-x-4 flex-wrap">
									<button
										class="px-3.5 py-0.5 border border-neutral-200 rounded text-sm text-neutral-700 focus:border-custom font-semibold dark:border-neutral-700 dark:text-neutral-100"
									>
										Black
									</button>
									<button
										class="px-3.5 py-0.5 border border-neutral-200 rounded text-sm text-neutral-700 focus:border-custom font-semibold dark:border-neutral-700 dark:text-neutral-100"
									>
										Blue
									</button>
									<button
										class="px-3.5 py-0.5 border border-neutral-200 rounded text-sm text-neutral-700 focus:border-custom font-semibold dark:border-neutral-700 dark:text-neutral-100"
									>
										Pink
									</button>
								</div>
							</div>
						</div>
						<div class="quantity w-full flex flex-col gap-y-1 py-3 border-t border-neutral-200 dark:border-neutral-600">
							<div class="">
								<small class="text-sm dark:text-neutral-100">Quantity:</small>
							</div>
							<div class="col-span-8 flex flex-row gap-x-0">
								<div class="relative w-[9rem] z-0">
									<button
										class="z-10 absolute left-0 top-0 bottom-0 px-2 py-1 text-neutral-600 border-r border-neutral-200 rounded-l hover:text-custom focus:text-custom transition duration-200 dark:border-neutral-600 dark:hover:text-custom dark:text-neutral-100"
									>
										<Icon name="mdi:minus" class="text-base" />
									</button>
									<input
										type="number"
										name="quantity"
										id="quantity"
										class="border border-neutral-200 rounded py-1 text-base text-center w-full outline-none hover:border-custom focus:border-custom transition duration-200 dark:bg-inherit dark:border-neutral-600 dark:text-neutral-100 dark:hover:border-custom dark:focus:border-custom"
										value="1"
										min="1"
									/>
									<button
										class="z-10 absolute right-0 top-0 bottom-0 px-2 py-1 text-neutral-600 border-l border-neutral-200 hover:text-custom focus:text-custom transition duration-200 dark:border-neutral-600 dark:hover:text-custom dark:text-neutral-100"
									>
										<Icon name="mdi:plus" class="text-base" />
									</button>
								</div>
							</div>
						</div>
						<div class="w-full flex flex-row gap-x-4 mt-1">
							<button
								class="text-sm sm:text-base text-custom border border-custom rounded px-6 py-2.5 font-medium transition duration-200"
							>
								Add to Cart
							</button>
							<button
								class="text-sm sm:text-base text-white bg-custom rounded px-6 py-2.5 font-medium hover:bg-custom/90 transition duration-200"
							>
								Buy now
							</button>
							<!-- Add to wishlist -->
							<button
								class="px-6 py-2.5 flex items-center justify-center border border-neutral-300 rounded text-neutral-600 hover:text-custom hover:border-custom focus:text-custom focus:border-custom transition-colors duration-200 dark:border-neutral-500 dark:hover:border-custom dark:focus:border-custom dark:text-neutral-100 dark:hover:text-custom dark:focus:text-custom"
							>
								<Icon name="mdi:heart-outline" class="text-lg sm:text-xl" />
							</button>
						</div>
						<!--  -->
					</div>
				</div>
				<div class="w-full flex flex-col gap-y-4 mt-4">
					<ContainersProductDetails />
				</div>
				<div class="mt-10 flex flex-col gap-y-4 w-full">
					<h2 class="text-lg font-medium uppercase dark:text-neutral-100">More Items to Explore</h2>
					<div class="w-full grid grid-cols-2 sm:grid-cols-3 md:grid-cols-4 gap-4">
						<ListItemCard />
						<ListItemCard />
						<ListItemCard />
						<ListItemCard />
					</div>
				</div>
			</div>
			<div class="xl:col-span-3 !sticky">
				<ContentsAsideProduct />
			</div>
		</div>
	</section>
</template>

<style scoped>
::-webkit-scrollbar:horizontal {
	height: 0px;
}

input[type="number"]::-webkit-inner-spin-button,
input[type="number"]::-webkit-outer-spin-button {
	-webkit-appearance: none;
	margin: 0;
}
</style>
