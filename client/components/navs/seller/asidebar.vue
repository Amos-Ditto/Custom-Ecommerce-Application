<template>
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
		<div class="px-2.5 py-3 w-full h-full rounded border border-neutral-200 bg-white">
			<ul id="seller-dash-links" class="w-full flex flex-col gap-y-0.5">
				<li>
					<NuxtLink :to="{ name: 'Seller-Home' }">
						<Icon name="mdi:view-dashboard" class="icon" />
						<span>Dashboard</span>
					</NuxtLink>
				</li>
				<li>
					<NuxtLink :to="{ name: 'Seller-Product-List' }">
						<Icon name="mdi:basket" class="icon" />
						<span>Products</span>
					</NuxtLink>
				</li>
				<li>
					<NuxtLink :to="{ name: 'Seller-Orders' }">
						<Icon name="mdi:list-box" class="icon" />
						<span>Orders</span>
					</NuxtLink>
				</li>
				<li>
					<NuxtLink :to="{ name: 'Seller-Queries' }">
						<Icon name="mdi:message-bulleted" class="icon" />
						<span>Product Queries</span>
					</NuxtLink>
				</li>
				<li>
					<NuxtLink :to="{ name: 'Seller-Reviews' }">
						<Icon name="mdi:star-settings" class="icon" />
						<span>Reviews</span>
					</NuxtLink>
				</li>
				<li>
					<NuxtLink :to="{ name: 'Seller-Settings' }">
						<Icon name="mdi:cog" class="icon" />
						<span>Shop Settings</span>
					</NuxtLink>
				</li>
			</ul>
		</div>
	</aside>
</template>
<style scoped>
ul#seller-dash-links li a {
	@apply w-full flex flex-row items-center gap-x-3 px-2 py-2.5 hover:bg-custom rounded cursor-pointer transition duration-200;
}
ul#seller-dash-links li .router-link-exact-active {
	@apply bg-custom;
}

ul#seller-dash-links li .icon {
	@apply text-2xl text-neutral-600;
}
ul#seller-dash-links li span {
	@apply text-neutral-700 text-base font-semibold;
}
ul#seller-dash-links li a:hover .icon,
ul#seller-dash-links li a:hover span {
	@apply text-c-base;
}
ul#seller-dash-links li .router-link-exact-active .icon,
ul#seller-dash-links li .router-link-exact-active span {
	@apply text-c-base;
}
</style>
