<template>
	<section class="w-full flex flex-col gap-y-2">
		<div class="featured w-full flex flex-col gap-y-4 mt-6">
			<h3 class="text-xl font-semibold">Featured Products</h3>
			<div class="w-full flex flex-row overflow-x-auto shrink-0 gap-x-4 py-1 px-1">
				<ListItemCard class="w-[210px] md:w-[250px] shrink-0" />
				<ListItemCard class="w-[210px] md:w-[250px] shrink-0" />
				<ListItemCard class="w-[210px] md:w-[250px] shrink-0" />
				<ListItemCard class="w-[210px] md:w-[250px] shrink-0" />
				<ListItemCard class="w-[210px] md:w-[250px] shrink-0" />
				<ListItemCard class="w-[210px] md:w-[250px] shrink-0" />
				<ListItemCard class="w-[210px] md:w-[250px] shrink-0" />
				<ListItemCard class="w-[210px] md:w-[250px] shrink-0" />
			</div>
		</div>
		<div class="w-full flex flex-col mt-6 gap-y-2">
			<h3 class="text-xl font-semibold">New Arrival</h3>
			<div class="arrivals w-full flex flex-row lg:grid grid-cols-3 gap-4 overflow-x-auto">
				<ListItemHorizontal class="shrink-0 w-[360px] lg:w-auto" />
				<ListItemHorizontal class="shrink-0 w-[360px] lg:w-auto" />
				<ListItemHorizontal class="shrink-0 w-[360px] lg:w-auto" />
				<ListItemHorizontal class="shrink-0 w-[360px] lg:w-auto" />
				<ListItemHorizontal class="shrink-0 w-[360px] lg:w-auto" />
				<ListItemHorizontal class="shrink-0 w-[360px] lg:w-auto" />
			</div>
		</div>
		<div class="ad-image w-full flex flex-row items-center py-6">
			<NuxtImg src="/products.png" class="w-full rounded-sm" />
		</div>
		<div class="w-full flex flex-col mt-6 gap-y-3">
			<h3 class="text-xl font-semibold">Best Rated</h3>
			<div class="w-full flex flex-row overflow-x-auto shrink-0 gap-x-4 md:gap-x-6 py-1 px-1">
				<ListItemCard class="w-[210px] md:w-[250px] shrink-0" />
				<ListItemCard class="w-[210px] md:w-[250px] shrink-0" />
				<ListItemCard class="w-[210px] md:w-[250px] shrink-0" />
				<ListItemCard class="w-[210px] md:w-[250px] shrink-0" />
				<ListItemCard class="w-[210px] md:w-[250px] shrink-0" />
				<ListItemCard class="w-[210px] md:w-[250px] shrink-0" />
			</div>
		</div>
	</section>
</template>

<style scoped>
::-webkit-scrollbar:horizontal {
	height: 0px;
}
</style>
