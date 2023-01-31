<template>
	<div class="w-full flex flex-col">
		<div class="w-full grid grid-cols-12 gap-x-5 gap-y-5">
			<div class="col-span-12 lg:col-span-6 min-h-[14rem] lg:min-h-[18rem] bg-base rounded-l">
				<NuxtImg src="/11.webp" class="bg-cover cursor-pointer" alt="" />
			</div>
			<div class="col-span-6 lg:col-span-3 min-h-[14rem] lg:min-h-[18rem] bg-base">
				<NuxtImg src="/21.webp" class="h-full w-full cursor-pointer" alt="" />
			</div>
			<div class="col-span-6 lg:col-span-3 min-h-[14rem] lg:min-h-[18rem] grid grid-rows-2 grid-cols-1 gap-y-4">
				<div class="bg-base rounded-tr row-span-1 col-span-1">
					<NuxtImg src="/14.webp" class="bg-cover cursor-pointer" alt="" />
				</div>
				<div class="bg-base rounded-br row-span-1 col-span-1">
					<NuxtImg src="/13.webp" class="bg-cover cursor-pointer" alt="" />
				</div>
			</div>
		</div>
	</div>
</template>
