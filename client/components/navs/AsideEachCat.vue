<template>
	<aside class="w-full flex flex-col py-2 px-0">
		<div class="w-full flex flex-col gap-y-2">
			<div class="py-3 px-1 flex items-center border-b border-neutral-200 dark:border-neutral-700">
				<h4 class="text-lg font-semibold dark:text-c-mode">Categories</h4>
			</div>
			<ul class="w-full flex flex-col">
				<li class="w-full flex flex-row gap-x-2 items-center py-1.5">
					<NuxtLink :to="{ name: 'Products' }" class="w-full flex flex-row gap-x-2 items-center">
						<Icon name="mdi:chevron-left" class="text-lg dark:text-c-mode" />
						<span class="text-neutral-700 text-base dark:text-c-mode">All categories</span>
					</NuxtLink>
				</li>
				<li class="w-full flex flex-col py-1.5">
					<div class="w-full flex flex-row gap-x-2 items-center">
						<Icon name="mdi:chevron-down" class="text-lg dark:text-c-mode" />
						<span class="text-neutral-700 font-semibold text-base truncate dark:text-c-mode">{{ $route.params.category }}</span>
					</div>
					<ul class="py-2 pl-6 pr-2 flex flex-col gap-y-1 border-b border-neutral-200 dark:border-neutral-700">
						<li class="text-neutral-700 text-base capitalize truncate py-1.5 dark:text-c-mode">
							<NuxtLink
								:to="{ name: 'Category', params: { category: 'Automobile & Motorcycle' } }"
								class="w-full h-full block"
							>
								Automobile & Motorcycle
							</NuxtLink>
						</li>
						<li class="text-neutral-700 text-base capitalize truncate py-1.5 dark:text-c-mode">
							<NuxtLink
								:to="{ name: 'Category', params: { category: 'Computer & Accessories' } }"
								class="w-full h-full block"
							>
								Computer & Accessories
							</NuxtLink>
						</li>
						<li class="text-neutral-700 text-base capitalize truncate py-1.5 dark:text-c-mode">
							<NuxtLink :to="{ name: 'Category', params: { category: 'Cellphones & Tabs' } }" class="w-full h-full block">
								Cellphones & Tabs
							</NuxtLink>
						</li>
						<li class="text-neutral-700 text-base capitalize truncate py-1.5 dark:text-c-mode">
							<NuxtLink :to="{ name: 'Category', params: { category: 'Beauty, Health & Hair' } }" class="w-full h-full block">
								Beauty, Health & Hair
							</NuxtLink>
						</li>
						<li class="text-neutral-700 text-base capitalize truncate py-1.5 dark:text-c-mode">
							<NuxtLink
								:to="{ name: 'Category', params: { category: 'Women Clothing & Fashion' } }"
								class="w-full h-full block"
							>
								Women Clothing & Fashion
							</NuxtLink>
						</li>
						<li class="text-neutral-700 text-base capitalize truncate py-1.5 dark:text-c-mode">
							<NuxtLink
								:to="{ name: 'Category', params: { category: 'Men Clothing & Fashion' } }"
								class="w-full h-full block"
							>
								Men Clothing & Fashion
							</NuxtLink>
						</li>
						<li class="text-neutral-700 text-base capitalize truncate py-1.5 dark:text-c-mode">
							<NuxtLink :to="{ name: 'Category', params: { category: 'Sports & Outdoor' } }" class="w-full h-full block"
								>Sports & Outdoor</NuxtLink
							>
						</li>
					</ul>
				</li>
			</ul>
		</div>
		<div class="w-full flex flex-col gap-y-1">
			<div class="py-3 px-1 flex items-center border-neutral-200 dark:border-neutral-700">
				<h4 class="text-lg font-semibold">Price</h4>
			</div>
			<div
				class="w-full pl-1 pr-3 flex flex-row justify-between gap-x-3 items-center border-b border-neutral-200 pb-4 dark:border-neutral-700"
			>
				<div class="relative">
					<input
						type="text"
						id="min"
						class="block px-2.5 py-2 w-full text-sm text-gray-900 bg-transparent rounded-lg border border-gray-300 appearance-none dark:text-white dark:border-gray-600 dark:focus:border-custom focus:outline-none focus:ring-0 focus:border-custom peer"
						placeholder=" "
					/>
					<label
						for="min"
						class="absolute text-sm text-gray-500 dark:text-gray-400 duration-300 transform -translate-y-4 scale-75 top-2 z-10 origin-[0] bg-white dark:bg-gray-900 px-2 peer-focus:px-2 peer-focus:text-custom peer-focus:dark:text-custom peer-placeholder-shown:scale-100 peer-placeholder-shown:-translate-y-1/2 peer-placeholder-shown:top-1/2 peer-focus:top-2 peer-focus:scale-75 peer-focus:-translate-y-4 left-1"
						>Min</label
					>
				</div>
				<div class="relative">
					<input
						type="text"
						id="max"
						class="block px-2.5 py-2 w-full text-sm text-gray-900 bg-transparent rounded-lg border border-gray-300 appearance-none dark:text-white dark:border-gray-600 dark:focus:border-custom focus:outline-none focus:ring-0 focus:border-custom peer"
						placeholder=" "
					/>
					<label
						for="max"
						class="absolute text-sm text-gray-500 dark:text-gray-400 duration-300 transform -translate-y-4 scale-75 top-2 z-10 origin-[0] bg-white dark:bg-gray-900 px-2 peer-focus:px-2 peer-focus:text-custom peer-focus:dark:text-custom peer-placeholder-shown:scale-100 peer-placeholder-shown:-translate-y-1/2 peer-placeholder-shown:top-1/2 peer-focus:top-2 peer-focus:scale-75 peer-focus:-translate-y-4 left-1"
						>Max</label
					>
				</div>
				<button class="bg-custom px-3.5 py-2 text-sm font-semibold tracking-wide text-white rounded">Go</button>
			</div>
		</div>
		<div class="w-full flex flex-col gap-y-1 border-b border-neutral-200 dark:border-neutral-700">
			<div class="py-3 px-1 flex items-center border-neutral-200">
				<h4 class="text-lg font-semibold dark:text-c-mode">Brands</h4>
			</div>
			<ul class="flex flex-col gap-y-1 w-full px-1">
				<li class="text-neutral-700 flex items-center flex-row gap-x-1.5 py-1">
					<ListCheckListItem :item-name="'Audi'" />
				</li>
				<li class="text-neutral-700 flex items-center flex-row gap-x-1.5 py-1">
					<ListCheckListItem :item-name="'LOUIS VUITTON'" />
				</li>
				<li class="text-neutral-700 flex items-center flex-row gap-x-1.5 py-1">
					<ListCheckListItem :item-name="'Adidas'" />
				</li>
			</ul>
			<div class="px-1 py-2">
				<span class="text-sm text-custom">Show more</span>
			</div>
		</div>
		<div class="w-full flex flex-col gap-y-1 border-b border-neutral-200 dark:border-neutral-700">
			<div class="py-3 px-1 flex items-center border-neutral-200">
				<h4 class="text-lg font-semibold dark:text-c-mode">Size</h4>
			</div>
			<ul class="flex flex-col gap-y-1 w-full px-1">
				<li class="text-neutral-700 flex items-center flex-row gap-x-1.5 py-1">
					<ListCheckListItem :item-name="'Small'" />
				</li>
				<li class="text-neutral-700 flex items-center flex-row gap-x-1.5 py-1">
					<ListCheckListItem :item-name="'Medium'" />
				</li>
				<li class="text-neutral-700 flex items-center flex-row gap-x-1.5 py-1">
					<ListCheckListItem :item-name="'Large'" />
				</li>
			</ul>
			<div class="px-1 py-2">
				<span class="text-sm text-custom">Show more</span>
			</div>
		</div>
		<div class="w-full flex flex-col gap-y-1 border-b border-neutral-200 dark:border-neutral-700">
			<div class="py-3 px-1 flex items-center border-neutral-200">
				<h4 class="text-lg font-semibold dark:text-c-mode">Color</h4>
			</div>
			<ul class="flex flex-col gap-y-1 w-full px-1">
				<li class="text-neutral-700 flex items-center flex-row gap-x-1.5 py-1">
					<ListCheckListItem :item-name="'Black'" />
				</li>
				<li class="text-neutral-700 flex items-center flex-row gap-x-1.5 py-1">
					<ListCheckListItem :item-name="'White'" />
				</li>
				<li class="text-neutral-700 flex items-center flex-row gap-x-1.5 py-1">
					<ListCheckListItem :item-name="'Blue'" />
				</li>
			</ul>
			<div class="px-1 py-2">
				<span class="text-sm text-custom">Show more</span>
			</div>
		</div>
		<div class="w-full flex flex-col gap-y-1 border-b border-neutral-200 dark:border-neutral-700">
			<div class="py-3 px-1 flex items-center border-neutral-200">
				<h4 class="text-lg font-semibold dark:text-c-mode">Memory</h4>
			</div>
			<ul class="flex flex-col gap-y-1 w-full px-1">
				<li class="text-neutral-700 flex items-center flex-row gap-x-1.5 py-1">
					<ListCheckListItem :item-name="'32GB'" />
				</li>
				<li class="text-neutral-700 flex items-center flex-row gap-x-1.5 py-1">
					<ListCheckListItem :item-name="'64GB'" />
				</li>
				<li class="text-neutral-700 flex items-center flex-row gap-x-1.5 py-1">
					<ListCheckListItem :item-name="'128GB'" />
				</li>
			</ul>
			<div class="px-1 py-2">
				<span class="text-sm text-custom">Show more</span>
			</div>
		</div>
	</aside>
</template>
