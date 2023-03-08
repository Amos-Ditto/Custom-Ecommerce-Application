<template>
	<div class="col-span-1 bg-white border border-neutral-200 flex flex-col gap-y-2">
		<div class="w-full flex item-center">
			<NuxtImg src="/items/phone.png" class="w-full" />
		</div>
		<div class="w-full flex flex-col gap-y-1 px-2.5 pb-1">
			<div class="w-full flex flex-row gap-x-2 items-center text-base">
				<span class="line-through">$25.75</span>
				<span class="text-custom">$24.98</span>
			</div>
			<ContentsSellerRates />
			<div class="w-full">
				<p class="line-clamp-2 text-base font-medium">Luxury Matte Magnetic For Ma</p>
			</div>
		</div>
	</div>
</template>
