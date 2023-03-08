<template>
	<li>
		<div class="">
			<span>1</span>
		</div>
		<div class="col-span-2 grid grid-cols-3">
			<div class="flex items-start justify-center">
				<NuxtImg src="/items/tecno.jpg" class="w-full" />
			</div>
			<div class="col-span-2">
				<span class="line-clamp-3">Asus ROG Phone 5 Dual Sim s888 Phantom</span>
			</div>
		</div>
		<div class="col-span-2 flex flex-col">
			<div class="w-full flex flex-row items-center gap-x-1">
				<span>Rating:</span>
				<ContentsSellerRates />
			</div>
			<div class="w-full flex flex-row items-center gap-x-1">
				<span>Total Sold:</span>
				<span class="font-semibold">2</span>
			</div>
			<div class="w-full flex flex-row items-center gap-x-1">
				<span>Price:</span>
				<span class="font-semibold">$98.00</span>
			</div>
		</div>
		<div class="col-span-2">
			<button class="bg-neutral-100 px-2 py-1 font-semibold rounded">Phones & Tablets</button>
		</div>
		<div class="col-span-2">
			<NuxtImg src="/samsung.png" class="max-h-[3rem]" />
		</div>
		<div class="col-span-2">
			<label class="relative inline-flex items-center cursor-pointer">
				<input type="checkbox" value="" class="sr-only peer" checked />
				<div
					class="w-11 h-6 bg-gray-200 rounded-full peer peer-focus:ring-2 peer-focus:ring-green-300 peer-checked:after:translate-x-full peer-checked:after:border-white after:content-[''] after:absolute after:top-0.5 after:left-[2px] after:bg-white after:border-gray-300 after:border after:rounded-full after:h-5 after:w-5 after:transition-all dark:border-gray-600 peer-checked:bg-green-600/50"
				></div>
			</label>
		</div>
		<div class="col-span-2 flex items-start justify-start space-x-3">
			<a href="#" class="font-medium text-green-600 hover:underline">View</a>
			<a href="#" class="font-medium text-blue-600 hover:underline">Edit</a>
			<a href="#" class="font-medium text-red-600 dark:text-red-500 hover:underline">Remove</a>
		</div>
	</li>
</template>

<style scoped>
#product-list li {
	@apply grid grid-cols-[repeat(13,minmax(0,1fr))] gap-x-4 text-sm text-gray-700 bg-white px-6 py-4 hover:bg-gray-50 border-t;
}
</style>
