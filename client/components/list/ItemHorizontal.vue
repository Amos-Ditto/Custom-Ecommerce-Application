<template>
	<div class="grid grid-cols-11 gap-x-2 px-2 py-2 border border-neutral-200 rounded mt-2 dark:border-neutral-700">
		<NuxtLink to="/products/product-1" class="col-span-5 flex items-center justify-center">
			<NuxtImg src="/items/phone.png" class="w-[90%] h-auto" />
		</NuxtLink>
		<div class="col-span-6 flex flex-col gap-y-2 items-start justify-center">
			<div class="flex flex-row gap-x-2 items-baseline">
				<span class="text-base md:text-xl font-medium tracking-wide dark:text-c-mode">$28.98</span>
			</div>
			<div class="flex flex-col">
				<NuxtLink to="/products/product-1" class="text-sm text-neutral-500 line-clamp-2">
					Samsung Electronics Galaxy Buds Live, True Wireless Earbuds W/Active Noise Cancelling (Wireless Charging Case Included)
				</NuxtLink>
			</div>
			<div class="flex flex-row gap-x-4 items-center">
				<button class="px-2.5 py-1.5 bg-custom text-c-base text-sm font-semibold rounded-sm flex flex-row gap-x-1 items-center">
					<Icon name="mdi:cart-outline" class="text-base" />
					<span>Buy Now</span>
				</button>
				<button class="px-3 py-1 text-custom flex items-center">
					<Icon name="mdi:heart-outline" class="text-xl" />
				</button>
			</div>
		</div>
	</div>
</template>
