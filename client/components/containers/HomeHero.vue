<template>
	<div class="w-full flex flex-col">
		<div class="w-full grid grid-cols-12 gap-x-2 sm:gap-x-5 gap-y-2 sm:gap-y-5">
			<div class="col-span-12 lg:col-span-6 lg:max-h-[17.5rem] bg-base">
				<NuxtImg src="/slides/11.webp" class="bg-cover cursor-pointer h-full w-full rounded-md" alt="" />
			</div>
			<div class="col-span-6 lg:col-span-3 lg:max-h-[17.5rem] bg-base">
				<NuxtImg src="/slides/21.webp" class="h-full w-full cursor-pointer rounded-md" alt="" />
			</div>
			<div class="col-span-6 lg:col-span-3 lg:max-h-[17.5rem] grid grid-rows-2 grid-cols-1 gap-y-1 sm:gap-y-4">
				<div class="bg-base rounded-tr row-span-1 col-span-1">
					<NuxtImg src="/slides/14.webp" class="bg-cover cursor-pointer rounded-md h-full w-full" alt="" />
				</div>
				<div class="bg-base rounded-br row-span-1 col-span-1">
					<NuxtImg src="/slides/13.webp" class="bg-cover cursor-pointer rounded-md h-full w-full" alt="" />
				</div>
			</div>
		</div>
	</div>
</template>
