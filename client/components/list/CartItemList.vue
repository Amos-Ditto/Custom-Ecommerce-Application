<script setup lang="ts"></script>
<template>
	<li class="w-full flex flex-col px-2">
		<div class="w-full px-1 py-3 border-b flex flex-row items-center justify-between relative dark:border-neutral-600">
			<div class="flex flex-row items-center gap-x-2">
				<ListCheckListItem :item-name="''" />
				<div class="ml-2">
					<NuxtImg src="/sellers/avatar.png" class="w-10 h-10 rounded-full" />
				</div>
				<div class="flex flex-col gap-y-0">
					<h3 class="text-lg font-semibold">The Shop</h3>
					<span class="text-neutral-700 text-sm"> <span class="text-xs">KES</span> 900.80</span>
				</div>
			</div>
			<button class="py-1 px-2"><Icon name="mdi:chevron-down" class="text-lg" /></button>
		</div>
		<ul class="nest-list w-full flex flex-col pl-4 pr-1">
			<li class="border-b grid grid-cols-9 gap-x-1 items-center px-1 py-1 dark:border-neutral-600">
				<ListCheckListItem :item-name="''" />
				<div class="col-span-2 items-center flex justify-center">
					<NuxtImg src="/items/phone.png" class="w-full rounded" />
				</div>
				<div class="col-span-5 items-start flex justify-start flex-col gap-y-1">
					<span class="line-clamp-1 text-sm"> Asus ROG Phone 5 Dual Sim s888 Phantom </span>
					<div class="w-full grid grid-cols-2 items-center">
						<span class="text-sm font-semibold truncate"> <span class="text-xs font-normal">KES</span> 134.80</span>
						<div class="relative w-full z-0">
							<button
								class="flex items-center z-10 absolute left-0 top-0 bottom-0 px-1 py-0.5 text-neutral-600 border-r border-neutral-200 rounded-l hover:text-custom focus:text-custom transition duration-200 dark:border-neutral-600 dark:hover:text-custom dark:text-neutral-100"
							>
								<Icon name="mdi:minus" class="text-base" />
							</button>
							<input
								type="number"
								name="quantity"
								id="quantity"
								class="bg-inherit border border-neutral-200 rounded py-0.5 text-sm text-center w-full outline-none hover:border-custom focus:border-custom transition duration-200 dark:bg-inherit dark:border-neutral-600 dark:text-neutral-100 dark:hover:border-custom dark:focus:border-custom"
								value="1"
								min="1"
							/>
							<button
								class="flex items-center z-10 absolute right-0 top-0 bottom-0 px-1 py-0.5 text-neutral-600 border-l border-neutral-200 hover:text-custom focus:text-custom transition duration-200 dark:border-neutral-600 dark:hover:text-custom dark:text-neutral-100"
							>
								<Icon name="mdi:plus" class="text-base" />
							</button>
						</div>
					</div>
				</div>
				<div class="flex h-full items-center justify-end">
					<button>
						<Icon name="mdi:trash-can-outline" class="text-lg text-neutral-600 dark:text-neutral-300" />
					</button>
				</div>
			</li>
		</ul>
	</li>
</template>

<style scoped>
input[type="number"]::-webkit-inner-spin-button,
input[type="number"]::-webkit-outer-spin-button {
	-webkit-appearance: none;
	margin: 0;
}
</style>
