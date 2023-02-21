<template>
	<div class="grid grid-cols-11 gap-x-2 px-2 py-2 border border-neutral-200 rounded mt-2">
		<NuxtLink to="/products/product-1" class="col-span-5 flex items-center justify-center">
			<NuxtImg src="/items/phone.png" class="w-[90%] h-auto" />
		</NuxtLink>
		<div class="col-span-6 flex flex-col gap-y-2 items-start justify-center">
			<div class="flex flex-row gap-x-2 items-center">
				<span class="text-base md:text-lg font-medium text-neutral-400 line-through tracking-wide">$30.00</span>
				<span class="text-base md:text-lg font-semibold tracking-wide">$28.98</span>
			</div>
			<div class="flex flex-col">
				<NuxtLink to="/products/product-1" class="text-sm text-neutral-500 line-clamp-2">
					Samsung Electronics Galaxy Buds Live, True Wireless Earbuds W/Active Noise Cancelling (Wireless Charging Case Included)
				</NuxtLink>
			</div>
			<div class="flex">
				<ContentsRatings />
			</div>
			<div class="flex flex-row gap-x-4 items-center">
				<button class="px-2.5 py-1.5 bg-custom text-c-base text-sm font-semibold rounded-sm flex flex-row gap-x-1 items-center">
					<div class="w-4 md:w-5 h-4 md:h-5">
						<IconsCart />
					</div>
					<span>Buy Now</span>
				</button>
				<button class="w-5 md:w-6 h-5 md:h-6 text-custom">
					<IconsHeart />
				</button>
			</div>
		</div>
	</div>
</template>
