<template>
	<section class="w-full flex flex-col gap-y-2 sm:px-4 md:px-8 lg:px-20 2xl:px-44">
		<div class="ad-image w-full flex flex-row items-center">
			<NuxtImg src="/products.png" class="w-full rounded-sm" />
		</div>
		<div class="w-full grid grid-cols-12 gap-x-6 px-3 sm:px-0">
			<div class="col-span-3 hidden lg:flex flex-col border-r border-neutral-200 dark:border-neutral-700">
				<NavsAsideProducts />
			</div>
			<div class="col-span-12 lg:col-span-9 flex flex-col py-4">
				<div class="w-full flex flex-row justify-between">
					<div class="flex flex-col gap-y-0.5">
						<h3 class="text-base sm:text-xl font-semibold dark:text-c-mode">All products</h3>
						<div class="flex flex-row items-center">
							<small class="text-neutral-500 text-xs sm:text-sm dark:text-neutral-200">Total 300 products</small>
						</div>
					</div>
					<div class="flex flex-row items-center">
						<div class="relative flex flex-row items-center gap-x-2">
							<span class="text-neutral-500 dark:text-neutral-200 text-base">Sort by :</span>
							<button
								class="flex flex-row items-center gap-x-1 px-3 sm:px-4 py-2 sm:py-2.5 border border-neutral-200 dark:border-neutral-600 rounded text-sm sm:text-base focus:border-custom transition-colors duration-200 dark:focus:border-custom"
							>
								<span class="tracking-wide font-medium dark:text-c-mode">Most popular</span>
								<Icon name="mdi:chevron-down" class="text-lg dark:text-neutral-100" />
							</button>
						</div>
					</div>
				</div>
				<div class="w-full grid grid-cols-2 sm:grid-cols-3 md:grid-cols-4 gap-x-4 sm:gap-x-6 gap-y-4 sm:gap-y-8 py-8">
					<ListItemCard />
					<ListItemCard />
					<ListItemCard />
					<ListItemCard />
					<ListItemCard />
					<ListItemCard />
					<ListItemCard />
					<ListItemCard />
					<ListItemCard />
					<ListItemCard />
					<ListItemCard />
					<ListItemCard />
				</div>
			</div>
		</div>
	</section>
</template>
