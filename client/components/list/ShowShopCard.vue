<template>
	<div class="flex flex-col border border-neutral-200 rounded dark:border-neutral-700">
		<NuxtLink to="/shops/shop-1" class="w-full flex flex-col">
			<NuxtImg src="/shop-1-banner.webp" class="h-[150px] object-cover w-full rounded-t" />
		</NuxtLink>
		<div class="w-full flex flex-col h-full gap-y-4">
			<div class="w-full flex flex-row items-center justify-center relative">
				<NuxtImg
					src="/sellers/avatar.png"
					loading="lazy"
					class="w-20 h-20 rounded-full shadow-md ring-1 ring-white absolute top-0 -translate-y-1/2"
				/>
			</div>
			<div class="w-full flex flex-col gap-y-1.5 items-center h-full justify-between mt-5 px-4 py-4">
				<div class="">
					<NuxtLink to="/shops/shop-1" class="text-2xl font-semibold capitalize truncate dark:text-neutral-100"
						>Beauty Shop</NuxtLink
					>
				</div>
				<div class="flex flex-row">
					<p class="text-neutral-600 text-sm line-clamp-2 text-center dark:text-neutral-100">
						Cellphones & Tabs, Women Clothing & Fashion, Beauty, Health & Hair, Men Clothing & Fashion
					</p>
				</div>
				<ContentsRatings />
				<div class="flex flex-col gap-y-0.5 items-center justify-center text-neutral-600 dark:text-neutral-100">
					<p class="text-sm text-center">Shop since 17 Jan, 2022</p>
				</div>
				<div class="flex flex-col w-full mt-2">
					<button
						@click="() => useRouter().push('/shops/shop-1')"
						class="bg-[#212121] px-4 py-2.5 rounded tracking-wide text-sm font-semibold text-gray-100 dark:border-neutral-600 dark:border"
					>
						Visit Store
					</button>
				</div>
			</div>
		</div>
	</div>
</template>
