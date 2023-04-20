<template>
	<div class="shrink-0 w-[250px] lg:w-auto flex flex-col border border-neutral-200 rounded dark:border-neutral-700">
		<div class="w-full flex flex-col relative">
			<img src="/shop-1-banner.webp" alt="" class="object-cover w-full h-[150px] rounded-t" />
			<div class="absolute left-0 right-0 bottom-0 py-2 bg-neutral-700/90 flex items-center justify-center">
				<ContentsRatings />
			</div>
		</div>
		<div class="w-full flex flex-col py-4 px-4 gap-y-1 text-neutral-700">
			<h4 class="text-lg md:text-2xl text-center font-semibold dark:text-neutral-200 line-clamp-1">Beauty Shop</h4>
			<span class="text-xs sm:text-sm text-center dark:text-neutral-200"
				>Less than <span class="text-custom">10</span> products sold</span
			>
			<div class="w-full flex flex-col mt-4 sm:mt-6 sm:px-8">
				<button
					class="py-2 text-sm border border-custom/80 hover:border-custom bg-custom/10 hover:bg-custom/20 rounded font-semibold dark:bg-alt-dark dark:text-neutral-200 dark:border-custom/60 dark:hover:border-custom/90 transition-colors duration-200"
				>
					Visit Store
				</button>
			</div>
		</div>
	</div>
</template>
