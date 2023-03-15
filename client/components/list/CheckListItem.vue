<script setup lang="ts">
const props = defineProps<{
	itemName: string;
}>();
</script>
<template>
	<div class="inline-flex items-center">
		<label class="relative flex cursor-pointer items-center rounded-full gap-x-2">
			<div class="style-checkbox relative flex">
				<input
					type="checkbox"
					class="peer relative h-5 w-5 cursor-pointer appearance-none rounded-md border border-neutral-300 transition-all checked:border-custom checked:bg-custom"
				/>
				<div
					class="icon pointer-events-none h-3.5 w-3.5 absolute top-2/4 left-2/4 -translate-y-2/4 -translate-x-2/4 text-white opacity-0 transition-opacity peer-checked:opacity-100"
				>
					<IconsCheck />
				</div>
			</div>
			<span class="cursor-pointer select-none text-base text-neutral-700 line-clamp-1">{{ props.itemName }}</span>
		</label>
	</div>
</template>
