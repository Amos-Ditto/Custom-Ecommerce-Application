<template>
	<section class="w-full flex flex-col gap-y-4">
		<h3 class="text-2xl font-semibold text-neutral-700">Purchase History</h3>

		<div class="w-full">
			<!-- Table -->

			<div class="relative overflow-x-auto border border-neutral-200 rounded px-2.5">
				<table class="w-full text-sm text-left text-gray-800 dark:text-gray-400 px-">
					<thead class="text-sm text-gray-700 uppercase bg-gray-50 border-b border-neutral-200">
						<tr>
							<th scope="col" class="px-6 pt-6 pb-2">Details</th>
							<th scope="col" class="px-6 pt-6 pb-2">Info</th>
							<th scope="col" class="px-6 pt-6 pb-2">Amount</th>
							<th scope="col" class="px-6 pt-6 pb-2 text-end">Actions</th>
						</tr>
					</thead>
					<tbody>
						<tr class="border-b hover:bg-gray-100 text-base">
							<td scope="row" class="px-6 py-2.5 font-medium flex flex-col gap-y-1">
								<h4 class="text-base truncate">20230224-122456</h4>
								<small class="text-sm text-neutral-500 truncate">Feb 24, 2023</small>
							</td>
							<td class="px-6 py-2.5">
								<div class="w-full flex flex-col gap-y-1">
									<span>3 products</span>
									<span class="text-sm text-neutral-500">from 1 shop</span>
								</div>
							</td>
							<td class="px-6 py-2.5">$1335.00</td>

							<td class="px-6 py-2.5 text-right">
								<NuxtLink
									to="/user/purchase/1"
									class="font-medium text-blue-600 dark:text-blue-500 hover:bg-blue-400/20 px-2 py-1 rounded transition-colors"
								>
									View details
								</NuxtLink>
							</td>
						</tr>
						<tr class="border-b hover:bg-gray-100 text-base">
							<td scope="row" class="px-6 py-2.5 font-medium flex flex-col gap-y-1">
								<h4 class="text-base truncate">20230224-122456</h4>
								<small class="text-sm text-neutral-500 truncate">Feb 24, 2023</small>
							</td>
							<td class="px-6 py-2.5">
								<div class="w-full flex flex-col gap-y-1">
									<span>3 products</span>
									<span class="text-sm text-neutral-500">from 1 shop</span>
								</div>
							</td>
							<td class="px-6 py-2.5">$1999</td>

							<td class="px-6 py-2.5 text-right">
								<NuxtLink
									to="/user/purchase/1"
									class="font-medium text-blue-600 dark:text-blue-500 hover:bg-blue-400/20 px-2 py-1 rounded transition-colors"
								>
									View details
								</NuxtLink>
							</td>
						</tr>
						<tr class="hover:bg-gray-100 text-base">
							<td scope="row" class="px-6 py-2.5 font-medium flex flex-col gap-y-1">
								<h4 class="text-base truncate">20230224-122456</h4>
								<small class="text-sm text-neutral-500 truncate">Feb 24, 2023</small>
							</td>
							<td class="px-6 py-2.5">
								<div class="w-full flex flex-col gap-y-1">
									<span>3 products</span>
									<span class="text-sm text-neutral-500">from 1 shop</span>
								</div>
							</td>
							<td class="px-6 py-2.5">$99</td>

							<td class="px-6 py-2.5 text-right">
								<NuxtLink
									to="/user/purchase/1"
									class="font-medium text-blue-600 dark:text-blue-500 hover:bg-blue-400/20 px-2 py-1 rounded transition-colors"
								>
									View details
								</NuxtLink>
							</td>
						</tr>
						<tr class="border-b hover:bg-gray-100 text-base">
							<td scope="row" class="px-6 py-2.5 font-medium flex flex-col gap-y-1">
								<h4 class="text-base truncate">20230224-122456</h4>
								<small class="text-sm text-neutral-500 truncate">Feb 24, 2023</small>
							</td>
							<td class="px-6 py-2.5">
								<div class="w-full flex flex-col gap-y-1">
									<span>3 products</span>
									<span class="text-sm text-neutral-500">from 1 shop</span>
								</div>
							</td>
							<td class="px-6 py-2.5">$1335.00</td>

							<td class="px-6 py-2.5 text-right">
								<NuxtLink
									to="/user/purchase/1"
									class="font-medium text-blue-600 dark:text-blue-500 hover:bg-blue-400/20 px-2 py-1 rounded transition-colors"
								>
									View details
								</NuxtLink>
							</td>
						</tr>
						<tr class="border-b hover:bg-gray-100 text-base">
							<td scope="row" class="px-6 py-2.5 font-medium flex flex-col gap-y-1">
								<h4 class="text-base truncate">20230224-122456</h4>
								<small class="text-sm text-neutral-500 truncate">Feb 24, 2023</small>
							</td>
							<td class="px-6 py-2.5">
								<div class="w-full flex flex-col gap-y-1">
									<span>3 products</span>
									<span class="text-sm text-neutral-500">from 1 shop</span>
								</div>
							</td>
							<td class="px-6 py-2.5">$1999</td>

							<td class="px-6 py-2.5 text-right">
								<NuxtLink
									to="/user/purchase/1"
									class="font-medium text-blue-600 dark:text-blue-500 hover:bg-blue-400/20 px-2 py-1 rounded transition-colors"
								>
									View details
								</NuxtLink>
							</td>
						</tr>
						<tr class="hover:bg-gray-100 text-base">
							<td scope="row" class="px-6 py-2.5 font-medium flex flex-col gap-y-1">
								<h4 class="text-base truncate">20230224-122456</h4>
								<small class="text-sm text-neutral-500 truncate">Feb 24, 2023</small>
							</td>
							<td class="px-6 py-2.5">
								<div class="w-full flex flex-col gap-y-1">
									<span>3 products</span>
									<span class="text-sm text-neutral-500">from 1 shop</span>
								</div>
							</td>
							<td class="px-6 py-2.5">$99</td>

							<td class="px-6 py-2.5 text-right">
								<NuxtLink
									to="/user/purchase/1"
									class="font-medium text-blue-600 dark:text-blue-500 hover:bg-blue-400/20 px-2 py-1 rounded transition-colors"
								>
									View details
								</NuxtLink>
							</td>
						</tr>
					</tbody>
				</table>
			</div>

			<!--  -->
		</div>
	</section>
</template>
