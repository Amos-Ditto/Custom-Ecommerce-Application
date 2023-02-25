<template>
	<li class="w-full flex flex-col px-4">
		<div class="w-full py-3.5 border-b flex flex-row items-center justify-between relative">
			<div class="flex flex-row items-center gap-x-2">
				<div class="">
					<input
						type="checkbox"
						value=""
						class="w-3.5 h-3.5 text-blue-600 bg-gray-100 border-gray-300 rounded focus:ring-blue-500 dark:focus:ring-blue-600 dark:ring-offset-gray-800 focus:ring-2 dark:bg-gray-700 dark:border-gray-600"
					/>
				</div>
				<div class="ml-2">
					<NuxtImg src="/sellers/avatar.png" class="w-10 h-10 rounded-full" />
				</div>
				<div class="flex flex-col gap-y-0">
					<span class="text-base font-medium leading-tight">The Shop</span>
					<span class="text-neutral-500 text-sm leading-tight">$900.80</span>
				</div>
			</div>
			<div class="w-5 h-5 rotate-90 mr-2">
				<IconsChevronRight />
			</div>
		</div>
		<ul class="nest-list w-full flex flex-col px-2">
			<li class="border-b grid grid-cols-9 gap-x-1.5 items-center px-2">
				<div class="">
					<input
						type="checkbox"
						value=""
						class="w-3.5 h-3.5 text-blue-600 bg-gray-100 border-gray-300 rounded focus:ring-blue-500 dark:focus:ring-blue-600 dark:ring-offset-gray-800 focus:ring-2 dark:bg-gray-700 dark:border-gray-600"
					/>
				</div>
				<div class="col-span-2 items-center flex justify-center">
					<NuxtImg src="/items/phone.png" class="w-full h-auto" />
				</div>
				<div class="col-span-3 items-center flex justify-center flex-col gap-y-1">
					<span class="line-clamp-1 text-sm leading-tight"> Asus ROG Phone 5 Dual Sim s888 Phantom </span>
					<div class="w-full flex flex-row justify-between items-center gap-x-0">
						<button class="p-1.5 rounded shadow-sm bg-custom text-c-base">
							<div class="w-3 h-3">
								<IconsMinus />
							</div>
						</button>
						<span class="text-sm leading-tight"> QTY : 1 </span>
						<button class="p-1.5 rounded shadow-sm bg-custom text-c-base">
							<div class="w-3 h-3">
								<IconsPlus />
							</div>
						</button>
					</div>
				</div>
				<div class="col-span-2 items-center flex justify-center flex-col text-base">
					<span class="line-through text-neutral-500">$193.80</span>
					<span class="text-custom">$184.11</span>
				</div>
				<div class="flex items-center justify-end">
					<button>
						<div class="w-4 h-4">
							<IconsTrash />
						</div>
					</button>
				</div>
			</li>
			<li class="border-b grid grid-cols-9 gap-x-1.5 items-center px-2">
				<div class="">
					<input
						type="checkbox"
						value=""
						class="w-3.5 h-3.5 text-blue-600 bg-gray-100 border-gray-300 rounded focus:ring-blue-500 dark:focus:ring-blue-600 dark:ring-offset-gray-800 focus:ring-2 dark:bg-gray-700 dark:border-gray-600"
					/>
				</div>
				<div class="col-span-2 items-center flex justify-center">
					<NuxtImg src="/items/phone.png" class="w-full h-auto" />
				</div>
				<div class="col-span-3 items-center flex justify-center flex-col gap-y-1">
					<span class="line-clamp-1 text-sm leading-tight"> Asus ROG Phone 5 Dual Sim s888 Phantom </span>
					<div class="w-full flex flex-row justify-between items-center gap-x-0">
						<button class="p-1.5 rounded shadow-sm bg-custom text-c-base">
							<div class="w-3 h-3">
								<IconsMinus />
							</div>
						</button>
						<span class="text-sm leading-tight"> QTY : 1 </span>
						<button class="p-1.5 rounded shadow-sm bg-custom text-c-base">
							<div class="w-3 h-3">
								<IconsPlus />
							</div>
						</button>
					</div>
				</div>
				<div class="col-span-2 items-center flex justify-center flex-col text-base">
					<span class="line-through text-neutral-500">$193.80</span>
					<span class="text-custom">$184.11</span>
				</div>
				<div class="flex items-center justify-end">
					<button>
						<div class="w-4 h-4">
							<IconsTrash />
						</div>
					</button>
				</div>
			</li>
		</ul>
	</li>
</template>
