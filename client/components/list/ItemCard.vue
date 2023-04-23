<script setup lang="ts">
const add_favorite = ref<boolean>(false);
</script>
<template>
	<div class="w-full flex flex-col py-2 px-2 ring-1 ring-neutral-200 rounded-sm sm:rounded dark:ring-neutral-700">
		<NuxtLink to="/products/product-1" class="w-full flex relative">
			<NuxtImg src="/items/tecno.jpg" class="w-full rounded" loading="lazy" />
			<div class="absolute top-1 -left-2">
				<button class="bg-[tomato] rounded-sm text-xs text-white px-1.5 py-1 uppercase -translate-x-1/4 translate-y-1/2 -rotate-90">
					off 2%
				</button>
			</div>
		</NuxtLink>
		<div class="flex flex-col mt-1.5 gap-y-1 w-full">
			<div class="price flex flex-row items-baseline gap-x-2 w-full">
				<span class="text-sm sm:text-lg text-neutral-700 font-semibold dark:text-c-mode"
					><span class="text-sm">KES</span> 25.00</span
				>
				<span class="mt-0.5 text-xs sm:text-sm text-neutral-500 line-through font-semibold dark:text-neutral-200"
					><span class="">KES</span> 30.00</span
				>
			</div>
			<div class="name w-full">
				<small class="line-clamp-2 text-xs sm:text-sm dark:text-c-mode text-neutral-600"
					>Asus ROG Phone 5 Dual Sim s888 Phantom</small
				>
			</div>
			<div class="w-full flex flex-row justify-between items-center">
				<button
					class="text-xs sm:text-sm font-normal sm:font-medium text-neutral-50 tracking-wide flex flex-row items-center gap-x-1 py-1 px-2 bg-custom hover:bg-opacity-90 rounded transition duration-200"
				>
					<Icon name="mdi:cart-outline" class="text-base" />
					Buy Now
				</button>
				<div role="button" @click="() => (add_favorite = !add_favorite)" class="px-2 py-1 text-custom flex items-center">
					<Transition mode="out-in">
						<!-- <IconsHeartSolid /> -->
						<Icon v-if="add_favorite" name="mdi:heart" class="text-xl dark:text-custom" />
						<Icon v-else name="mdi:heart-outline" class="text-xl dark:text-custom" />
						<!-- <IconsHeart /> -->
					</Transition>
				</div>
			</div>
		</div>
	</div>
</template>
