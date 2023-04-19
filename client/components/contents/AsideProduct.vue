<template>
	<div class="w-full grid grid-cols-1 sm:grid-cols-10 xl:grid-cols-1 gap-y-8 sm:gap-y-3 gap-x-6">
		<div
			class="w-full flex flex-col bg-gray-100 border border-neutral-200 rounded text-neutral-800 dark:bg-alt-dark dark:border-neutral-700"
		>
			<div class="w-full flex flex-row justify-between items-center border-b border-neutral-200 px-2 py-2 dark:border-neutral-700">
				<h4 class="leading-none m-0 uppercase text-base dark:text-neutral-100">Seller Information</h4>

				<button>
					<Icon name="mdi:chevron-right" class="dark:text-neutral-100" />
				</button>
			</div>
			<div class="w-full flex flex-col gap-y-1 px-2 py-2 text-neutral-600 dark:text-neutral-200">
				<span class="text-lg capitalize font-medium">The Shop</span>
				<small class="">This store has been open since <span class="text-custom">Mar 11, 2020</span></small>
				<span class="text-sm">Less than <span class="text-custom">10</span> products sold</span>
				<button class="bg-custom py-1.5 px-4 mt-2 text-sm text-white rounded-sm">Visit shop</button>
			</div>
		</div>
		<div class="sm:col-span-7 xl:col-span-1 flex flex-col xl:mt-6">
			<div class="w-full flex flex-col gap-y-2">
				<h3 class="text-base uppercase text-neutral-900 font-medium dark:text-neutral-100">Related Products</h3>
				<ul class="w-full grid grid-cols-2 xl:grid-cols-1 gap-4">
					<li class="flex flex-col px-3 py-3 border border-neutral-200 rounded-sm dark:border-neutral-700">
						<div class="w-full">
							<NuxtImg src="/items/phone.png" class="w-full rounded-sm" />
						</div>
						<div class="w-full flex flex-col sm:flex-row items-start sm:items-center gap-x-3 gap-y-1 mt-3">
							<span class="text-base text-neutral-600 dark:text-neutral-200">KES 30,000</span>
							<button class="px-2 py-0.5 rounded-sm bg-[tomato] text-white uppercase text-xs">off 5%</button>
						</div>
					</li>
					<li class="flex flex-col px-3 py-3 border border-neutral-200 rounded-sm dark:border-neutral-700">
						<div class="w-full">
							<NuxtImg src="/items/phone.png" class="w-full rounded-sm" />
						</div>
						<div class="w-full flex flex-col sm:flex-row items-start sm:items-center gap-x-3 gap-y-1 mt-3">
							<span class="text-base text-neutral-600 dark:text-neutral-200">KES 30,000</span>
							<button class="px-2 py-0.5 rounded-sm bg-[tomato] text-white uppercase text-xs">off 5%</button>
						</div>
					</li>
					<li class="flex flex-col px-3 py-3 border border-neutral-200 rounded-sm dark:border-neutral-700">
						<div class="w-full">
							<NuxtImg src="/items/phone.png" class="w-full rounded-sm" />
						</div>
						<div class="w-full flex flex-col sm:flex-row items-start sm:items-center gap-x-3 gap-y-1 mt-3">
							<span class="text-base text-neutral-600 dark:text-neutral-200">KES 30,000</span>
							<button class="px-2 py-0.5 rounded-sm bg-[tomato] text-white uppercase text-xs">off 5%</button>
						</div>
					</li>
				</ul>
			</div>
		</div>
	</div>
</template>
