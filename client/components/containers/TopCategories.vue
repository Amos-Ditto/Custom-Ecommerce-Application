<template>
	<div class="w-full flex flex-col gap-y-3 mt-2 mb-2 sm:mb-0 sm:mt-4 px-3 sm:px-2 md:px-0">
		<div
			class="w-full flex flex-col lg:flex-row items-start sm:items-center justify-between gap-y-4 py-1.5 sm:py-2.5 border-neutral-200 dark:border-neutral-700"
		>
			<h3
				class="text-sm sm:text-xl sm:font-semibold relative after:content-[''] sm:after:w-[106%] after:h-[2px] after:bg-custom after:absolute lg:after:left-0 after:left-[-3%] after:-bottom-1.5 dark:text-c-base"
			>
				Popular Categories
			</h3>
			<div id="categories" class="flex flex-row justify-center gap-x-2.5 sm:gap-x-4 items-center w-full lg:w-auto mt-2.5 md:mt-0">
				<button>Mens Clothing & Fashion</button>
				<button>Computer & Accessories</button>
				<button>Speakers & Electronics</button>
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
#categories button {
	@apply px-1 tracking-normal md:px-2 py-0.5 sm:py-1 text-xs sm:text-sm md:text-base font-medium first:text-custom hover:text-custom border-b border-transparent hover:border-custom first:border-custom truncate dark:text-c-mode dark:hover:text-custom dark:first:text-custom transition duration-200;
}
</style>
<style scoped>
::-webkit-scrollbar {
	width: 0px;
	height: 0px;
}
</style>
