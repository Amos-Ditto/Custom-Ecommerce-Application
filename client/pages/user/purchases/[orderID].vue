<template>
	<div class="w-full flex flex-col gap-y-4">
		<h3 class="text-xl sm:text-2xl font-semibold text-neutral-700 dark:text-c-mode">Order: {{ $route.params.orderID }}</h3>

		<div class="w-full flex flex-col gap-y-2 mt-4">
			<div class="w-full bg-gray-200 px-4 py-3 rounded dark:bg-neutral-700">
				<h5 class="text-base sm:text-lg font-semibold text-neutral-800 dark:text-c-mode">Order Summary</h5>
			</div>
			<ul class="order-details w-full grid grid-cols-1 md:grid-cols-2 gap-4 px-4 mt-2 dark:text-c-mode">
				<li>
					<div class="flex fle-row items-start">
						<span class="text-sm sm:text-base font-semibold">Order Code:</span>
					</div>
					<div class="flex flex-col text-neutral-600 dark:text-c-mode">
						<span class="text-sm sm:text-base">20230224-122456</span>
					</div>
				</li>
				<li>
					<div class="flex fle-row items-start">
						<span class="text-sm sm:text-base font-semibold">Total Order Amount:</span>
					</div>
					<div class="flex flex-col text-neutral-600 dark:text-c-mode">
						<span class="text-sm sm:text-base">$1,335.40</span>
					</div>
				</li>
				<li>
					<div class="flex fle-row items-start">
						<span class="text-sm sm:text-base font-semibold">Name:</span>
					</div>
					<div class="flex flex-col text-neutral-600 dark:text-c-mode">
						<span class="text-sm sm:text-base">Amos Kipyegon</span>
					</div>
				</li>
				<li>
					<div class="flex fle-row items-start">
						<span class="text-sm sm:text-base font-semibold">Email:</span>
					</div>
					<div class="flex flex-col text-neutral-600 dark:text-c-mode">
						<span class="text-sm sm:text-base">amosk@gmail.com</span>
					</div>
				</li>

				<li>
					<div class="flex fle-row items-start">
						<span class="text-sm sm:text-base font-semibold">Phone number:</span>
					</div>
					<div class="flex flex-col text-neutral-600 dark:text-c-mode">
						<span class="text-sm sm:text-base">0794818111</span>
					</div>
				</li>
				<li>
					<div class="flex fle-row items-start">
						<span class="text-sm sm:text-base font-semibold">Shipping Address:</span>
					</div>
					<div class="flex flex-col text-neutral-600 dark:text-c-mode">
						<p class="text-sm sm:text-base leading-tight">
							4471 Nutters Barn Lane Des Moines, IA 50309 5252, Alabaster, Alabama United States
						</p>
						<p class="text-sm sm:text-base leading-tight">5156416642</p>
					</div>
				</li>
			</ul>
		</div>
		<div class="w-full flex flex-col gap-y-2 mt-6">
			<div class="w-full bg-gray-200 px-4 py-3 rounded dark:bg-neutral-700">
				<h5 class="text-base sm:text-lg font-semibold text-neutral-800 dark:text-c-mode">The Shop</h5>
			</div>
			<div class="w-full flex flex-col items-center justify-center">
				<ContentsSteps />
			</div>
			<div class="w-full flex flex-col">
				<ul
					class="w-full grid grid-cols-12 gap-x-1 border-b border-neutral-200 px-1 sm:px-4 py-2.5 text-neutral-500 text-sm sm:text-base font-semibold tracking-tight dark:border-neutral-700 dark:text-c-mode/70"
				>
					<li class="col-span-1">#</li>
					<li class="col-span-5">Product</li>
					<li class="col-span-2 text-center truncate">Quantity</li>
					<li class="col-span-2 text-center truncate">Unit price</li>
					<li class="col-span-2 text-end">Total</li>
				</ul>
				<ul class="w-full flex flex-col text-sm sm:text-base dark:text-c-mode">
					<li class="w-full py-2.5 sm:py-2 border-b border-neutral-200 px-1 sm:px-4 dark:border-neutral-700">
						<ul class="w-full grid grid-cols-12 items-center gap-x-1">
							<li class="col-span-1">
								<span>1</span>
							</li>
							<li class="col-span-5 grid grid-cols-10 gap-x-2 items-center">
								<div class="col-span-2">
									<NuxtImg src="/items/phone.png" class="w-full" />
								</div>
								<div class="col-span-8">
									<p class="text-neutral-600 line-clamp-1 leading-tight dark:text-c-mode/80">
										Asus ROG Phone 5 Dual Sim s888 Phantom
									</p>
								</div>
							</li>
							<li class="col-span-2 text-center">
								<span>1</span>
							</li>
							<li class="col-span-2 text-center">
								<span>$292.00</span>
							</li>
							<li class="col-span-2 text-end">
								<span>$292.00</span>
							</li>
						</ul>
					</li>
					<li class="w-full py-2.5 sm:py-2 border-b border-neutral-200 px-1 sm:px-4 dark:border-neutral-700">
						<ul class="w-full grid grid-cols-12 items-center gap-x-1">
							<li class="col-span-1">
								<span>1</span>
							</li>
							<li class="col-span-5 grid grid-cols-10 gap-x-2 items-center">
								<div class="col-span-2">
									<NuxtImg src="/items/phone.png" class="w-full" />
								</div>
								<div class="col-span-8">
									<p class="text-neutral-600 line-clamp-1 leading-tight dark:text-c-mode/80">
										Asus ROG Phone 5 Dual Sim s888 Phantom
									</p>
								</div>
							</li>
							<li class="col-span-2 text-center">
								<span>1</span>
							</li>
							<li class="col-span-2 text-center">
								<span>$292.00</span>
							</li>
							<li class="col-span-2 text-end">
								<span>$292.00</span>
							</li>
						</ul>
					</li>
					<li class="w-full py-2.5 sm:py-2 border-b border-neutral-200 px-1 sm:px-4 dark:border-neutral-700">
						<ul class="w-full grid grid-cols-12 items-center gap-x-1">
							<li class="col-span-1">
								<span>1</span>
							</li>
							<li class="col-span-5 grid grid-cols-10 gap-x-2 items-center">
								<div class="col-span-2">
									<NuxtImg src="/items/phone.png" class="w-full" />
								</div>
								<div class="col-span-8">
									<p class="text-neutral-600 line-clamp-1 leading-tight dark:text-c-mode/80">
										Asus ROG Phone 5 Dual Sim s888 Phantom
									</p>
								</div>
							</li>
							<li class="col-span-2 text-center">
								<span>1</span>
							</li>
							<li class="col-span-2 text-center">
								<span>$292.00</span>
							</li>
							<li class="col-span-2 text-end">
								<span>$292.00</span>
							</li>
						</ul>
					</li>
				</ul>
				<div class="w-full flex flex-col-reverse md:grid grid-cols-2 gap-x-2 gap-y-2 mt-8">
					<div class="flex items-center justify-center">
						<NuxtImg src="/icons/paid_sticker.svg" />
					</div>
					<div class="flex flex-col gap-y-4">
						<div class="grid grid-cols-2 items-center text-base font-semibold px-4">
							<div class="">
								<span>Sub Total:</span>
							</div>
							<div class="text-end">
								<span>$224.10</span>
							</div>
						</div>
						<div class="grid grid-cols-2 items-center text-base font-semibold px-4">
							<div class="">
								<span>Tax:</span>
							</div>
							<div class="text-end">
								<span>$3.90</span>
							</div>
						</div>
						<div class="grid grid-cols-2 items-center text-base font-semibold bg-red-400/10 rounded py-3 px-4">
							<div class="">
								<span>Total:</span>
							</div>
							<div class="text-end">
								<span>$230.00</span>
							</div>
						</div>
					</div>
				</div>
			</div>
		</div>
	</div>
</template>

<style scoped>
ul.order-details li {
	@apply grid grid-cols-2 gap-x-4;
}
</style>
