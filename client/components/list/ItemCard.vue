<script setup lang="ts">
const add_favorite = ref<boolean>(false);
</script>
<template>
	<div class="w-full flex flex-col py-2 px-2 ring-1 ring-neutral-200 rounded dark:ring-neutral-700">
		<div class="w-full flex relative">
			<NuxtImg src="/items/tecno.jpg" class="w-full rounded" loading="lazy" />
			<div class="absolute top-1 -left-2">
				<button class="bg-[tomato] rounded-sm text-xs text-white px-1.5 py-1 uppercase -translate-x-1/4 translate-y-1/2 -rotate-90">
					off 2%
				</button>
			</div>
		</div>
		<div class="flex flex-col mt-1.5 gap-y-1 w-full">
			<div class="price flex flex-row items-center gap-x-2 w-full">
				<span class="text-base sm:text-lg text-neutral-500 line-through font-light dark:text-neutral-200">$30.00</span>
				<span class="text-base sm:text-lg text-neutral-800 font-semibold dark:text-c-mode">$25.00</span>
			</div>
			<div class="name w-full">
				<small class="line-clamp-2 text-sm dark:text-c-mode">Asus ROG Phone 5 Dual Sim s888 Phantom</small>
			</div>
			<div class="w-full flex flex-row justify-between items-center">
				<button
					class="text-sm font-normal sm:font-medium text-neutral-50 tracking-wide flex flex-row items-center gap-x-1 py-1 px-2 bg-custom hover:bg-opacity-90 rounded transition duration-200"
				>
					<div class="w-4 h-4">
						<IconsCart />
					</div>
					Buy Now
				</button>
				<div role="button" @click="() => (add_favorite = !add_favorite)" class="w-5 h-5 text-custom">
					<Transition mode="out-in">
						<IconsHeartSolid v-if="add_favorite" />
						<IconsHeart v-else />
					</Transition>
				</div>
			</div>
		</div>
	</div>
</template>
