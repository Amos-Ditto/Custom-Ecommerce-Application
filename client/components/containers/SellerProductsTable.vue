<template>
	<div class="w-full flex flex-col">
		<div class="grid grid-cols-[repeat(13,minmax(0,1fr))] gap-x-4 text-xs text-gray-700 font-bold uppercase bg-white py-4 px-6">
			<div class="">
				<span>#</span>
			</div>
			<div class="col-span-2">
				<span>Name</span>
			</div>
			<div class="col-span-2">
				<span>Info</span>
			</div>
			<div class="col-span-2">
				<span>Categories</span>
			</div>
			<div class="col-span-2">
				<span>Brand</span>
			</div>
			<div class="col-span-2">
				<span>Published</span>
			</div>
			<div class="col-span-2">
				<span>Actions</span>
			</div>
		</div>
		<ul id="product-list" class="w-full flex flex-col gap-y-0.5">
			<ListSellerProductItem />
			<ListSellerProductItem />
			<ListSellerProductItem />
			<ListSellerProductItem />
		</ul>
	</div>
</template>
