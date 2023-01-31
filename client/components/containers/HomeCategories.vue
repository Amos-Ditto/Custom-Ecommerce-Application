<template>
	<div class="w-full flex flex-col gap-y-2">
		<div class="w-full flex flex-row items-center justify-between py-1">
			<h3 class="text-xl md:text-2xl font-semibold">Product Categories</h3>
			<div class="flex flex-row items-center">
				<button class="text-base font-semibold text-custom capitalize flex flex-row items-center gap-x-1 hover:opacity-80">
					view all
					<div class="w-4 h-4">
						<IconsChevronRight />
					</div>
				</button>
			</div>
		</div>
		<div class="flex flex-row gap-x-3 items-center w-full">
			<div class="category flex flex-col p-2 ring-1 ring-neutral-200 rounded">
				<div class="flex items-center min-h-[8rem] bg-gray-200"></div>
				<div class="flex flex-col gap-y-1 mt-2.5">
					<small class="text-sm text-neutral-600 truncate">Men clothing & Fashion</small>
				</div>
			</div>
		</div>
	</div>
</template>
