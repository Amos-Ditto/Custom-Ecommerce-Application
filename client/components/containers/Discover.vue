<template>
	<div class="w-full flex flex-col items-center justify-center gap-y-2 mt-2">
		<!-- <div class="flex flex-col">
			<button
				class="px-16 py-3 rounded-full text-lg text-c-mode bg-gradient-to-r from-[#ff0a0a] to-[#ff7539] hover:to-[#ff0a0a] hover:from-[#ff7539]"
			>
				View more
			</button>
		</div> -->
		<div class="flex flex-row gap-x-4 items-center mt-6 text-neutral-700 dark:text-c-mode font-medium">
			<span class="text-sm sm:text-base">Discover more</span>
			<ul class="discover-list flex flex-row items-center text-sm sm:text-base">
				<li role="button" class="">Shirts</li>
				<li role="button" class="">shoes</li>
			</ul>
			<span class="text-sm sm:text-base">Shop</span>
		</div>
	</div>
</template>

<style scoped>
.discover-list li {
	@apply px-2 sm:py-[1px] capitalize flex items-center relative after:content-[''] after:absolute after:right-0 after:h-[65%] after:w-[1px] after:bg-neutral-400 after:dark:bg-neutral-300;
}
</style>
