<template>
	<div class="w-full flex flex-col">
		<div class="grid grid-cols-10 gap-x-5">
			<div class="col-span-3 lg:col-span-2 hidden md:flex flex-col gap-y-2.5 bg-white rounded py-2 dark:bg-[#212121] shadow">
				<div
					class="w-full flex flex-row items-center gap-x-2 px-2.5 py-1 text-gray-900 border-b border-neutral-200 dark:border-neutral-700 dark:text-c-base"
				>
					<div class="">
						<Icon name="mdi:format-list-bulleted-square" class="text-2xl text-neutral-600 dark:text-neutral-300" />
					</div>
					<p class="font-semibold text-base lg:text-lg">Categories</p>
				</div>
				<ul class="w-full flex flex-col gap-y-1">
					<li
						class="w-full flex flex-row items-center gap-x-2 py-1.5 px-2.5 text-neutral-500 cursor-pointer hover:bg-neutral-200 rounded transition duration-200 dark:text-neutral-400 dark:hover:bg-neutral-700"
					>
						<Icon name="mdi:cellphone" class="w-4 lg:w-5 h-4 lg:h-5" />
						<span class="truncate text-sm lg:text-base text-neutral-700 dark:text-c-mode">Phone's & Tablets</span>
					</li>
					<li
						class="w-full flex flex-row items-center gap-x-2 py-1.5 px-2.5 text-neutral-500 cursor-pointer hover:bg-neutral-200 rounded transition duration-200 dark:text-neutral-400 dark:hover:bg-neutral-700"
					>
						<Icon name="uil:monitor" class="w-4 lg:w-5 h-4 lg:h-5" />
						<span class="truncate text-sm lg:text-base text-neutral-700 dark:text-c-mode">Laptops & Computers</span>
					</li>
					<li
						class="w-full flex flex-row items-center gap-x-2 py-1.5 px-2.5 text-neutral-500 cursor-pointer hover:bg-neutral-200 rounded transition duration-200 dark:text-neutral-400 dark:hover:bg-neutral-700"
					>
						<Icon name="mdi:speaker-wireless" class="w-4 lg:w-5 h-4 lg:h-5" />
						<span class="truncate text-sm lg:text-base text-neutral-700 dark:text-c-mode">Speakers & Electronics</span>
					</li>
					<li
						class="w-full flex flex-row items-center gap-x-2 py-1.5 px-2.5 text-neutral-500 cursor-pointer hover:bg-neutral-200 rounded transition duration-200 dark:text-neutral-400 dark:hover:bg-neutral-700"
					>
						<Icon name="mdi:face-woman-outline" class="w-4 lg:w-5 h-4 lg:h-5" />
						<span class="truncate text-sm lg:text-base text-neutral-700 dark:text-c-mode">Health & Beauty</span>
					</li>
					<li
						class="w-full flex flex-row items-center gap-x-2 py-1.5 px-2.5 text-neutral-500 cursor-pointer hover:bg-neutral-200 rounded transition duration-200 dark:text-neutral-400 dark:hover:bg-neutral-700"
					>
						<Icon name="mdi:man" class="w-4 lg:w-5 h-4 lg:h-5" />
						<span class="truncate text-sm lg:text-base text-neutral-700 dark:text-c-mode">Mens Clothings</span>
					</li>
					<li
						class="w-full flex flex-row items-center gap-x-2 py-1.5 px-2.5 text-neutral-500 cursor-pointer hover:bg-neutral-200 rounded transition duration-200 dark:text-neutral-400 dark:hover:bg-neutral-700"
					>
						<Icon name="mdi:woman" class="w-4 lg:w-5 h-4 lg:h-5" />
						<span class="truncate text-sm lg:text-base text-neutral-700 dark:text-c-mode">Women's Clothings</span>
					</li>
					<li
						class="w-full flex flex-row items-center gap-x-2 py-1.5 px-2.5 text-neutral-500 cursor-pointer hover:bg-neutral-200 rounded transition duration-200 dark:text-neutral-400 dark:hover:bg-neutral-700"
					>
						<Icon name="mdi:shoe-sneaker" class="w-4 lg:w-5 h-4 lg:h-5" />
						<span class="truncate text-sm lg:text-base text-neutral-700 dark:text-c-mode">Bags and Shoes</span>
					</li>
				</ul>
			</div>
			<div class="col-span-10 md:col-span-7 lg:col-span-6 flex flex-row justify-center rounded-md">
				<NuxtImg src="/slides/slide-1.webp" class="cursor-pointer w-[96%] md:w-full rounded-md" alt="" />
			</div>
			<div class="col-span-2 hidden lg:grid grid-cols-1 grid-rows-2 gap-y-2 bg-white px-0 py-2 rounded shadow dark:bg-alt-dark">
				<div class="w-full">
					<div
						class="bg-white border-b border-neutral-100 flex flex-col gap-y-4 py-3 px-2.5 dark:bg-[#212121] dark:text-c-mode dark:border-neutral-700"
					>
						<div class="flex flex-row gap-x-1.5 items-center cursor-pointer">
							<div class="px-0.5">
								<Icon name="mdi:account-multiple" class="text-custom text-4xl" />
							</div>
							<div class="flex flex-col">
								<h5 class="text-sm lg:text-sm font-semibold line-clamp-1 uppercase leading-tight">Help Center</h5>
								<p class="text-xs lg:text-sm line-clamp-1 leading-tight">Guide To Customer Care</p>
							</div>
						</div>
						<div class="flex flex-row gap-x-1.5 items-center cursor-pointer">
							<div class="px-0.5">
								<Icon name="mdi:security" class="text-custom text-4xl" />
							</div>
							<div class="flex flex-col">
								<h5 class="text-sm lg:text-sm font-semibold line-clamp-1 uppercase leading-tight">Shop With confidence</h5>
								<p class="text-xs lg:text-sm line-clamp-1 leading-tight">Buyer Protection policy</p>
							</div>
						</div>
						<div class="flex flex-row gap-x-1.5 items-center cursor-pointer">
							<div class="px-0.5">
								<Icon name="mdi:currency-usd" class="text-custom text-4xl" />
							</div>
							<div class="flex flex-col">
								<h5 class="text-sm lg:text-sm font-semibold line-clamp-1 uppercase leading-tight">Sell on Shop</h5>
								<p class="text-xs lg:text-sm line-clamp-1 leading-tight">Thousands Of Visitors</p>
							</div>
						</div>
					</div>
				</div>
				<div class="w-full px-3">
					<div class="w-full flex items-center justify-end">
						<NuxtImg src="/slides/21.webp" class="h-full cursor-pointer rounded-md" alt="" />
					</div>
				</div>
			</div>
		</div>
	</div>
</template>
