<template>
	<div class="flex flex-col gap-y-0 ring-1 ring-neutral-200 rounded">
		<div class="w-full flex flex-col">
			<NuxtImg src="/shop-1-banner.webp" class="h-[150px] w-full rounded-t" />
		</div>
		<div class="w-full flex flex-col h-full gap-y-4">
			<div class="w-full flex flex-row items-center justify-center relative">
				<NuxtImg
					src="/sellers/avatar.png"
					loading="lazy"
					class="w-24 h-24 rounded-full shadow-md ring-2 ring-white absolute top-0 -translate-y-1/2"
				/>
			</div>
			<div class="w-full flex flex-col gap-y-2.5 items-center h-full justify-between mt-10 px-4 py-4">
				<div class="">
					<h3 class="text-2xl font-semibold capitalize truncate">Beauty Shop</h3>
				</div>
				<div class="flex flex-row">
					<p class="text-neutral-600 text-sm font-light line-clamp-2 text-center">
						Cellphones & Tabs, Women Clothing & Fashion, Beauty, Health & Hair, Men Clothing & Fashion
					</p>
				</div>
				<div class="flex flex-row items-center justify-center gap-x-1 text-neutral-700 dark:text-c-mode">
					<small class="text-sm font-light">4.0</small>
					<div class="flex flex-row gap-x-0.5 items-center">
						<button class="w-4 h-4 text-yellow-400">
							<IconsStar />
						</button>
						<button class="w-4 h-4 text-yellow-400">
							<IconsStar /></button
						><button class="w-4 h-4 text-yellow-400">
							<IconsStar /></button
						><button class="w-4 h-4 text-yellow-400">
							<IconsStar /></button
						><button class="w-4 h-4 text-gray-300">
							<IconsStar />
						</button>
					</div>
					<small class="text-sm font-light truncate">(10 Ratings)</small>
				</div>
				<div class="flex flex-col gap-y-0.5 items-center justify-center">
					<p class="text-neutral-600 text-sm font-light text-center">Shop since 17 Jan, 2022</p>
					<p class="text-neutral-600 text-sm font-light text-center">Total Products 181</p>
				</div>
				<div class="flex flex-row items-center mt-2">
					<button class="bg-[#212121] px-4 py-2.5 rounded tracking-wide text-sm font-semibold text-gray-100">Visit Store</button>
				</div>
			</div>
		</div>
	</div>
</template>
