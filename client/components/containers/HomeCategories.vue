<template>
	<div class="w-full flex flex-col gap-y-2 mt-2 sm:mt-4 bg-[#f5f5f5] dark:bg-[#212121] px-4 py-4 rounded">
		<div class="w-full flex flex-row items-center justify-between pb-2.5 pt-1 dark:text-c-mode">
			<h3 class="text-base sm:text-lg font-semibold tracking-wide">Explore popular Categories</h3>
			<div class="flex flex-row">
				<button class="text-xs sm:text-sm font-medium flex flex-row items-center gap-x-2">
					<span>See all</span>
					<Icon name="mdi:arrow-right" />
				</button>
			</div>
		</div>
		<!-- <div class="hidden md:flex flex-col items-center justify-center mr-1">
			<button class="p-2 rounded-full bg-c-base dark:bg-c-dark dark:text-c-base">
				<div class="w-5 h-5 rotate-180">
					<IconsChevronRight />
				</div>
			</button>
		</div> -->
		<!-- <div class="w-full flex flex-row gap-x-2 sm:gap-x-4 items-center px-2 overflow-x-auto pb-3">
			<div
				class="flex flex-col gap-y-2 w-[100px] md:w-[140px] sm:h-[140px] md:h-[183px] bg-c-base dark:bg-c-dark py-2 px-2 items-center rounded-xl"
			>
				<div class="h-[80px] md:h-[124px] w-[80px] md:w-[124px] flex items-center justify-center">
					<NuxtImg src="/cat/Laptops.png" class="rounded-md w-full h-full" loading="lazy" />
				</div>
				<div class="w-full flex-col">
					<p class="text-xs sm:text-sm md:text-base text-center font-medium text-neutral-900 dark:text-c-base">
						Laptops
					</p>
				</div>
			</div>
			<div
				class="flex flex-col gap-y-2 w-[100px] md:w-[140px] sm:h-[140px] md:h-[183px] bg-c-base dark:bg-c-dark py-2 px-2 items-center rounded-xl"
			>
				<div class="h-[80px] md:h-[124px] w-[80px] md:w-[124px] flex items-center justify-center">
					<NuxtImg src="/cat/Phones.png" class="rounded-md w-full h-full" loading="lazy" />
				</div>
				<div class="w-full flex-col">
					<p class="text-xs sm:text-sm md:text-base text-center font-medium text-neutral-900 dark:text-c-base">
						Phones
					</p>
				</div>
			</div>
			<div
				class="flex flex-col gap-y-2 w-[100px] md:w-[140px] sm:h-[140px] md:h-[183px] bg-c-base dark:bg-c-dark py-2 px-2 items-center rounded-xl"
			>
				<div class="h-[80px] md:h-[124px] w-[80px] md:w-[124px] flex items-center justify-center">
					<NuxtImg src="/cat/Speakers.png" class="rounded-md w-full h-full" loading="lazy" />
				</div>
				<div class="w-full flex-col">
					<p class="text-xs sm:text-sm md:text-base text-center font-medium text-neutral-900 dark:text-c-base">
						Speakers
					</p>
				</div>
			</div>
			<div
				class="flex flex-col gap-y-2 w-[100px] md:w-[140px] sm:h-[140px] md:h-[183px] bg-c-base dark:bg-c-dark py-2 px-2 items-center rounded-xl"
			>
				<div class="h-[80px] md:h-[124px] w-[80px] md:w-[124px] flex items-center justify-center">
					<NuxtImg src="/cat/MenClothing.png" class="rounded-md w-full h-full" loading="lazy" />
				</div>
				<div class="w-full flex-col">
					<p class="text-xs sm:text-sm md:text-base text-center font-medium text-neutral-900 dark:text-c-base">
						Men Clothing
					</p>
				</div>
			</div>
			<div
				class="flex flex-col gap-y-2 w-[100px] md:w-[140px] sm:h-[140px] md:h-[183px] bg-c-base dark:bg-c-dark py-2 px-2 items-center rounded-xl"
			>
				<div class="h-[80px] md:h-[124px] w-[80px] md:w-[124px] flex items-center justify-center">
					<NuxtImg src="/cat/Beauty.png" class="rounded-md w-full h-full" loading="lazy" />
				</div>
				<div class="w-full flex-col">
					<p class="text-xs sm:text-sm md:text-base text-center font-medium text-neutral-900 dark:text-c-base">
						Beauty
					</p>
				</div>
			</div>

			<div
				class="flex flex-col gap-y-2 w-[100px] md:w-[140px] sm:h-[140px] md:h-[183px] bg-c-base dark:bg-c-dark py-2 px-2 items-center rounded-xl"
			>
				<div class="h-[80px] md:h-[124px] w-[80px] md:w-[124px] flex items-center justify-center">
					<NuxtImg src="/cat/Speakers.png" class="rounded-md w-full h-full" loading="lazy" />
				</div>
				<div class="w-full flex-col">
					<p class="text-xs sm:text-sm md:text-base text-center font-medium text-neutral-900 dark:text-c-base">
						Speakers
					</p>
				</div>
			</div>
			<div
				class="flex flex-col gap-y-2 w-[100px] md:w-[140px] sm:h-[140px] md:h-[183px] bg-c-base dark:bg-c-dark py-2 px-2 items-center rounded-xl"
			>
				<div class="h-[80px] md:h-[124px] w-[80px] md:w-[124px] flex items-center justify-center">
					<NuxtImg src="/cat/MenClothing.png" class="rounded-md w-full h-full" loading="lazy" />
				</div>
				<div class="w-full flex-col">
					<p class="text-xs sm:text-sm md:text-base text-center font-medium text-neutral-900 dark:text-c-base">
						Men Clothing
					</p>
				</div>
			</div>
			<div
				class="flex flex-col gap-y-2 w-[100px] md:w-[140px] sm:h-[140px] md:h-[183px] bg-c-base dark:bg-c-dark py-2 px-2 items-center rounded-xl"
			>
				<div class="h-[80px] md:h-[124px] w-[80px] md:w-[124px] flex items-center justify-center">
					<NuxtImg src="/cat/Beauty.png" class="rounded-md w-full h-full" loading="lazy" />
				</div>
				<div class="w-full flex-col">
					<p class="text-xs sm:text-sm md:text-base text-center font-medium text-neutral-900 dark:text-c-base">
						Beauty
					</p>
				</div>
			</div>
		</div> -->
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
						<Icon name="mdi:arrow-right" class="text-lg text-neutral-500 dark:text-neutral-400" />
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
						<Icon name="mdi:arrow-right" class="text-lg text-neutral-500 dark:text-neutral-400" />
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
						<Icon name="mdi:arrow-right" class="text-lg text-neutral-500 dark:text-neutral-400" />
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
						<Icon name="mdi:arrow-right" class="text-lg text-neutral-500 dark:text-neutral-400" />
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
						<Icon name="mdi:arrow-right" class="text-lg text-neutral-500 dark:text-neutral-400" />
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
						<Icon name="mdi:arrow-right" class="text-lg text-neutral-500 dark:text-neutral-400" />
					</div>
				</button>
			</div>
		</div>
		<!-- <div class="ml-1 hidden md:flex flex-col items-center justify-center">
			<button class="p-2 rounded-full bg-c-base dark:bg-c-dark dark:text-c-base">
				<div class="w-5 h-5">
					<IconsChevronRight />
				</div>
			</button>
		</div> -->
	</div>
</template>
<style scoped>
::-webkit-scrollbar {
	width: 0px;
	height: 2px;
}
</style>
