<script setup lang="ts">
const showcart = ref<boolean>(false);
</script>
<template>
	<main class="w-full flex flex-col text-neutral-800 pb-16 md:pb-0">
		<NavsNavTop />
		<slot />
		<NavsNavBottom />
		<Footer />

		<!-- Cart floating container -->
		<div
			@click="() => (showcart = !showcart)"
			class="fixed right-0 bottom-1/2 translate-y-1/2 hidden md:flex flex-col gap-y-2 py-3 pl-3 pr-2.5 rounded-l-xl bg-custom cursor-pointer"
		>
			<div class="flex flex-row justify-between items-center gap-x-1 text-c-base">
				<Icon name="mdi:cart-variant" class="text-2xl" />
				<div class="flex flex-row items-center gap-x-1">
					<span class="text-base">0</span>
					<span class="text-base">item(s)</span>
				</div>
			</div>
			<div class="flex flex-col w-full">
				<button class="bg-c-base py-1.5 px-2 rounded text-custom text-base w-full">KES 0.00</button>
			</div>
		</div>
		<Transition name="slide-cart">
			<ContainersCartDisplay v-if="showcart" @close-cart="() => (showcart = !showcart)" />
		</Transition>
	</main>
</template>

<style scoped>
.slide-cart-enter-from,
.slide-cart-leave-to {
	@apply opacity-0 translate-x-full;
}
.slide-cart-enter-active,
.slide-cart-leave-active {
	@apply transition duration-300;
}
</style>
