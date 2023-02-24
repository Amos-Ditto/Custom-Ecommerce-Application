<template>
	<section class="w-full flex flex-col gap-y-4 mt-4">
		<h3 class="text-2xl font-semibold text-neutral-700">Dashboard</h3>
		<div class="w-full grid grid-cols-1 sm:grid-cols-3 gap-y-6 gap-x-3 xl:gap-x-6 mt-2">
			<div class="flex flex-col gap-y-3 items-center justify-center py-4 md:py-6 rounded bg-[#424242] text-custom">
				<h3 class="text-3xl md:text-4xl font-semibold tracking-wide text-c-base">14</h3>
				<h5 class="text-base">Products in Your Cart</h5>
			</div>
			<div class="flex flex-col gap-y-3 items-center justify-center py-4 md:py-6 rounded bg-[#424242] text-blue-400">
				<h3 class="text-3xl md:text-4xl font-semibold tracking-wide text-c-base">30</h3>
				<h5 class="text-base">Products in Your Wishlist</h5>
			</div>
			<div class="flex flex-col gap-y-3 items-center justify-center py-4 md:py-6 rounded bg-[#424242] text-green-400">
				<h3 class="text-3xl md:text-4xl font-semibold tracking-wide text-c-base">50</h3>
				<h5 class="text-base">Products in You Ordered</h5>
			</div>
		</div>
		<div class="w-full grid grid-cols-1 md:grid-cols-3 gap-y-6 gap-x-3 xl:gap-x-6 mt-6 xl:mt-10">
			<!-- Purchased -->
			<div class="min-h-[40vh] max-h-[48vh] flex flex-col px-2.5 border border-neutral-200 rounded overflow-y-auto">
				<div class="w-full flex-row items-center pt-3.5 pb-2 border-b border-neutral-200 sticky top-0 z-10 bg-c-base">
					<h4 class="text-lg font-semibold truncate">Recent Purchase History</h4>
				</div>
				<ul class="items-lists w-full flex flex-col">
					<li>
						<NuxtLink to="/products/product-1" class="col-span-2 md:col-span-3 lg:col-span-4 flex items-center justify-center">
							<NuxtImg src="/items/phone.png" class="w-full rounded" />
						</NuxtLink>
						<div class="col-span-10 md:col-span-9 lg:col-span-8 flex flex-col items-center justify-center gap-y-2">
							<NuxtLink to="/products/product-1" class="text-sm text-start w-full text-neutral-600 line-clamp-1"
								>Asus ROG Phone 5 Dual Sim s888 Phantom</NuxtLink
							>
							<div class="flex flex-row gap-x-1 items-center w-full">
								<span class="text-base text-neutral-600 line-through">$300.00</span>
								<span class="text-base font-semibold">$280.00</span>
							</div>
						</div>
					</li>
					<li>
						<NuxtLink to="/products/product-1" class="col-span-2 md:col-span-3 lg:col-span-4 flex items-center justify-center">
							<NuxtImg src="/items/phone.png" class="w-full rounded" />
						</NuxtLink>
						<div class="col-span-10 md:col-span-9 lg:col-span-8 flex flex-col items-center justify-center gap-y-2">
							<NuxtLink to="/products/product-1" class="text-sm text-start w-full text-neutral-600 line-clamp-1"
								>Asus ROG Phone 5 Dual Sim s888 Phantom</NuxtLink
							>
							<div class="flex flex-row gap-x-1 items-center w-full">
								<span class="text-base text-neutral-600 line-through">$300.00</span>
								<span class="text-base font-semibold">$280.00</span>
							</div>
						</div>
					</li>
					<li>
						<NuxtLink to="/products/product-1" class="col-span-2 md:col-span-3 lg:col-span-4 flex items-center justify-center">
							<NuxtImg src="/items/phone.png" class="w-full rounded" />
						</NuxtLink>
						<div class="col-span-10 md:col-span-9 lg:col-span-8 flex flex-col items-center justify-center gap-y-2">
							<NuxtLink to="/products/product-1" class="text-sm text-start w-full text-neutral-600 line-clamp-1"
								>Asus ROG Phone 5 Dual Sim s888 Phantom</NuxtLink
							>
							<div class="flex flex-row gap-x-1 items-center w-full">
								<span class="text-base text-neutral-600 line-through">$300.00</span>
								<span class="text-base font-semibold">$280.00</span>
							</div>
						</div>
					</li>
				</ul>
			</div>
			<!-- Wishlist -->
			<div class="max-h-[48vh] flex flex-col px-2.5 border border-neutral-200 rounded overflow-y-auto">
				<div class="w-full flex-row items-center pt-3.5 pb-2 border-b border-neutral-200 sticky top-0 z-10 bg-c-base">
					<h4 class="text-lg font-semibold truncate">My Wishlist</h4>
				</div>
				<ul class="items-lists w-full flex flex-col">
					<li>
						<NuxtLink to="/products/product-1" class="col-span-2 md:col-span-3 lg:col-span-4 flex items-center justify-center">
							<NuxtImg src="/items/phone.png" class="w-full rounded" />
						</NuxtLink>
						<div class="col-span-10 md:col-span-9 lg:col-span-8 flex flex-col items-center justify-center gap-y-2">
							<NuxtLink to="/products/product-1" class="text-sm text-start w-full text-neutral-600 line-clamp-1"
								>Asus ROG Phone 5 Dual Sim s888 Phantom</NuxtLink
							>
							<div class="flex flex-row gap-x-1 items-center w-full">
								<span class="text-base text-neutral-600 line-through">$300.00</span>
								<span class="text-base font-semibold">$280.00</span>
							</div>
						</div>
					</li>
					<li>
						<NuxtLink to="/products/product-1" class="col-span-2 md:col-span-3 lg:col-span-4 flex items-center justify-center">
							<NuxtImg src="/items/phone.png" class="w-full rounded" />
						</NuxtLink>
						<div class="col-span-10 md:col-span-9 lg:col-span-8 flex flex-col items-center justify-center gap-y-2">
							<NuxtLink to="/products/product-1" class="text-sm text-start w-full text-neutral-600 line-clamp-1"
								>Asus ROG Phone 5 Dual Sim s888 Phantom</NuxtLink
							>
							<div class="flex flex-row gap-x-1 items-center w-full">
								<span class="text-base text-neutral-600 line-through">$300.00</span>
								<span class="text-base font-semibold">$280.00</span>
							</div>
						</div>
					</li>
					<li>
						<NuxtLink to="/products/product-1" class="col-span-2 md:col-span-3 lg:col-span-4 flex items-center justify-center">
							<NuxtImg src="/items/phone.png" class="w-full rounded" />
						</NuxtLink>
						<div class="col-span-10 md:col-span-9 lg:col-span-8 flex flex-col items-center justify-center gap-y-2">
							<NuxtLink to="/products/product-1" class="text-sm text-start w-full text-neutral-600 line-clamp-1"
								>Asus ROG Phone 5 Dual Sim s888 Phantom</NuxtLink
							>
							<div class="flex flex-row gap-x-1 items-center w-full">
								<span class="text-base text-neutral-600 line-through">$300.00</span>
								<span class="text-base font-semibold">$280.00</span>
							</div>
						</div>
					</li>
				</ul>
			</div>
			<div class="max-h-[48vh] grid grid-cols-1 grid-rows-3 gap-y-3">
				<div class="row-span-2 px-2.5 flex flex-col border border-neutral-200 rounded">
					<div class="w-full flex-row items-center pt-3.5 pb-2 border-b border-neutral-200 sticky top-0 z-0 bg-c-base">
						<h4 class="text-lg font-semibold truncate">Default Shipping Address</h4>
					</div>
					<div class="flex flex-col gap-y-1 py-2">
						<p class="text-sm lg:text-base">
							4471 Nutters Barn Lane Des Moines, IA 50309 5252, Alabaster, Alabama United States
						</p>
						<p class="text-sm lg:text-base">5156416642</p>
					</div>
				</div>
				<div
					class="py-2 px-4 flex justify-center items-center bg-red-400/10 rounded border-dashed border-2 border-neutral-200 cursor-pointer"
				>
					<div class="flex flex-row gap-x-1 items-center text-custom">
						<div class="w-5 h-5">
							<IconsPlus />
						</div>
						<span class="text-lg font-medium">Add New Address</span>
					</div>
				</div>
			</div>
		</div>
	</section>
</template>

<style scoped>
.items-lists li {
	@apply grid grid-cols-12 gap-x-1 px-2.5 py-2 border-b border-neutral-200 last:border-none;
}

::-webkit-scrollbar {
	width: 3px;
}
</style>
