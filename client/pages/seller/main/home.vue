<template>
	<div class="w-full flex flex-col">
		<div class="w-full grid grid-cols-4 gap-x-4">
			<div class="bg-white border border-neutral-200 rounded px-5 min-h-[8rem] flex flex-col items-start justify-center text-custom">
				<span class="text-base font-semibold">Total Products</span>
				<span class="text-4xl font-semibold">15</span>
			</div>
			<div class="bg-white border border-neutral-200 rounded px-5 min-h-[8rem] flex flex-col items-start justify-center text-custom">
				<span class="text-base font-semibold">Total Orders</span>
				<span class="text-4xl font-semibold">10</span>
			</div>
			<div class="bg-white border border-neutral-200 rounded px-5 min-h-[8rem] flex flex-col items-start justify-center text-custom">
				<span class="text-base font-semibold">Earnings</span>
				<span class="text-4xl font-semibold">$1,372.79</span>
			</div>
			<div class="bg-white border border-neutral-200 rounded px-5 min-h-[8rem] flex flex-col items-start justify-center text-custom">
				<span class="text-base font-semibold">Total Sales</span>
				<span class="text-4xl font-semibold">$887.63</span>
			</div>
		</div>
		<div class="w-full grid grid-cols-2 gap-x-6 mt-12">
			<div class="flex flex-col">
				<div class="grid grid-cols-2 gap-3">
					<div
						class="bg-white rounded border border-neutral-200 min-h-[6rem] px-6 py-4 flex flex-row items-center justify-between"
					>
						<div class="flex flex-col">
							<Icon name="mdi:shopping" class="text-3xl text-custom" />
						</div>
						<div class="flex flex-col">
							<span class="text-base font-medium">Placed Orders</span>
						</div>
						<div class="flex flex-col">
							<span class="text-4xl font-semibold text-custom">4</span>
						</div>
					</div>
					<div
						class="bg-white rounded border border-neutral-200 min-h-[6rem] px-6 py-4 flex flex-row items-center justify-between"
					>
						<div class="flex flex-col">
							<Icon name="mdi:basket-check-outline" class="text-3xl text-green-500" />
						</div>
						<div class="flex flex-col">
							<span class="text-base font-medium">Confirmed Orders</span>
						</div>
						<div class="flex flex-col">
							<span class="text-4xl font-semibold text-green-500">1</span>
						</div>
					</div>
					<div
						class="bg-white rounded border border-neutral-200 min-h-[6rem] px-6 py-4 flex flex-row items-center justify-between"
					>
						<div class="flex flex-col">
							<Icon name="mdi:package-variant-closed" class="text-3xl text-purple-400" />
						</div>
						<div class="flex flex-col">
							<span class="text-base font-medium">Processed Orders</span>
						</div>
						<div class="flex flex-col">
							<span class="text-4xl font-semibold text-purple-400">1</span>
						</div>
					</div>
					<div
						class="bg-white rounded border border-neutral-200 min-h-[6rem] px-6 py-4 flex flex-row items-center justify-between"
					>
						<div class="flex flex-col">
							<Icon name="mdi:truck-delivery-outline" class="text-3xl text-red-500" />
						</div>
						<div class="flex flex-col">
							<span class="text-base font-medium">Delivered Orders</span>
						</div>
						<div class="flex flex-col">
							<span class="text-4xl font-semibold text-red-500">3</span>
						</div>
					</div>
				</div>
			</div>
			<div class="flex flex-col border border-neutral-200 bg-white px-4 -space-y-px">
				<div class="flex flex-col items-start border-b border-neutral-200 py-3">
					<h4 class="text-2xl font-semibold">Recent Orders</h4>
				</div>
				<ul id="list-orders" class="w-full flex flex-col gap-y-0.5 -space-y-px">
					<li class="flex flex-col border-t border-neutral-200 py-2.5 px-2 text-neutral-600">
						<span class="text-lg font-semibold">20221221-16180436</span>
						<span class="text-base">Dec 21, 2022</span>
					</li>
					<li class="flex flex-col border-t border-neutral-200 py-2.5 px-2 text-neutral-600">
						<span class="text-lg font-semibold">20221221-16180436</span>
						<span class="text-base">Dec 21, 2022</span>
					</li>
				</ul>
				<div class="w-full border-t border-neutral-200 py-2.5 px-2 items-center">
					<button class="text-base font-semibold text-custom">View more</button>
				</div>
			</div>
		</div>
		<div class="w-full flex flex-col mt-6">
			<div class="w-full flex flex-col gap-y-4">
				<h3 class="text-2xl font-semibold">Top Products</h3>
				<div class="w-full grid grid-cols-6 gap-x-3">
					<ListSellerItem />
					<ListSellerItem />
					<ListSellerItem />
					<ListSellerItem />
					<ListSellerItem />
					<ListSellerItem />
				</div>
			</div>
		</div>
	</div>
</template>
