<template>
	<div class="w-full flex flex-col px-4">
		<div class="w-full flex flex-row items-center space-x-4">
			<button class="px-2 py-1.5 rounded-sm border border-neutral-200 text-neutral-600 hover:text-neutral-800">
				<Icon name="mdi:arrow-left" class="text-2xl" />
			</button>
			<h4 class="text-2xl font-semibold">Add product</h4>
		</div>
		<div class="w-full grid grid-cols-10 gap-x-8 mt-10">
			<div class="col-span-7">
				<div class="form-container"></div>
			</div>
			<div class="col-span-3">Other info</div>
		</div>
	</div>
</template>
<style scoped>
.form-container {
	@apply w-full flex flex-col gap-y-2 px-4 py-3 bg-white shadow-sm rounded border border-neutral-200;
}
</style>
