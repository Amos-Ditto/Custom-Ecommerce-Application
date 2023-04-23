<template>
	<aside class="w-full flex flex-col py-2">
		<div class="w-full flex flex-col gap-y-2">
			<div class="py-3 px-1 flex items-center border-b border-neutral-200 dark:border-neutral-700">
				<h4 class="text-lg font-semibold dark:text-c-mode">Categories</h4>
			</div>
			<ul class="py-2 px-1 flex flex-col gap-y-1 border-b border-neutral-200 dark:border-neutral-700">
				<li class="text-neutral-700 text-base capitalize truncate py-1.5 dark:text-c-mode">
					<NuxtLink :to="{ name: 'Category', params: { category: 'Automobile & Motorcycle' } }" class="w-full h-full block">
						Automobile & Motorcycle
					</NuxtLink>
				</li>
				<li class="text-neutral-700 text-base capitalize truncate py-1.5 dark:text-c-mode">
					<NuxtLink :to="{ name: 'Category', params: { category: 'Computer & Accessories' } }" class="w-full h-full block">
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
					<NuxtLink :to="{ name: 'Category', params: { category: 'Women Clothing & Fashion' } }" class="w-full h-full block">
						Women Clothing & Fashion
					</NuxtLink>
				</li>
				<li class="text-neutral-700 text-base capitalize truncate py-1.5 dark:text-c-mode">
					<NuxtLink :to="{ name: 'Category', params: { category: 'Men Clothing & Fashion' } }" class="w-full h-full block">
						Men Clothing & Fashion
					</NuxtLink>
				</li>
				<li class="text-neutral-700 text-base capitalize truncate py-1.5 dark:text-c-mode">
					<NuxtLink :to="{ name: 'Category', params: { category: 'Sports & Outdoor' } }" class="w-full h-full block"
						>Sports & Outdoor</NuxtLink
					>
				</li>
			</ul>
		</div>
		<div class="w-full flex flex-col gap-y-1">
			<div class="py-3 px-1 flex items-center border-neutral-200 dark:border-neutral-700">
				<h4 class="text-lg font-semibold dark:text-c-mode">Price</h4>
			</div>
			<div class="w-full flex flex-row justify-between gap-x-3 items-center border-b border-neutral-200 pb-4 dark:border-neutral-700">
				<input
					type="text"
					name="min"
					id="min"
					class="w-full py-2 px-2 border border-neutral-200 rounded text-sm focus:outline-none focus:ring-1 ring-custom focus:border-transparent transition duration-200"
					placeholder="min price"
				/>
				<small class="text-sm text-neutral-600">to</small>
				<input
					type="text"
					name="max"
					id="max"
					class="w-full py-2 px-2 border border-neutral-200 rounded text-sm focus:outline-none focus:ring-1 ring-custom focus:border-transparent transition duration-200"
					placeholder="max price"
				/>
				<button class="bg-custom px-2.5 py-2 text-sm font-semibold tracking-wide text-white rounded">Go</button>
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
