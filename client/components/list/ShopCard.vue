<template>
	<div
		class="ring-1 ring-neutral-300 rounded-sm sm:rounded px-3 py-3 grid grid-cols-1 lg:grid-cols-2 justify-between gap-x-4 gap-y-4 dark:ring-neutral-700"
	>
		<div class="flex flex-col h-full justify-between gap-y-2">
			<div class="w-full flex items-center justify-center">
				<NuxtImg src="/sellers/avatar.png" loading="lazy" class="w-[36%] sm:w-1/4 lg:w-1/2 rounded-full shadow" />
			</div>
			<div class="flex flex-row p-1 sm:p-2 w-full items-center justify-center">
				<h4 class="text-xl font-semibold capitalize text-center dark:text-c-mode">Beauty shop</h4>
			</div>
			<div class="w-full flex flex-col">
				<ContentsRatings />
			</div>
			<div class="w-full flex flex-col items-center mt-1">
				<button
					class="w-full bg-yellow-100 text-yellow-800 text-sm font-medium px-3.5 py-1.5 rounded dark:bg-inherit dark:text-yellow-300 border border-yellow-300"
				>
					Visit Shop
				</button>
			</div>
		</div>
		<div class="h-full grid grid-cols-1 grid-rows-3 gap-y-2.5">
			<div
				class="grid grid-cols-2 lg:grid-cols-1 xl:grid-cols-2 gap-x-1 items-center justify-center ring-1 ring-neutral-200 rounded-sm sm:rounded px-1 py-1 dark:ring-neutral-800"
			>
				<div class="col-span-1 flex items-center justify-center">
					<NuxtImg src="/items/phone.png" class="max-h-14 lg:max-h-16 rounded" />
				</div>
				<div class="flex lg:hidden xl:flex flex-col gap-y-2">
					<p class="text-xs truncate dark:text-c-mode">Asus ROG Phone 5 Dual Sim s888 Phantom</p>
					<span class="text-sm sm:text-base font-semibold dark:text-c-mode truncate">$19.57</span>
				</div>
			</div>
			<div
				class="grid grid-cols-2 lg:grid-cols-1 xl:grid-cols-2 gap-x-1 items-center justify-center ring-1 ring-neutral-200 rounded-sm sm:rounded px-1 py-1 dark:ring-neutral-800"
			>
				<div class="col-span-1 flex items-center justify-center">
					<NuxtImg src="/items/phone.png" class="max-h-14 lg:max-h-16 rounded" />
				</div>
				<div class="flex lg:hidden xl:flex flex-col gap-y-2">
					<p class="text-xs truncate dark:text-c-mode">Asus ROG Phone 5 Dual Sim s888 Phantom</p>
					<span class="text-sm sm:text-base font-semibold dark:text-c-mode truncate">$19.57</span>
				</div>
			</div>
			<div
				class="grid grid-cols-2 lg:grid-cols-1 xl:grid-cols-2 gap-x-1 items-center justify-center ring-1 ring-neutral-200 rounded-sm sm:rounded px-1 py-1 dark:ring-neutral-800"
			>
				<div class="col-span-1 flex items-center justify-center">
					<NuxtImg src="/items/phone.png" class="max-h-14 lg:max-h-16 rounded" />
				</div>
				<div class="flex lg:hidden xl:flex flex-col gap-y-2">
					<p class="text-xs truncate dark:text-c-mode">Asus ROG Phone 5 Dual Sim s888 Phantom</p>
					<span class="text-sm sm:text-base font-semibold dark:text-c-mode truncate">$19.57</span>
				</div>
			</div>
		</div>
	</div>
</template>
