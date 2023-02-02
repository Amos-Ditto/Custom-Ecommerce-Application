<template>
	<div class="w-full flex flex-col gap-y-2 mt-4">
		<div class="w-full flex flex-row items-center justify-between py-1.5 sm:py-2.5 border-b border-neutral-200 dark:border-neutral-700">
			<h3
				class="text-lg sm:text-xl md:text-2xl font-semibold relative after:content-[''] after:w-[106%] after:h-[2px] after:bg-custom after:absolute after:left-0 after:-bottom-1.5 dark:text-c-base"
			>
				Featured Deals
			</h3>
			<div class="flex flex-row items-center">
				<button
					class="text-neutral-900 flex items-center p-1 rounded-full shadow bg-white hover:text-custom hover:shadow-md transition duration-200 dark:bg-neutral-700 dark:text-c-base dark:hover:text-custom"
				>
					<div class="w-5 sm:w-4 h-5 sm:h-4 flex items-center justify-center">
						<IconsChevronRight />
					</div>
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
