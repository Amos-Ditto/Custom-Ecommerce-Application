<template>
	<div class="w-full flex flex-col gap-y-2 sm:mt-4 bg-[#f5f5f5] dark:bg-[#212121] px-3 py-2 sm:py-4 rounded">
		<div class="w-full flex flex-row items-center justify-between pb-2.5 pt-1 dark:text-c-mode">
			<h3 class="text-base sm:text-lg sm:font-semibold sm:tracking-wide">Explore popular Categories</h3>
			<div class="flex flex-row">
				<button class="text-xs sm:text-sm font-medium flex flex-row items-center gap-x-2">
					<span>See all</span>
					<Icon name="mdi:arrow-right" />
				</button>
			</div>
		</div>
		<div class="w-full grid grid-cols-3 md:grid-cols-6 gap-x-4 sm:gap-x-6 gap-y-4">
			<div class="flex flex-col">
				<div class="w-full flex flex-col">
					<NuxtImg src="/cat/Laptops.png" class="rounded w-full" loading="lazy" />
				</div>
				<button class="w-full flex flex-row items-center justify-between py-1 mt-1 md:mt-2">
					<div class="w-full flex-col">
						<p class="text-sm md:text-base text-start font-medium text-neutral-900 dark:text-c-base line-clamp-1">Laptops</p>
					</div>
					<div class="flex flex-col items-center">
						<Icon name="mdi:arrow-right" class="text-base sm:text-lg text-neutral-500 dark:text-neutral-400" />
					</div>
				</button>
			</div>
			<div class="flex flex-col">
				<div class="w-full flex flex-col">
					<NuxtImg src="/cat/Phones.png" class="rounded w-full" loading="lazy" />
				</div>
				<button class="w-full flex flex-row items-center justify-between py-1 mt-1 md:mt-2">
					<div class="w-full flex-col">
						<p class="text-sm md:text-base text-start font-medium text-neutral-900 dark:text-c-base line-clamp-1">Phones</p>
					</div>
					<div class="flex flex-col items-center">
						<Icon name="mdi:arrow-right" class="text-base sm:text-lg text-neutral-500 dark:text-neutral-400" />
					</div>
				</button>
			</div>
			<div class="flex flex-col">
				<div class="w-full flex flex-col">
					<NuxtImg src="/cat/Speakers.png" class="rounded w-full" loading="lazy" />
				</div>
				<button class="w-full flex flex-row items-center justify-between py-1 mt-1 md:mt-2">
					<div class="w-full flex-col">
						<p class="text-sm md:text-base text-start font-medium text-neutral-900 dark:text-c-base line-clamp-1">Speakers</p>
					</div>
					<div class="flex flex-col items-center">
						<Icon name="mdi:arrow-right" class="text-base sm:text-lg text-neutral-500 dark:text-neutral-400" />
					</div>
				</button>
			</div>
			<div class="flex flex-col">
				<div class="w-full flex flex-col">
					<NuxtImg src="/cat/MenClothing.png" class="rounded w-full" loading="lazy" />
				</div>
				<button class="w-full flex flex-row items-center justify-between py-1 mt-1 md:mt-2">
					<div class="w-full flex-col">
						<p class="text-sm md:text-base text-start font-medium text-neutral-900 dark:text-c-base line-clamp-1">
							Men Clothing
						</p>
					</div>
					<div class="flex flex-col items-center">
						<Icon name="mdi:arrow-right" class="text-base sm:text-lg text-neutral-500 dark:text-neutral-400" />
					</div>
				</button>
			</div>
			<div class="flex flex-col">
				<div class="w-full flex flex-col">
					<NuxtImg src="/cat/Beauty.png" class="rounded w-full" loading="lazy" />
				</div>
				<button class="w-full flex flex-row items-center justify-between py-1 mt-1 md:mt-2">
					<div class="w-full flex-col">
						<p class="text-sm md:text-base text-start font-medium text-neutral-900 dark:text-c-base line-clamp-1">
							Health & Beauty
						</p>
					</div>
					<div class="flex flex-col items-center">
						<Icon name="mdi:arrow-right" class="text-base sm:text-lg text-neutral-500 dark:text-neutral-400" />
					</div>
				</button>
			</div>
			<div class="flex flex-col">
				<div class="w-full flex flex-col">
					<NuxtImg src="/cat/Laptops.png" class="rounded w-full" loading="lazy" />
				</div>
				<button class="w-full flex flex-row items-center justify-between py-1 mt-1 md:mt-2">
					<div class="w-full flex-col">
						<p class="text-sm md:text-base text-start font-medium text-neutral-900 dark:text-c-base line-clamp-1">Laptops</p>
					</div>
					<div class="flex flex-col items-center">
						<Icon name="mdi:arrow-right" class="text-base sm:text-lg text-neutral-500 dark:text-neutral-400" />
					</div>
				</button>
			</div>
		</div>
	</div>
</template>
<style scoped>
::-webkit-scrollbar {
	width: 0px;
	height: 2px;
}
</style>
