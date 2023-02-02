<template>
	<div class="w-full flex flex-col gap-y-2 mt-1 sm:mt-2">
		<div class="w-full flex flex-row items-center justify-between py-1.5">
			<h3 class="text-lg sm:text-xl md:text-2xl font-semibold dark:text-c-base">Product Categories</h3>
			<div class="flex flex-row items-center gap-x-5">
				<!-- <span class="h-2 sm:h-2.5 w-12 rounded-3xl bg-custom"></span> -->
				<button
					class="text-sm md:text-base font-serif font-medium hover:text-custom capitalize flex flex-row items-center justify-center gap-x-1 transition-colors duration-200 dark:text-c-base dark:hover:text-custom"
				>
					all
					<div class="w-3 sm:w-4 h-3 sm:h-4 -translate-y-[15%] sm:translate-y-0">
						<IconsChevronRight />
					</div>
				</button>
			</div>
		</div>
		<div class="flex flex-row gap-x-3 md:gap-x-5 items-center w-full overflow-x-auto px-0.5 py-1">
			<div
				class="category flex shrink-0 h-[10rem] sm:h-[12rem] w-[10rem] sm:w-[12rem] flex-col p-2 ring-1 ring-neutral-200 rounded dark:ring-neutral-700"
			>
				<div class="flex items-center h-[88%] w-full">
					<NuxtImg src="/cat/comp.webp" class="h-full rounded-md w-full" loading="lazy" />
				</div>
				<div class="flex flex-col gap-y-1 py-1">
					<small class="text-sm sm:text-base font-medium text-neutral-600 truncate dark:text-c-mode"
						>Computers & Accessories</small
					>
				</div>
			</div>
			<div
				class="category flex shrink-0 h-[10rem] sm:h-[12rem] w-[10rem] sm:w-[12rem] flex-col p-2 ring-1 ring-neutral-200 rounded dark:ring-neutral-700"
			>
				<div class="flex items-center h-[88%] w-full">
					<NuxtImg src="/cat/men.webp" class="h-full rounded-md w-full" loading="lazy" />
				</div>
				<div class="flex flex-col gap-y-1 py-1">
					<small class="text-sm sm:text-base font-medium text-neutral-600 truncate dark:text-c-mode"
						>Men clothing & Fashion</small
					>
				</div>
			</div>
			<div
				class="category flex shrink-0 h-[10rem] sm:h-[12rem] w-[10rem] sm:w-[12rem] flex-col p-2 ring-1 ring-neutral-200 rounded dark:ring-neutral-700"
			>
				<div class="flex items-center h-[88%] w-full">
					<NuxtImg src="/cat/beauty.webp" class="h-full rounded-md w-full" loading="lazy" />
				</div>
				<div class="flex flex-col gap-y-1 py-1">
					<small class="text-sm sm:text-base font-medium text-neutral-600 truncate dark:text-c-mode">Beauty, Health & Hair</small>
				</div>
			</div>
			<div
				class="category flex shrink-0 h-[10rem] sm:h-[12rem] w-[10rem] sm:w-[12rem] flex-col p-2 ring-1 ring-neutral-200 rounded dark:ring-neutral-700"
			>
				<div class="flex items-center h-[88%] w-full">
					<NuxtImg src="/cat/drinks.webp" class="h-full rounded-md w-full" loading="lazy" />
				</div>
				<div class="flex flex-col gap-y-1 py-1">
					<small class="text-sm sm:text-base font-medium text-neutral-600 truncate dark:text-c-mode">Drinks</small>
				</div>
			</div>
			<div
				class="category flex shrink-0 h-[10rem] sm:h-[12rem] w-[10rem] sm:w-[12rem] flex-col p-2 ring-1 ring-neutral-200 rounded dark:ring-neutral-700"
			>
				<div class="flex items-center h-[88%] w-full">
					<NuxtImg src="/cat/shoes.webp" class="h-full rounded-md w-full" loading="lazy" />
				</div>
				<div class="flex flex-col gap-y-1 py-1">
					<small class="text-sm sm:text-base font-medium text-neutral-600 truncate dark:text-c-mode">Shoes & Sneakers</small>
				</div>
			</div>
			<div
				class="category flex shrink-0 h-[10rem] sm:h-[12rem] w-[10rem] sm:w-[12rem] flex-col p-2 ring-1 ring-neutral-200 rounded dark:ring-neutral-700"
			>
				<div class="flex items-center h-[88%] w-full">
					<NuxtImg src="/cat/speakers.webp" class="h-full rounded-md w-full" loading="lazy" />
				</div>
				<div class="flex flex-col gap-y-1 py-1">
					<small class="text-sm sm:text-base font-medium text-neutral-600 truncate dark:text-c-mode"
						>Speakers & Electronics</small
					>
				</div>
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
