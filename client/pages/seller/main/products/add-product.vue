<script setup lang="ts"></script>

<template>
	<div class="w-full flex flex-col px-4">
		<div class="w-full flex flex-row items-center space-x-4">
			<button class="px-2 py-1.5 rounded-sm border border-neutral-200 text-neutral-600 hover:text-neutral-800">
				<Icon name="mdi:arrow-left" class="text-2xl" />
			</button>
			<h4 class="text-2xl font-semibold">Add product</h4>
		</div>
		<div class="w-full grid grid-cols-10 gap-x-8 mt-10">
			<div class="col-span-7 flex flex-col gap-y-8">
				<div class="form-container">
					<label for="title" class="text-lg font-semibold">Title</label>
					<input
						type="text"
						name="title"
						id="title"
						class="text-base mb-2 px-3 py-2 border border-neutral-300 rounded tracking-wide outline-none focus:border-custom transition"
						placeholder="Short sleeve t-shirt"
					/>
				</div>
				<div class="form-container">
					<span class="text-lg font-semibold">Media</span>
					<div class="w-full grid grid-cols-2 gap-x-3 gap-y-3">
						<div class="flex items-center justify-center border border-neutral-300 rounded p-2">
							<div class="py-8 flex flex-col gap-y-2 items-center justify-center">
								<button
									class="px-2.5 py-1 rounded text-base font-semibold bg-custom/20 text-neutral-600 hover:text-neutral-800"
								>
									Add main image
								</button>
							</div>
						</div>
						<div class="grid grid-cols-2 grid-rows-2 gap-3">
							<div class="flex items-center justify-center border border-dashed border-neutral-300 rounded p-2">
								<div class="py-8 flex flex-col gap-y-2 items-center justify-center">
									<button
										class="px-2.5 py-1 rounded text-base font-semibold bg-custom/20 text-neutral-600 hover:text-neutral-800"
									>
										Add other image
									</button>
								</div>
							</div>
							<div class="flex items-center justify-center border border-dashed border-neutral-300 rounded p-2"></div>
							<div class="flex items-center justify-center border border-dashed border-neutral-300 rounded p-2"></div>
							<div class="flex items-center justify-center border border-dashed border-neutral-300 rounded p-2"></div>
						</div>
					</div>
					<small class="text-sm text-neutral-500">Accepts images: png, jpg, jpeg or webp</small>
				</div>
				<div class="form-container">
					<span class="text-lg font-semibold">Pricing</span>
					<div class="w-full grid grid-cols-2 gap-x-6 py-3.5">
						<div class="flex flex-col gap-y-1">
							<label for="price" class="text-base font-medium">Price</label>
							<div class="w-full relative flex items-center">
								<span class="text-base text-neutral-400 absolute left-2">KES</span>
								<input
									type="text"
									name="price"
									id="price"
									placeholder="0.00"
									class="w-full text-base pl-12 py-2 border border-neutral-300 rounded tracking-wide outline-none focus:border-custom transition"
								/>
							</div>
						</div>
						<div class="flex flex-col gap-y-1">
							<label for="discount" class="text-base font-medium">Discount</label>
							<div class="w-full relative flex items-center">
								<span class="text-base text-neutral-400 absolute left-2">KES</span>
								<input
									type="text"
									name="discount"
									id="discount"
									placeholder="0.00"
									class="w-full text-base pl-12 py-2 border border-neutral-300 rounded tracking-wide outline-none focus:border-custom transition"
								/>
							</div>
						</div>
					</div>
				</div>
				<div class="form-container">
					<span class="text-lg font-semibold">Inventory</span>
					<div class="flex flex-row gap-x-3 items-center py-4">
						<input type="checkbox" name="track" id="track" class="w-5 h-5" />
						<label for="track" class="text-base">Track quantity</label>
					</div>
					<div class="w-full py-4 border-y border-neutral-200 flex flex-row items-center justify-between">
						<span class="text-base font-semibold">Quantity:</span>
						<div class="flex items-center">
							<input
								type="number"
								placeholder="0"
								class="text-base px-3 py-2 border border-neutral-300 rounded tracking-wide outline-none focus:border-custom transition"
							/>
						</div>
					</div>
					<div class="flex flex-row gap-x-3 items-center py-4">
						<input type="checkbox" name="selling" id="selling" class="w-5 h-5" />
						<label for="selling" class="text-base font-medium">Continue selling when out of stock</label>
					</div>
				</div>
				<div class="form-container">
					<span class="text-lg font-semibold">Description</span>
					<ClientOnly>
						<ContentsEditor />
					</ClientOnly>
				</div>
				<div class="w-full flex flex-col -space-y-px pt-3 bg-white shadow-sm rounded border border-neutral-200">
					<span class="text-lg font-semibold px-5">Variants</span>
					<div class="variant-item w-full grid grid-cols-10 px-5 pt-6">
						<div class="col-span-1 flex flex-col pt-8">
							<button class="text-neutral-500">
								<Icon name="mdi:drag-vertical" class="text-2xl" />
							</button>
						</div>
						<div class="col-span-8 flex flex-col gap-y-4 pb-6">
							<div class="flex flex-col w-full">
								<span class="text-base">Option name</span>
								<input
									type="text"
									placeholder="Color"
									class="text-base mb-2 px-3 py-2 border border-neutral-300 rounded tracking-wide outline-none focus:border-custom transition"
								/>
							</div>
							<div class="flex flex-col w-full">
								<span class="text-base">Option values</span>
								<input
									type="text"
									placeholder="Black"
									class="text-base mb-2 px-3 py-2 border border-neutral-300 rounded tracking-wide outline-none focus:border-custom transition"
								/>
							</div>
							<div class="w-full flex flex-row items-center">
								<button
									class="px-4 py-2 border border-neutral-200 rounded hover:border-custom hover:text-custom transition"
								>
									Done
								</button>
							</div>
						</div>
						<div class="col-span-1 flex flex-col pt-6">
							<button class="text-neutral-500">
								<Icon name="mdi:trash-can-outline" class="text-2xl" />
							</button>
						</div>
					</div>
					<div class="px-5 w-full flex flex-col border-t border-neutral-200 mt-3">
						<button class="text-custom flex flex-row items-center py-4 gap-x-4">
							<Icon name="mdi:plus" class="text-2xl font-semibold" />
							<span class="text-base">Add options like size or color</span>
						</button>
					</div>
				</div>
			</div>
			<div class="col-span-3">Other info</div>
		</div>
	</div>
</template>
<style scoped>
.form-container {
	@apply w-full flex flex-col gap-y-1 px-5 py-3 bg-white shadow-sm rounded border border-neutral-200;
}
</style>
