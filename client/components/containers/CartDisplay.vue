<script setup lang="ts">
const emits = defineEmits<{
	(e: "closeCart"): void;
}>();
</script>
<template>
	<div
		class="fixed top-0 bottom-0 right-0 flex flex-col py-3 z-50 bg-c-base w-[80%] sm:w-[60%] md:w-[54%] lg:w-[35%] xl:w-[31%] 2xl:w-1/4 shadow-2xl"
	>
		<div class="border-b border-neutral-200 pt-3 pb-4 px-4 flex flex-row justify-between items-center relative w-full">
			<div class="flex flex-row gap-x-2 items-center">
				<div class="w-9 h-9 text-custom">
					<IconsCart />
				</div>
				<span class="text-xl font-semibold">14 item(s)</span>
			</div>
			<div class="absolute right-4">
				<button @click="() => emits('closeCart')" class="w-7 h-7 p-0.5 hover:opacity-80 hover:bg-neutral-200 rounded transition">
					<IconsClose />
				</button>
			</div>
		</div>

		<ul class="w-full flex flex-col mt-1 overflow-y-auto pb-16">
			<ListCartItemList />
			<ListCartItemList />
			<ListCartItemList />
			<ListCartItemList />
		</ul>
		<div class="w-full px-4 py-3.5 absolute bottom-0 border-t bg-c-base">
			<button class="w-full bg-custom py-2.5 text-c-base text-lg font-semibold rounded">Checkout $1,000.90</button>
		</div>
	</div>
</template>

<style scoped>
::-webkit-scrollbar {
	width: 3px;
}
</style>
