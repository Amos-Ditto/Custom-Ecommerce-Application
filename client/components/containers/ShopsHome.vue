<template>
	<div class="w-full flex flex-col gap-y-6 mt-2 sm:mt-3 mb-2 sm:mb-0 px-3 sm:px-0 py-1 sm:py-0">
		<div class="relative w-full flex flex-row item-cards-center sm:px-2 md:px-02">
			<h3
				class="text-sm sm:text-xl sm:font-semibold relative after:content-[''] after:w-[106%] after:h-[2px] after:bg-custom after:absolute after:left-0 after:-bottom-1.5 dark:text-c-base"
			>
				Featured Shops
			</h3>
		</div>

		<div class="arrivals w-full flex flex-row lg:grid grid-cols-4 gap-4 overflow-x-auto sm:px-2 md:px-0 pb-2">
			<ListFeaturedShop />
			<ListFeaturedShop />
			<ListFeaturedShop />
			<ListFeaturedShop />
		</div>
	</div>
</template>

<style scoped>
::-webkit-scrollbar:horizontal {
	height: 0px;
}
</style>
