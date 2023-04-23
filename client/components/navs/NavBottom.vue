<script setup lang="ts">
const colorMode = useColorMode();
const toggleColor = (): void => {
	if (colorMode.value === "system" || colorMode.value === "light") {
		colorMode.value = "dark";
	} else {
		colorMode.value = "light";
	}
};
const colorBg = computed(() => {
	return colorMode.value === "system" || colorMode.value === "light";
});

const show_menu_data = ref<boolean>(false);
const toggleMenu = (): void => {
	show_menu_data.value = !show_menu_data.value;
};
const closeMenu = (): void => {
	setTimeout(() => {
		toggleMenu();
	}, 350);
};
</script>
<template>
	<nav class="w-screen fixed bottom-0 left-0 right-0 md:hidden flex flex-col z-20">
		<div
			id="mobi-nav"
			class="z-10 flex flex-row justify-between items-center py-2 px-4 sm:px-6 border-t border-neutral-300 dark:border-neutral-700 bg-white dark:bg-c-dark"
		>
			<button>
				<Icon name="mdi:home-outline" class="text-2xl" />
				<small class="text-xs sm:text-sm font-medium sm:font-semibold">Home</small>
			</button>
			<button>
				<Icon name="mdi:view-grid-outline" class="text-2xl" />
				<small class="text-xs sm:text-sm font-medium sm:font-semibold">Products</small>
			</button>
			<button>
				<Icon name="mdi:cart-outline" class="text-2xl" />
				<small class="text-xs sm:text-sm font-medium sm:font-semibold">Cart</small>

				<div
					class="absolute inline-flex items-center justify-center w-6 h-6 text-xs font-bold text-white bg-custom rounded -top-1 -right-1.5 dark:border-gray-900"
				>
					8
				</div>
			</button>
			<button @click="toggleMenu">
				<Transition mode="out-in">
					<Icon v-if="show_menu_data" name="mdi:close" class="icon text-2xl" />
					<Icon v-else name="mdi:dots-horizontal" class="icon text-2xl" />
				</Transition>
				<small class="text-xs sm:text-sm font-medium sm:font-semibold">Menu</small>
			</button>
		</div>
		<Transition name="show-menu-transition">
			<div v-if="show_menu_data" class="z-0 absolute bottom-full h-screen w-screen flex flex-col bg-black/50"></div>
		</Transition>
		<Transition name="show-menu">
			<div v-if="show_menu_data" class="z-0 absolute bottom-full h-screen w-screen flex flex-col">
				<div @click="toggleMenu" class="h-full w-full z-0"></div>
				<div
					class="h-[calc(100vh-225px)] absolute bottom-0 w-full bg-c-base z-10 backdrop-filter backdrop-blur-md rounded-t-md py-6 px-1 flex flex-col dark:bg-c-dark dark:backdrop-filter dark:backdrop-blur-md overflow-y-auto"
				>
					<nav class="w-full flex flex-col gap-y-2 px-1">
						<NuxtLink to="/" class="hover:bg-white px-2 rounded dark:hover:bg-alt-dark transition-colors duration-200">
							<div class="flex flex-row items-center gap-4 py-2.5">
								<Icon name="mdi:home-outline" class="text-xl sm:text-2xl text-neutral-600 dark:text-c-mode" />
								<span class="block text-base">Home</span>
							</div>
						</NuxtLink>
						<NuxtLink to="/products" class="hover:bg-white px-2 rounded dark:hover:bg-alt-dark transition-colors duration-200">
							<div class="flex flex-row items-center gap-4 py-2.5">
								<Icon name="mdi:view-grid-outline" class="text-xl sm:text-2xl text-neutral-600 dark:text-c-mode" />
								<span class="block text-base"> All Products</span>
							</div>
						</NuxtLink>
						<NuxtLink to="/shops" class="hover:bg-white px-2 rounded dark:hover:bg-alt-dark transition-colors duration-200">
							<div class="flex flex-row items-center gap-4 py-2.5">
								<Icon name="mdi:shopping-search-outline" class="text-xl sm:text-2xl text-neutral-600 dark:text-c-mode" />
								<span class="block text-base">Shops</span>
							</div>
						</NuxtLink>
						<NuxtLink to="/shops" class="hover:bg-white px-2 rounded dark:hover:bg-alt-dark transition-colors duration-200">
							<div class="flex flex-row items-center gap-4 py-2.5">
								<Icon name="mdi:cart-percent" class="text-xl sm:text-2xl text-neutral-600 dark:text-c-mode" />
								<span class="block text-base">Offers</span>
							</div>
						</NuxtLink>

						<NuxtLink to="/shops" class="hover:bg-white px-2 rounded dark:hover:bg-alt-dark transition-colors duration-200">
							<div class="flex flex-row items-center gap-4 py-2.5">
								<Icon name="mdi:arrow-top-right" class="text-xl sm:text-2xl text-neutral-600 dark:text-c-mode" />
								<span class="block text-base">Men Clothing & Fashion</span>
							</div>
						</NuxtLink>

						<NuxtLink to="/shops" class="hover:bg-white px-2 rounded dark:hover:bg-alt-dark transition-colors duration-200">
							<div class="flex flex-row items-center gap-4 py-2.5">
								<Icon name="mdi:arrow-top-right" class="text-xl sm:text-2xl text-neutral-600 dark:text-c-mode" />
								<span class="block text-base">Computer & Accessories</span>
							</div>
						</NuxtLink>
					</nav>
					<div class="a w-full flex flex-col gap-y-1 border-t border-neutral-200 mt-2 pt-2 dark:border-neutral-600">
						<NuxtLink
							to="/user/dashboard"
							class="w-full flex flex-row py-0.5 px-3.5 hover:bg-white rounded dark:hover:bg-alt-dark transition-colors duration-200"
						>
							<div class="flex flex-row items-center gap-4 py-2">
								<Icon name="mdi:account-outline" class="text-xl sm:text-2xl text-neutral-600 dark:text-c-mode" />
								<span class="block text-base">Account</span>
							</div>
						</NuxtLink>
						<button
							@click="toggleColor"
							class="w-full flex flex-row py-2.5 px-3.5 hover:bg-white rounded dark:hover:bg-alt-dark transition-colors duration-200"
						>
							<Transition mode="out-in">
								<div v-if="colorBg" class="flex flex-row w-full gap-x-3 items-center">
									<Icon name="mdi:white-balance-sunny" class="text-xl sm:text-2xl text-neutral-600 dark:text-c-mode" />
									<span class="text-base">Toggle Dark Mode</span>
								</div>
								<div v-else class="flex flex-row w-full gap-x-3 items-center">
									<Icon
										name="mdi:moon-waning-crescent"
										class="text-xl sm:text-2xl -rotate-45 text-neutral-600 dark:text-c-mode"
									/>
									<span class="text-base">Toggle Light Mode</span>
								</div>
							</Transition>
						</button>
					</div>
				</div>
			</div>
		</Transition>
	</nav>
</template>

<style scoped>
#mobi-nav button {
	@apply relative flex flex-col gap-y-1 items-center justify-center px-2 py-1 text-neutral-700 hover:text-custom dark:text-c-mode dark:hover:text-custom dark:first:text-custom;
}
button:focus small,
button:focus .icon {
	@apply text-custom dark:text-custom;
}
.show-menu-transition-enter-from,
.show-menu-transition-leave-to {
	@apply opacity-0;
}
.show-menu-transition-enter-active,
.show-menu-transition-leave-active {
	transition: opacity 250ms ease;
}
.show-menu-enter-from,
.show-menu-leave-to {
	@apply translate-y-[80%] opacity-0;
}
.show-menu-enter-active,
.show-menu-leave-active {
	transition: all 250ms ease;
}
</style>
