<template>
	<section class="w-full flex flex-col gap-y-2">
		<div class="w-full grid grid-cols-12 gap-x-6">
			<div class="col-span-3 hidden lg:flex flex-col border-r border-neutral-200 dark:border-neutral-600">
				<NavsAsideProducts />
			</div>
			<div class="col-span-12 lg:col-span-9 flex flex-col py-4">
				<div class="w-full flex flex-row justify-between gap-y-6">
					<div class="flex flex-col gap-y-0.5">
						<h3 class="text-xl font-semibold">All products</h3>
						<div class="flex flex-row items-center">
							<small class="text-neutral-500 text-sm">Total 300 products</small>
						</div>
					</div>
					<div class="flex flex-row items-center">
						<div class="relative flex flex-row items-baseline gap-x-2 flex-nowrap">
							<span class="text-neutral-500 truncate hidden sm:block">Sort by :</span>
							<button
								class="flex flex-row items-center justify-between gap-x-1 px-4 py-2.5 border border-neutral-200 rounded text-sm focus:border-custom transition-colors duration-200 dark:border-neutral-600 dark:focus:border-custom"
							>
								<span class="tracking-wide font-medium">Most popular</span>

								<Icon name="mdi:chevron-down" class="text-lg text-neutral-500 ml-2" />
							</button>
						</div>
					</div>
				</div>
				<div class="w-full grid grid-cols-2 sm:grid-cols-3 md:grid-cols-4 gap-x-4 md:gap-x-6 gap-y-5 md:gap-y-8 py-8">
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
