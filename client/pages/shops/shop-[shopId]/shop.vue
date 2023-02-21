<template>
	<section class="w-full flex flex-col gap-y-2">
		<div class="featured w-full flex flex-col gap-y-4 mt-6">
			<h3 class="text-2xl font-semibold">Featured Products</h3>
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
		<div class="offers w-full overflow-x-auto px-1 flex flex-row items-center gap-x-4 justify-between mt-4">
			<NuxtImg src="/slides/14.webp" class="w-auto h-[200px] shrink-0" />
			<NuxtImg src="/slides/12.webp" class="w-auto h-[200px] shrink-0" />
			<NuxtImg src="/slides/13.webp" class="w-auto h-[200px] shrink-0" />
		</div>
		<div class="w-full flex flex-col mt-6 gap-y-2">
			<h3 class="text-2xl font-semibold">New Arrival</h3>
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
			<h3 class="text-2xl font-semibold">Best Rated</h3>
			<div class="w-full flex flex-row overflow-x-auto shrink-0 gap-x-4 md:gap-x-6 py-1 px-1">
				<ListItemCard class="w-[210px] md:w-[250px] shrink-0" />
				<ListItemCard class="w-[210px] md:w-[250px] shrink-0" />
				<ListItemCard class="w-[210px] md:w-[250px] shrink-0" />
				<ListItemCard class="w-[210px] md:w-[250px] shrink-0" />
				<ListItemCard class="w-[210px] md:w-[250px] shrink-0" />
				<ListItemCard class="w-[210px] md:w-[250px] shrink-0" />
			</div>
		</div>
		<div class="w-full mt-10 border border-custom bg-[tomato]/10 flex flex-col items-center justify-center py-4 rounded">
			<button class="text-lg md:text-xl py-1 font-semibold flex flex-row items-center gap-x-3">
				<span>View all Products of This Shop</span>
				<div class="w-6 h-6">
					<IconsArrow />
				</div>
			</button>
		</div>
	</section>
</template>

<style scoped>
::-webkit-scrollbar:horizontal {
	height: 0px;
}
</style>
