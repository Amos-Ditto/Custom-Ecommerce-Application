<template>
	<div class="w-full flex flex-col gap-y-6 mt-3">
		<div class="relative w-full flex flex-row item-cards-center">
			<h3
				class="text-lg sm:text-xl font-semibold relative after:content-[''] after:w-[106%] after:h-[2px] after:bg-custom after:absolute after:left-0 after:-bottom-1.5 dark:text-c-base"
			>
				Featured Shops
			</h3>
		</div>

		<div class="grid grid-cols-1 lg:grid-cols-3 gap-x-6 gap-y-3">
			<ListShopCard class="item-card" />
			<ListShopCard class="item-card" />
			<ListShopCard class="item-card" />
		</div>
	</div>
</template>

<style scoped>
.item-card {
	@apply lg:flex first:flex hidden;
}
</style>
