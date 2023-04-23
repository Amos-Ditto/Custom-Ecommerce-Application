<template>
	<section class="w-full flex flex-col gap-y-2">
		<div class="promo-banner w-full flex flex-col">
			<NuxtImg src="/ad-shops.webp" class="w-full h-[3.8rem] sm:h-auto object-cover" />
		</div>
		<div class="w-full px-4 md:px-8 lg:px-20 2xl:px-44 py-2 flex flex-col">
			<div class="w-full grid grid-cols-1 gap-y-6 sm:grid-cols-3 lg:grid-cols-2 sm:items-center">
				<div class="">
					<h3 class="text-lg sm:text-xl font-semibold uppercase dark:text-neutral-50">All Shops</h3>
				</div>
				<div
					class="col-span- sm:col-span-2 lg:col-span-1 flex flex-row items-center justify-between sm:justify-end gap-x-3 sm:gap-x-6"
				>
					<div class="relative w-full lg:w-[45%]">
						<button
							class="w-full flex flex-row items-center justify-between gap-x-1 px-3 sm:px-4 py-2 sm:py-2.5 border border-neutral-200 rounded text-base focus:border-custom transition-colors duration-200 dark:border-neutral-600 dark:focus:border-custom"
						>
							<span class="text-sm sm:text-base text-neutral-500 dark:text-neutral-100">Sort by category </span>
							<Icon name="mdi:chevron-down" class="text-xl text-neutral-600 dark:text-neutral-200" />
						</button>
					</div>
					<div class="relative w-full lg:w-[45%]">
						<button
							class="w-full flex flex-row items-center justify-between gap-x-1 px-3 sm:px-4 py-2 sm:py-2.5 border border-neutral-200 rounded text-base focus:border-custom transition-colors duration-200 dark:border-neutral-600 dark:focus:border-custom"
						>
							<span class="text-sm sm:text-base text-neutral-500 dark:text-neutral-100">Sort by brand </span>
							<Icon name="mdi:chevron-down" class="text-xl text-neutral-600 dark:text-neutral-200" />
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
		</div>
	</section>
</template>
