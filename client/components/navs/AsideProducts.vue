<template>
	<aside class="w-full flex flex-col py-2 px-4">
		<div class="w-full flex flex-col gap-y-2">
			<div class="py-3 px-1 flex items-center border-b border-neutral-200">
				<h4 class="text-lg font-semibold">Categories</h4>
			</div>
			<ul class="py-2 px-1 flex flex-col gap-y-1 border-b border-neutral-200">
				<li class="text-neutral-700 text-base capitalize truncate py-1.5">
					<NuxtLink :to="{ name: 'Category', params: { category: 'Automobile & Motorcycle' } }" class="w-full h-full block">
						Automobile & Motorcycle
					</NuxtLink>
				</li>
				<li class="text-neutral-700 text-base capitalize truncate py-1.5">
					<NuxtLink :to="{ name: 'Category', params: { category: 'Computer & Accessories' } }" class="w-full h-full block">
						Computer & Accessories
					</NuxtLink>
				</li>
				<li class="text-neutral-700 text-base capitalize truncate py-1.5">
					<NuxtLink :to="{ name: 'Category', params: { category: 'Cellphones & Tabs' } }" class="w-full h-full block">
						Cellphones & Tabs
					</NuxtLink>
				</li>
				<li class="text-neutral-700 text-base capitalize truncate py-1.5">
					<NuxtLink :to="{ name: 'Category', params: { category: 'Beauty, Health & Hair' } }" class="w-full h-full block">
						Beauty, Health & Hair
					</NuxtLink>
				</li>
				<li class="text-neutral-700 text-base capitalize truncate py-1.5">
					<NuxtLink :to="{ name: 'Category', params: { category: 'Women Clothing & Fashion' } }" class="w-full h-full block">
						Women Clothing & Fashion
					</NuxtLink>
				</li>
				<li class="text-neutral-700 text-base capitalize truncate py-1.5">
					<NuxtLink :to="{ name: 'Category', params: { category: 'Men Clothing & Fashion' } }" class="w-full h-full block">
						Men Clothing & Fashion
					</NuxtLink>
				</li>
				<li class="text-neutral-700 text-base capitalize truncate py-1.5">
					<NuxtLink :to="{ name: 'Category', params: { category: 'Sports & Outdoor' } }" class="w-full h-full block"
						>Sports & Outdoor</NuxtLink
					>
				</li>
			</ul>
		</div>
		<div class="w-full flex flex-col gap-y-1">
			<div class="py-3 px-1 flex items-center border-neutral-200">
				<h4 class="text-lg font-semibold">Price</h4>
			</div>
			<div class="w-full flex flex-row justify-between gap-x-3 items-center border-b border-neutral-200 pb-4">
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
		<div class="w-full flex flex-col gap-y-1 border-b border-neutral-200">
			<div class="py-3 px-1 flex items-center border-neutral-200">
				<h4 class="text-lg font-semibold">Brands</h4>
			</div>
			<ul class="flex flex-col gap-y-1 w-full px-1">
				<li class="text-neutral-700 flex items-center flex-row gap-x-1.5 py-1">
					<input
						id="default-checkbox"
						type="checkbox"
						value=""
						class="w-4 h-4 text-blue-600 bg-gray-100 border-gray-300 rounded focus:ring-blue-500 dark:focus:ring-blue-600 dark:ring-offset-gray-800 focus:ring-2 dark:bg-gray-700 dark:border-gray-600"
					/>
					<label for="default-checkbox" class="ml-2 text-sm text-neutral-700 dark:text-gray-300">Audi</label>
				</li>
				<li class="text-neutral-700 flex items-center flex-row gap-x-1.5 py-1">
					<input
						id="default-checkbox"
						type="checkbox"
						value=""
						class="w-4 h-4 text-blue-600 bg-gray-100 border-gray-300 rounded focus:ring-blue-500 dark:focus:ring-blue-600 dark:ring-offset-gray-800 focus:ring-2 dark:bg-gray-700 dark:border-gray-600"
					/>
					<label for="default-checkbox" class="ml-2 text-sm text-neutral-700 dark:text-gray-300">LOUIS VUITTON</label>
				</li>
				<li class="text-neutral-700 flex items-center flex-row gap-x-1.5 py-1">
					<input
						id="default-checkbox"
						type="checkbox"
						value=""
						class="w-4 h-4 text-blue-600 bg-gray-100 border-gray-300 rounded focus:ring-blue-500 dark:focus:ring-blue-600 dark:ring-offset-gray-800 focus:ring-2 dark:bg-gray-700 dark:border-gray-600"
					/>
					<label for="default-checkbox" class="ml-2 text-sm text-neutral-700 dark:text-gray-300">Adidas</label>
				</li>
			</ul>
			<div class="px-1 py-2">
				<span class="text-sm text-custom font-bold tracking-tight">Show more</span>
			</div>
		</div>
		<div class="w-full flex flex-col gap-y-1 border-b border-neutral-200">
			<div class="py-3 px-1 flex items-center border-neutral-200">
				<h4 class="text-lg font-semibold">Size</h4>
			</div>
			<ul class="flex flex-col gap-y-1 w-full px-1">
				<li class="text-neutral-700 flex items-center flex-row gap-x-1.5 py-1">
					<input
						id="default-checkbox"
						type="checkbox"
						value=""
						class="w-4 h-4 text-blue-600 bg-gray-100 border-gray-300 rounded focus:ring-blue-500 dark:focus:ring-blue-600 dark:ring-offset-gray-800 focus:ring-2 dark:bg-gray-700 dark:border-gray-600"
					/>
					<label for="default-checkbox" class="ml-2 text-sm text-neutral-700 dark:text-gray-300">Small</label>
				</li>
				<li class="text-neutral-700 flex items-center flex-row gap-x-1.5 py-1">
					<input
						id="default-checkbox"
						type="checkbox"
						value=""
						class="w-4 h-4 text-blue-600 bg-gray-100 border-gray-300 rounded focus:ring-blue-500 dark:focus:ring-blue-600 dark:ring-offset-gray-800 focus:ring-2 dark:bg-gray-700 dark:border-gray-600"
					/>
					<label for="default-checkbox" class="ml-2 text-sm text-neutral-700 dark:text-gray-300">Medium</label>
				</li>
				<li class="text-neutral-700 flex items-center flex-row gap-x-1.5 py-1">
					<input
						id="default-checkbox"
						type="checkbox"
						value=""
						class="w-4 h-4 text-blue-600 bg-gray-100 border-gray-300 rounded focus:ring-blue-500 dark:focus:ring-blue-600 dark:ring-offset-gray-800 focus:ring-2 dark:bg-gray-700 dark:border-gray-600"
					/>
					<label for="default-checkbox" class="ml-2 text-sm text-neutral-700 dark:text-gray-300">Large</label>
				</li>
			</ul>
			<div class="px-1 py-2">
				<span class="text-sm text-custom font-bold tracking-tight">Show more</span>
			</div>
		</div>
		<div class="w-full flex flex-col gap-y-1 border-b border-neutral-200">
			<div class="py-3 px-1 flex items-center border-neutral-200">
				<h4 class="text-lg font-semibold">Color</h4>
			</div>
			<ul class="flex flex-col gap-y-1 w-full px-1">
				<li class="text-neutral-700 flex items-center flex-row gap-x-1.5 py-1">
					<input
						id="default-checkbox"
						type="checkbox"
						value=""
						class="w-4 h-4 text-blue-600 bg-gray-100 border-gray-300 rounded focus:ring-blue-500 dark:focus:ring-blue-600 dark:ring-offset-gray-800 focus:ring-2 dark:bg-gray-700 dark:border-gray-600"
					/>
					<label for="default-checkbox" class="ml-2 text-sm text-neutral-700 dark:text-gray-300">Black</label>
				</li>
				<li class="text-neutral-700 flex items-center flex-row gap-x-1.5 py-1">
					<input
						id="default-checkbox"
						type="checkbox"
						value=""
						class="w-4 h-4 text-blue-600 bg-gray-100 border-gray-300 rounded focus:ring-blue-500 dark:focus:ring-blue-600 dark:ring-offset-gray-800 focus:ring-2 dark:bg-gray-700 dark:border-gray-600"
					/>
					<label for="default-checkbox" class="ml-2 text-sm text-neutral-700 dark:text-gray-300">White</label>
				</li>
				<li class="text-neutral-700 flex items-center flex-row gap-x-1.5 py-1">
					<input
						id="default-checkbox"
						type="checkbox"
						value=""
						class="w-4 h-4 text-blue-600 bg-gray-100 border-gray-300 rounded focus:ring-blue-500 dark:focus:ring-blue-600 dark:ring-offset-gray-800 focus:ring-2 dark:bg-gray-700 dark:border-gray-600"
					/>
					<label for="default-checkbox" class="ml-2 text-sm text-neutral-700 dark:text-gray-300">Blue</label>
				</li>
			</ul>
			<div class="px-1 py-2">
				<span class="text-sm text-custom font-bold tracking-tight">Show more</span>
			</div>
		</div>
		<div class="w-full flex flex-col gap-y-1 border-b border-neutral-200">
			<div class="py-3 px-1 flex items-center border-neutral-200">
				<h4 class="text-lg font-semibold">Memory</h4>
			</div>
			<ul class="flex flex-col gap-y-1 w-full px-1">
				<li class="text-neutral-700 flex items-center flex-row gap-x-1.5 py-1">
					<input
						id="default-checkbox"
						type="checkbox"
						value=""
						class="w-4 h-4 text-blue-600 bg-gray-100 border-gray-300 rounded focus:ring-blue-500 dark:focus:ring-blue-600 dark:ring-offset-gray-800 focus:ring-2 dark:bg-gray-700 dark:border-gray-600"
					/>
					<label for="default-checkbox" class="ml-2 text-sm text-neutral-700 dark:text-gray-300">32 gb</label>
				</li>
				<li class="text-neutral-700 flex items-center flex-row gap-x-1.5 py-1">
					<input
						id="default-checkbox"
						type="checkbox"
						value=""
						class="w-4 h-4 text-blue-600 bg-gray-100 border-gray-300 rounded focus:ring-blue-500 dark:focus:ring-blue-600 dark:ring-offset-gray-800 focus:ring-2 dark:bg-gray-700 dark:border-gray-600"
					/>
					<label for="default-checkbox" class="ml-2 text-sm text-neutral-700 dark:text-gray-300">64 gb</label>
				</li>
				<li class="text-neutral-700 flex items-center flex-row gap-x-1.5 py-1">
					<input
						id="default-checkbox"
						type="checkbox"
						value=""
						class="w-4 h-4 text-blue-600 bg-gray-100 border-gray-300 rounded focus:ring-blue-500 dark:focus:ring-blue-600 dark:ring-offset-gray-800 focus:ring-2 dark:bg-gray-700 dark:border-gray-600"
					/>
					<label for="default-checkbox" class="ml-2 text-sm text-neutral-700 dark:text-gray-300">128 gb</label>
				</li>
			</ul>
			<div class="px-1 py-2">
				<span class="text-sm text-custom font-bold tracking-tight">Show more</span>
			</div>
		</div>
	</aside>
</template>
