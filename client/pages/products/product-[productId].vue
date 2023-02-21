<template>
	<section class="w-full flex flex-col py-4 px-4 md:px-8 lg:px-20 2xl:px-44">
		<div class="w-full grid grid-cols-1 xl:grid-cols-12 gap-x-6 gap-y-12">
			<div class="xl:col-span-9 flex flex-col gap-y-4">
				<div class="w-full grid grid-cols-1 md:grid-cols-10 gap-x-4 gap-y-8">
					<div class="md:col-span-4 flex flex-col gap-y-4">
						<ul class="w-full flex overflow-x-auto">
							<li class="w-full flex flex-col border border-neutral-200 rounded">
								<NuxtImg src="/items/phone.png" class="w-full rounded" />
							</li>
						</ul>
						<ul class="w-full flex flex-row gap-x-2 overflow-x-auto items-center">
							<li class="">
								<button
									class="w-24 h-24 p-1 border border-neutral-200 focus:border-custom rounded flex flex-col items-center justify-center"
								>
									<NuxtImg src="/items/phone.png" class="h-full" />
								</button>
							</li>
							<li class="">
								<button
									class="w-24 h-24 p-1 border border-neutral-200 focus:border-custom rounded flex flex-col items-center justify-center"
								>
									<NuxtImg src="/items/keyboard.png" class="h-full" />
								</button>
							</li>
							<li class="">
								<button
									class="w-24 h-24 p-1 border border-neutral-200 focus:border-custom rounded flex flex-col items-center justify-center"
								>
									<NuxtImg src="/items/tecno.jpg" class="h-full" />
								</button>
							</li>
						</ul>
					</div>
					<div class="md:col-span-6 flex flex-col gap-y-4">
						<div class="title w-full flex flex-col gap-y-2 pb-2 border-b border-neutral-200">
							<h2 class="text-2xl font-bold line-clamp-2 text-neutral-700">ASUS ROG Phone 5 Dual Sim S888 Phantom</h2>
							<div class="w-full flex flex-row items-center justify-between py-1">
								<div class="">
									<ContentsRatings />
								</div>
								<div class="flex flex-row gap-x-1 items-center pr-2">
									<button class="flex flex-row items-center gap-x-1 text-custom">
										<div class="w-3 h-3">
											<IconsHeart />
										</div>
										<small class="text-sm font-semibold">Add to Wishlist</small>
									</button>
								</div>
							</div>
						</div>
						<div class="brand w-full flex flex-row gap-x-4 items-center">
							<div class="w-20 h-20 flex items-center justify-center border border-neutral-200 rounded">
								<NuxtImg src="/items/phone.png" class="h-full w-auto" />
							</div>
							<div class="flex flex-col">
								<small class="text-sm text-neutral-500">Brand</small>
								<span class="text-base font-semibold uppercase">Hermes</span>
								<button class="text-sm text-neutral-500">View other products</button>
							</div>
						</div>
						<div class="w-full flex flex-col gap-y-2.5 mt-3 border-b border-neutral-200 pb-2.5">
							<div class="w-full grid grid-cols-10 gap-x-4 items-center">
								<div class="col-span-2">
									<small class="text-base text-neutral-500">Price</small>
								</div>
								<div class="col-span-8 flex flex-row items-center gap-x-4">
									<span class="text-xl text-neutral-500 font-medium line-through">$351.00</span>
									<div class="flex flex-row gap-x-2 items-center">
										<button class="px-2 bg-[tomato] text-white uppercase text-sm shadow-md">off 5%</button>
									</div>
								</div>
							</div>
							<div class="w-full grid grid-cols-10 gap-x-4 items-center">
								<div class="col-span-2">
									<small class="text-base text-neutral-500">Discounted Price</small>
								</div>
								<div class="col-span-8 flex flex-row items-center gap-x-4">
									<span class="text-2xl text-custom font-semibold">$351.00</span>
								</div>
							</div>
						</div>
						<div class="variant w-full flex flex-col gap-y-2 mt-1">
							<div class="w-full grid grid-cols-10 gap-x-4 items-center">
								<div class="col-span-2">
									<small class="text-base text-neutral-500">Memory</small>
								</div>
								<div class="col-span-8 flex flex-row items-center gap-x-4">
									<button class="px-3.5 py-1 border border-neutral-200 rounded text-base text-neutral-700 font-semibold">
										256 GB
									</button>
								</div>
							</div>
						</div>
						<div class="grid md:grid-cols-2 gap-x-4 gap-y-4 mt-2">
							<div class="px-4 py-3 border-custom border rounded bg-[red]/5 flex flex-col gap-y-2">
								<div class="flex flex-row gap-x-2 items-center">
									<div class="w-5 h-5 text-green-500">
										<svg fill="currentColor" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg" aria-hidden="true">
											<path
												clip-rule="evenodd"
												fill-rule="evenodd"
												d="M2.25 12c0-5.385 4.365-9.75 9.75-9.75s9.75 4.365 9.75 9.75-4.365 9.75-9.75 9.75S2.25 17.385 2.25 12zm13.36-1.814a.75.75 0 10-1.22-.872l-3.236 4.53L9.53 12.22a.75.75 0 00-1.06 1.06l2.25 2.25a.75.75 0 001.14-.094l3.75-5.25z"
											></path>
										</svg>
									</div>
									<small class="text-sm">In Stock</small>
								</div>
								<div class="flex flex-row gap-x-2 items-center">
									<div class="w-5 h-5 text-custom">
										<svg fill="currentColor" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg" aria-hidden="true">
											<path
												clip-rule="evenodd"
												fill-rule="evenodd"
												d="M4.804 21.644A6.707 6.707 0 006 21.75a6.721 6.721 0 003.583-1.029c.774.182 1.584.279 2.417.279 5.322 0 9.75-3.97 9.75-9 0-5.03-4.428-9-9.75-9s-9.75 3.97-9.75 9c0 2.409 1.025 4.587 2.674 6.192.232.226.277.428.254.543a3.73 3.73 0 01-.814 1.686.75.75 0 00.44 1.223zM8.25 10.875a1.125 1.125 0 100 2.25 1.125 1.125 0 000-2.25zM10.875 12a1.125 1.125 0 112.25 0 1.125 1.125 0 01-2.25 0zm4.875-1.125a1.125 1.125 0 100 2.25 1.125 1.125 0 000-2.25z"
											></path>
										</svg>
									</div>
									<small class="text-sm">Contact Admin</small>
								</div>
							</div>
							<div class="px-4 py-3 rounded bg-gray-200 flex flex-col gap-y-1.5">
								<div class="flex flex-row gap-x-2 items-center">
									<div class="w-7 h-7 text-neutral-500">
										<svg fill="currentColor" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg" aria-hidden="true">
											<path
												d="M3.375 4.5C2.339 4.5 1.5 5.34 1.5 6.375V13.5h12V6.375c0-1.036-.84-1.875-1.875-1.875h-8.25zM13.5 15h-12v2.625c0 1.035.84 1.875 1.875 1.875h.375a3 3 0 116 0h3a.75.75 0 00.75-.75V15z"
											></path>
											<path
												d="M8.25 19.5a1.5 1.5 0 10-3 0 1.5 1.5 0 003 0zM15.75 6.75a.75.75 0 00-.75.75v11.25c0 .087.015.17.042.248a3 3 0 015.958.464c.853-.175 1.522-.935 1.464-1.883a18.659 18.659 0 00-3.732-10.104 1.837 1.837 0 00-1.47-.725H15.75z"
											></path>
											<path d="M19.5 19.5a1.5 1.5 0 10-3 0 1.5 1.5 0 003 0z"></path>
										</svg>
									</div>
									<small class="text-base font-semibold leading-tight">Estimated Delivery time</small>
								</div>
								<div class="flex flex-row gap-x-2 px-8">
									<span class="text-base text-neutral-600 leading-tight">1 - 5 days</span>
								</div>
							</div>
						</div>
						<div class="quantity w-full grid grid-cols-10 gap-x-4 items-center mt-2">
							<div class="col-span-2">
								<small class="text-base text-neutral-500">Quantity</small>
							</div>
							<div class="col-span-8 flex flex-row gap-x-0 -space-x-px">
								<button class="px-2 py-1 text-neutral-600 border border-neutral-200 rounded-l">
									<div class="w-5 h-5">
										<IconsMinus />
									</div>
								</button>
								<input
									type="number"
									name="quantity"
									id="quantity"
									class="border border-neutral-200 py-1 text-lg text-center w-[6rem] outline-none focus:ring-1 focus:ring-custom focus:border-custom transition duration-200"
									value="1"
								/>
								<button class="px-2 py-1 text-neutral-600 border border-neutral-200 rounded-r">
									<div class="w-5 h-5">
										<IconsPlus />
									</div>
								</button>
							</div>
						</div>
						<div class="w-full flex flex-col gap-y-2 mt-2">
							<button
								class="text-lg text-white bg-c-dark/80 rounded py-2.5 font-medium hover:bg-c-dark/95 transition duration-200"
							>
								Add to Cart
							</button>
						</div>
						<!--  -->
					</div>
				</div>
				<div class="w-full flex flex-col gap-y-4 mt-12">
					<ContainersProductDetails />
				</div>
				<div class="mt-10 flex flex-col gap-y-4 w-full">
					<h2 class="text-xl sm:text-2xl md:text-3xl font-semibold text-neutral-600">More Items to Explore</h2>
					<div class="w-full grid grid-cols-2 sm:grid-cols-3 md:grid-cols-4 gap-4">
						<ListItemCard />
						<ListItemCard />
						<ListItemCard />
						<ListItemCard />
					</div>
				</div>
			</div>
			<div class="xl:col-span-3 !sticky">
				<ContentsAsideProduct />
			</div>
		</div>
	</section>
</template>

<style scoped>
::-webkit-scrollbar:horizontal {
	height: 0px;
}
</style>
