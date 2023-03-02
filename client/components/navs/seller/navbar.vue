<template>
	<nav class="w-full flex flex-col">
		<div class="w-full grid grid-cols-2 items-center justify-between px-12 py-3 border-b border-neutral-200">
			<div class="left grid grid-cols-3 gap-x-0 items-center">
				<NuxtLink :to="{ name: 'Seller-Home' }" class="flex flex-row items-center">
					<NuxtImg src="/logo.png" class="mr-3 max-h-[2.2rem] sm:max-h-[2.6rem] rounded-lg shadow opacity-90" />
					<small class="text-xl sm:text-2xl tracking-wide font-bold dark:text-c-mode"
						><span class="text-custom">S</span>hop</small
					>
				</NuxtLink>
				<div class="actions col-span-2 flex flex-row items-center gap-x-4">
					<button
						class="px-4 py-2 text-base font-medium text-neutral-700 flex flex-row gap-x-2 items-center border border-gray-200 rounded"
					>
						<div class="w-4 h-4">
							<IconsPlus />
						</div>
						<span>Add New Products</span>
					</button>
					<button
						class="px-4 py-2 text-base font-medium text-neutral-700 flex flex-row gap-x-2 items-center border border-gray-200 rounded"
					>
						<div class="w-4 h-4">
							<IconsWebsite />
						</div>
						<span>Browse Website</span>
					</button>
				</div>
			</div>
			<div class="right flex flex-row items-center justify-end gap-x-20">
				<div class="seller-details flex gap-x-3">
					<div class="flex flex-col">
						<span class="text-base font-medium leading-tight">Amos Kip</span>
						<small class="text-sm text-neutral-500 leading-tight">Seller</small>
					</div>
					<button class="flex flex-row items-center gap-x-0.5">
						<div class="relative">
							<NuxtImg src="/icons/male.png" class="w-9 h-9 rounded-full ring-1 ring-neutral-200" />
							<span class="top-0 left-7 absolute w-3.5 h-3.5 bg-green-400 dark:border-gray-800 rounded-full"></span>
						</div>
						<div class="w-4 h-4 text-gray-800">
							<IconsCaretDown />
						</div>
					</button>
				</div>
			</div>
		</div>
	</nav>
</template>
