<template>
	<div class="w-full grid grid-cols-1 sm:grid-cols-10 xl:grid-cols-1 gap-y-8 sm:gap-y-3 gap-x-6">
		<div class="sm:col-span-3 xl:col-span-1 flex flex-col gap-y-2">
			<div class="flex flex-col gap-y-2 bg-gray-100 border border-neutral-200 rounded py-3 px-2.5">
				<h3 class="text-xl font-semibold">Shop</h3>
				<div class="flex flex-row gap-x-4 items-center w-full">
					<div class="w-14 h-14">
						<NuxtImg src="/sellers/avatar.png" loading="lazy" class="w-full h-full rounded-full" />
					</div>
					<div class="flex flex-row">
						<span class="text-lg font-semibold truncate">The Shop</span>
					</div>
				</div>
				<div class="mt-3">
					<ContentsRatings />
				</div>
				<div class="w-full flex flex-col items-center mt-2">
					<button
						class="w-full bg-yellow-100 text-yellow-800 text-sm font-medium px-3.5 py-1.5 rounded dark:bg-neutral-800 dark:text-yellow-300 border border-yellow-300"
					>
						Visit Shop
					</button>
				</div>
			</div>
			<div class="mt-4 w-full flex flex-col">
				<NuxtImg src="/slides/14.webp" class="w-full h-auto" />
			</div>
		</div>
		<div class="sm:col-span-7 xl:col-span-1 flex flex-col xl:mt-6">
			<div class="w-full flex flex-col gap-y-2">
				<h3 class="text-lg">Related Products</h3>
				<ul class="w-full grid grid-cols-2 xl:grid-cols-1 gap-4">
					<li class="grid grid-cols-3 sm:grid-cols-2 gap-x-2 px-2.5 py-2.5 border border-neutral-200 rounded items-center">
						<div class="flex flex-col">
							<NuxtImg src="/items/phone.png" class="w-16 sm:w-24" />
						</div>
						<div class="col-span-2 sm:col-span-1 flex flex-col gap-y-2">
							<small class="text-neutral-600 text-sm truncate"> ASUS ROG Phone 5 Dual Sim S888 Phantom </small>
							<div class="flex flex-row gap-x-2 items-center">
								<span class="text-sm sm:text-base text-neutral-500 line-through">$80.00</span>
								<span class="text-sm sm:text-base font-semibold">$78.40</span>
							</div>
						</div>
					</li>
					<li class="grid grid-cols-3 sm:grid-cols-2 gap-x-2 px-2.5 py-2.5 border border-neutral-200 rounded items-center">
						<div class="flex flex-col">
							<NuxtImg src="/items/phone.png" class="w-16 sm:w-24" />
						</div>
						<div class="col-span-2 sm:col-span-1 flex flex-col gap-y-2">
							<small class="text-neutral-600 text-sm truncate"> ASUS ROG Phone 5 Dual Sim S888 Phantom </small>
							<div class="flex flex-row gap-x-2 items-center">
								<span class="text-sm sm:text-base text-neutral-500 line-through">$80.00</span>
								<span class="text-sm sm:text-base font-semibold">$78.40</span>
							</div>
						</div>
					</li>

					<li class="grid grid-cols-3 sm:grid-cols-2 gap-x-2 px-2.5 py-2.5 border border-neutral-200 rounded items-center">
						<div class="flex flex-col">
							<NuxtImg src="/items/phone.png" class="w-16 sm:w-24" />
						</div>
						<div class="col-span-2 sm:col-span-1 flex flex-col gap-y-2">
							<small class="text-neutral-600 text-sm truncate"> ASUS ROG Phone 5 Dual Sim S888 Phantom </small>
							<div class="flex flex-row gap-x-2 items-center">
								<span class="text-sm sm:text-base text-neutral-500 line-through">$80.00</span>
								<span class="text-sm sm:text-base font-semibold">$78.40</span>
							</div>
						</div>
					</li>

					<li class="grid grid-cols-3 sm:grid-cols-2 gap-x-2 px-2.5 py-2.5 border border-neutral-200 rounded items-center">
						<div class="flex flex-col">
							<NuxtImg src="/items/phone.png" class="w-16 sm:w-24" />
						</div>
						<div class="col-span-2 sm:col-span-1 flex flex-col gap-y-2">
							<small class="text-neutral-600 text-sm truncate"> ASUS ROG Phone 5 Dual Sim S888 Phantom </small>
							<div class="flex flex-row gap-x-2 items-center">
								<span class="text-sm sm:text-base text-neutral-500 line-through">$80.00</span>
								<span class="text-sm sm:text-base font-semibold">$78.40</span>
							</div>
						</div>
					</li>

					<li class="grid grid-cols-3 sm:grid-cols-2 gap-x-2 px-2.5 py-2.5 border border-neutral-200 rounded items-center">
						<div class="flex flex-col">
							<NuxtImg src="/items/phone.png" class="w-16 sm:w-24" />
						</div>
						<div class="col-span-2 sm:col-span-1 flex flex-col gap-y-2">
							<small class="text-neutral-600 text-sm truncate"> ASUS ROG Phone 5 Dual Sim S888 Phantom </small>
							<div class="flex flex-row gap-x-2 items-center">
								<span class="text-sm sm:text-base text-neutral-500 line-through">$80.00</span>
								<span class="text-sm sm:text-base font-semibold">$78.40</span>
							</div>
						</div>
					</li>

					<li class="grid grid-cols-3 sm:grid-cols-2 gap-x-2 px-2.5 py-2.5 border border-neutral-200 rounded items-center">
						<div class="flex flex-col">
							<NuxtImg src="/items/phone.png" class="w-16 sm:w-24" />
						</div>
						<div class="col-span-2 sm:col-span-1 flex flex-col gap-y-2">
							<small class="text-neutral-600 text-sm truncate"> ASUS ROG Phone 5 Dual Sim S888 Phantom </small>
							<div class="flex flex-row gap-x-2 items-center">
								<span class="text-sm sm:text-base text-neutral-500 line-through">$80.00</span>
								<span class="text-sm sm:text-base font-semibold">$78.40</span>
							</div>
						</div>
					</li>
				</ul>
			</div>
		</div>
	</div>
</template>
