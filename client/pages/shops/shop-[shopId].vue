<template>
	<section class="w-full flex flex-col">
		<div class="hero w-full flex flex-col items-center justify-center relative">
			<NuxtImg src="/shop-1-banner.webp" class="h-auto w-full" />
			<div class="w-full flex flex-col lg:absolute md:bottom-[5%] px-4 md:px-2 lg:px-20 2xl:px-44">
				<div class="w-full bg-c-base/70 px-2 md:px-8 rounded-sm flex flex-col md:grid grid-cols-10">
					<div
						class="col-span-7 lg:col-span-8 w-full sm:w-auto py-4 md:border-r border-custom flex flex-col md:flex-row md:items-center justify-start gap-x-6 gap-y-4"
					>
						<div class="flex items-start justify-start md:items-center md:justify-center">
							<NuxtImg src="/sellers/avatar.png" loading="lazy" class="w-20 sm:w-24 h-20 sm:h-24 rounded-full" />
						</div>
						<div class="flex flex-col gap-y-2">
							<h3 class="text-2xl capitalize tracking-wide leading-tight font-bold">Beauty Shop</h3>
							<p class="text-sm text-neutral-700 leading-tight">
								Cellphones & Tabs, Women Clothing & Fashion, Beauty, Health & Hair, Men Clothing & Fashion, Baby & Kids
							</p>
						</div>
					</div>
					<div class="col-span-3 lg:col-span-2 px-0 md:px-4 py-3 sm:py-6 mb-2 sm:mb-0">
						<div class="w-full h-full flex flex-col gap-y-1 justify-center items-start">
							<p class="text-base">Ratings</p>
							<ContentsRatings />
						</div>
					</div>
				</div>
			</div>
		</div>
		<div class="w-full flex flex-col py-4 px-4 md:px-8 lg:px-20 2xl:px-44 bg-c-dark">
			<div id="shop-links" class="w-full flex flex-row gap-x-8 md:gap-x-12 items-center justify-start">
				<NuxtLink to="/shops/shop-1" class="text-base tracking-wide text-c-base py-1 px-2">Shop</NuxtLink>
				<NuxtLink to="/shops/shop-2/offers" class="text-base tracking-wide text-c-base py-1 px-2">Offers</NuxtLink>
				<NuxtLink to="/shops/shop-2/products" class="text-base tracking-wide text-c-base py-1 px-2">All Products</NuxtLink>
			</div>
		</div>
		<div class="w-full flex flex-col px-4 md:px-8 lg:px-20 2xl:px-44 py-4">
			<NuxtPage />
		</div>
	</section>
</template>

<style scoped>
#shop-links a.router-link-exact-active {
	@apply text-custom;
}

#shop-links a.router-link-exact-active {
	background-image: linear-gradient(#dd9933, #dd9933);
	background-position: 0% 100%;
	background-repeat: no-repeat;
	background-size: 100% 2px;
	transition: background-size 0.2s, padding 0.2s;
}

#shop-links a {
	@apply pr-3 cursor-pointer;
	background-image: linear-gradient(#dd9933, #dd9933);
	background-position: 0% 100%;
	background-repeat: no-repeat;
	background-size: 0% 2px;
	transition: background-size 0.2s, padding 0.2s;
}

#shop-links a:hover {
	background-size: 100% 2px;
}
</style>
