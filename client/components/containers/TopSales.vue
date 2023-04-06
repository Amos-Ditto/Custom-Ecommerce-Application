<template>
	<div class="w-full flex flex-col gap-y-2 mt-2 sm:mt-4 mb-2 sm:mb-0 px-3 sm:px-0">
		<div class="w-full flex flex-row items-center justify-between py-1.5 sm:py-2.5 border-neutral-200 dark:border-neutral-700">
			<h3
				class="text-sm sm:text-xl sm:font-semibold relative after:content-[''] after:w-[106%] after:h-[2px] after:bg-custom after:absolute after:left-0 after:-bottom-1.5 dark:text-c-base"
			>
				Featured Deals
			</h3>
			<div class="flex flex-row items-center mr-4 dark:text-c-mode">
				<button class="text-xs sm:text-sm font-medium flex flex-row items-center gap-x-2">
					<span>See all</span>
					<Icon name="mdi:arrow-right" />
				</button>
			</div>
		</div>
		<div class="w-full flex flex-row gap-x-4 overflow-x-auto py-1 px-0.5">
			<div class="w-[12rem] sm:w-[15rem] shrink-0">
				<ListItemCard />
			</div>
			<div class="w-[12rem] sm:w-[15rem] shrink-0">
				<ListItemCard />
			</div>
			<div class="w-[12rem] sm:w-[15rem] shrink-0">
				<ListItemCard />
			</div>
			<div class="w-[12rem] sm:w-[15rem] shrink-0">
				<ListItemCard />
			</div>
			<div class="w-[12rem] sm:w-[15rem] shrink-0">
				<ListItemCard />
			</div>
		</div>
	</div>
</template>

<style scoped>
::-webkit-scrollbar {
	width: 0px;
	height: 0px;
}
</style>
