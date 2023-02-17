<template>
	<section class="w-full flex flex-col gap-y-2 px-4 md:px-8 lg:px-20 2xl:px-44">
		<div class="w-full grid grid-cols-12 gap-x-6">
			<div class="col-span-3 hidden lg:flex flex-col border-r border-neutral-200">
				<NavsAsideProducts />
			</div>
			<div class="col-span-12 lg:col-span-9 flex flex-col py-4">
				<div class="w-full flex flex-row justify-between">
					<div class="flex flex-col gap-y-0.5">
						<h3 class="text-xl font-semibold">All products</h3>
						<div class="flex flex-row items-center">
							<small class="text-neutral-500 text-sm">Total 300 products</small>
						</div>
					</div>
					<div class="flex flex-row items-center">
						<div class="relative">
							<button
								class="flex flex-row items-center gap-x-1 px-4 py-3.5 border border-neutral-200 rounded text-sm focus:border-custom transition-colors duration-200"
							>
								<span class="text-neutral-500">Sort by :</span>
								<span class="tracking-wide font-medium">Most popular</span>
								<div class="w-5 h-5 ml-2 text-neutral-500">
									<IconsChevronRight class="rotate-90" />
								</div>
							</button>
						</div>
					</div>
				</div>
				<div class="w-full grid grid-cols-3 md:grid-cols-4 gap-x-6 gap-y-8 py-8">
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
