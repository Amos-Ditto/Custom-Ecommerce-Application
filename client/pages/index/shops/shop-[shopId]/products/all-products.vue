<template>
	<section class="w-full flex flex-col gap-y-2">
		<div class="w-full grid grid-cols-12 gap-x-6">
			<div class="col-span-3 hidden lg:flex flex-col border-r border-neutral-200">
				<NavsShopAsideAllProducts />
			</div>
			<div class="col-span-12 lg:col-span-9 flex flex-col py-4">
				<div class="w-full flex flex-col sm:flex-row justify-between gap-y-6">
					<div class="flex flex-col gap-y-0.5">
						<h3 class="text-xl font-semibold">All products</h3>
						<div class="flex flex-row items-center">
							<small class="text-neutral-500 text-sm">Total 300 products</small>
						</div>
					</div>
					<div class="flex flex-row items-center w-full sm:w-auto">
						<div class="relative w-full sm:w-auto">
							<button
								class="w-full sm:w-auto flex flex-row items-center justify-between gap-x-1 px-4 py-3.5 border border-neutral-200 rounded text-sm focus:border-custom transition-colors duration-200"
							>
								<div class="flex flex-row items-center gap-x-1">
									<span class="text-neutral-500">Sort by :</span>
									<span class="tracking-wide font-medium">Most popular</span>
								</div>
								<div class="w-5 h-5 ml-2 text-neutral-500">
									<IconsChevronRight class="rotate-90" />
								</div>
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
