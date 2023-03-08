<template>
	<div class="w-full flex flex-col">
		<NuxtLayout name="seller">
			<section class="w-full grid grid-cols-12 gap-x-4 px-6 h-[calc(100vh-80px)] mt-1">
				<div class="col-span-2 h-full flex flex-col">
					<aside class="w-full h-full flex flex-col gap-y-4">
						<div class="flex flex-col gap-y-2.5 justify-center items-center py-5 bg-alt-dark rounded text-c-base">
							<div class="flex flex-col">
								<NuxtImg src="/sellers/avatar.png" class="w-20 h-20 rounded-full" />
							</div>
							<div class="flex flex-col">
								<span class="text-xl font-semibold">Beauty Shop</span>
								<small class="text-sm">+254 794 818 111</small>
							</div>
						</div>
						<!-- Links -->
						<div class="px-2.5 py-3 w-full h-full rounded border border-neutral-200">
							<ul id="seller-dash-links" class="w-full flex flex-col gap-y-0.5">
								<li>
									<Icon name="mdi:view-dashboard" class="icon" />
									<span>Dashboard</span>
								</li>
								<li>
									<Icon name="mdi:basket" class="icon" />
									<span>Products</span>
								</li>
								<li>
									<Icon name="mdi:list-box" class="icon" />
									<span>Orders</span>
								</li>
								<li>
									<Icon name="mdi:message-bulleted" class="icon" />
									<span>Product Querries</span>
								</li>
								<li>
									<Icon name="mdi:star-settings" class="icon" />
									<span>Reviews</span>
								</li>
								<li>
									<Icon name="mdi:cog" class="icon" />
									<span>Shop Settings</span>
								</li>
							</ul>
						</div>
					</aside>
				</div>
				<div class="col-span-10 h-full w-full flex flex-col">
					<NuxtPage />
				</div>
			</section>
		</NuxtLayout>
	</div>
</template>

<style scoped>
ul#seller-dash-links li {
	@apply w-full flex flex-row items-center gap-x-3 px-2 py-2.5 hover:bg-custom rounded cursor-pointer transition duration-200;
}

ul#seller-dash-links li .icon {
	@apply w-6 h-6 text-neutral-600;
}
ul#seller-dash-links li span {
	@apply text-neutral-700 text-base font-semibold;
}
ul#seller-dash-links li:hover .icon,
ul#seller-dash-links li:hover span {
	@apply text-c-base;
}
</style>
