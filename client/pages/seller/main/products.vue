<template>
	<section class="w-full flex flex-col">
		<div class="w-full flex flex-row justify-between items-center">
			<h4 class="text-2xl font-semibold">All products</h4>
			<div class="flex flex-row items-center">
				<button class="px-5 py-2.5 text-base text-c-base bg-custom rounded">Add New Product</button>
			</div>
		</div>
		<div class="w-full flex flex-col bg-white rounded border border-neutral-200 mt-12">
			<div class="w-full px-6 py-4 border-b border-neutral-200 flex flex-row items-center justify-between">
				<h4 class="text-xl font-medium">All products</h4>
				<div class="flex flex-row items-center justify-between gap-x-4">
					<div class="flex flex-col relative">
						<button
							class="min-w-[12rem] py-2 px-2.5 border border-neutral-200 rounded flex flex-row items-center justify-between gap-x-4 hover:border-custom focus:border-custom transition-colors duration-200"
						>
							<span class="text-base text-neutral-500">Sort by</span>
							<Icon name="mdi:chevron-down" class="text-base text-neutral-500" />
						</button>
					</div>
					<div class="flex flex-col relative">
						<input
							class="max-w-[12rem] py-2 px-2.5 border border-neutral-200 rounded flex flex-row items-center justify-between gap-x-4 outline-none hover:border-custom focus:border-custom transition-colors duration-200"
							placeholder="Type & enter"
						/>
					</div>
				</div>
			</div>
			<div class="w-full">
				<ContainersSellerProductsTable />
			</div>
		</div>
	</section>
</template>
