<template>
	<div class="w-full flex flex-col gap-y-2 border-r border-neutral-200">
		<div class="user-details w-full py-4 px-2 flex flex-col items-center justify-center gap-y-2 border-b border-neutral-200">
			<div class="user-avatar w-full flex items-center justify-center">
				<NuxtImg src="/icons/male.png" class="w-44 h-44 rounded-full ring-4 ring-white" />
			</div>
			<div class="w-full flex flex-col items-center">
				<h4 class="text-2xl truncate font-medium">Amos Kipyegon</h4>
				<small class="text-neutral-500 truncate text-base">amoskipyegon@gmail.com</small>
			</div>
		</div>
		<ul class="w-full flex flex-col gap-y-1 py-1">
			<li class="w-full flex flex-row gap-x-3 items-center py-3 px-4 text-base font-medium bg-custom text-c-base cursor-pointer">
				<div class="w-5 h-5">
					<IconsGrid />
				</div>
				<span class="tracking-wide">Dashboard</span>
			</li>
			<li class="w-full flex flex-row gap-x-3 items-center py-3 px-4 text-base font-medium hover:bg-gray-100 cursor-pointer">
				<div class="w-5 h-5">
					<IconsList />
				</div>
				<span class="tracking-wide">Purchase History</span>
			</li>
			<li class="w-full flex flex-row gap-x-3 items-center py-3 px-4 text-base font-medium hover:bg-gray-100 cursor-pointer">
				<div class="w-5 h-5">
					<IconsHeart />
				</div>
				<span class="tracking-wide">Wishlist</span>
			</li>
			<li class="w-full flex flex-row gap-x-3 items-center py-3 px-4 text-base font-medium hover:bg-gray-100 cursor-pointer">
				<div class="w-5 h-5">
					<IconsChat />
				</div>
				<span class="tracking-wide">Product Queries (0)</span>
			</li>
			<li class="w-full flex flex-row gap-x-3 items-center py-3 px-4 text-base font-medium hover:bg-gray-100 cursor-pointer">
				<div class="w-5 h-5">
					<IconsUser />
				</div>
				<span class="tracking-wide">Manage Profile</span>
			</li>
		</ul>
	</div>
</template>
