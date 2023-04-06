<template>
	<nav class="w-screen fixed bottom-0 left-0 right-0 md:hidden flex flex-col z-20">
		<div
			id="mobi-nav"
			class="flex flex-row justify-between items-center py-2 px-4 sm:px-6 border-t border-neutral-300 dark:border-neutral-700 bg-c-base/75 backdrop-blur-[100px] dark:bg-c-dark/90"
		>
			<button>
				<div class="w-6 h-6">
					<IconsHome />
				</div>
				<small class="text-xs sm:text-sm font-medium sm:font-semibold">Home</small>
			</button>
			<button>
				<div class="w-6 h-6">
					<IconsGrid />
				</div>
				<small class="text-xs sm:text-sm font-medium sm:font-semibold">Products</small>
			</button>
			<button>
				<div class="w-6 h-6">
					<IconsCart />
				</div>
				<small class="text-xs sm:text-sm font-medium sm:font-semibold">Cart</small>

				<div
					class="absolute inline-flex items-center justify-center w-6 h-6 text-xs font-bold text-white bg-custom rounded -top-1 -right-1.5 dark:border-gray-900"
				>
					8
				</div>
			</button>
			<button>
				<div class="w-6 h-6">
					<IconsDots />
				</div>
				<small class="text-xs sm:text-sm font-medium sm:font-semibold">Menu</small>
			</button>
		</div>
	</nav>
</template>

<style scoped>
#mobi-nav button {
	@apply relative flex flex-col gap-y-1 items-center justify-center px-2 py-1 text-neutral-700 hover:text-custom dark:text-c-mode dark:hover:text-custom dark:first:text-custom;
}
</style>
