<script setup lang="ts">
const colorMode = useColorMode();
console.log(colorMode.preference);
const toggleColor = (): void => {
	if (colorMode.value === "system" || colorMode.value === "light") {
		colorMode.value = "dark";
	} else {
		colorMode.value = "light";
	}
};
</script>
<template>
	<div
		class="w-full backdrop-blur-[100px] bg-c-base/90 hidden md:flex flex-row justify-between items-center py-2 px-8 lg:px-20 2xl:px-36 text-neutral-500 border-b border-neutral-200 dark:bg-c-dark/90 dark:border-neutral-700"
	>
		<div class="flex flex-row items-center gap-x-2">
			<button
				class="text-sm px-2.5 text-neutral-500 hover:text-neutral-600 transition-colors duration-200 bg-inherit dark:text-neutral-300"
			>
				Be a Seller
			</button>
			<span
				class="h-full relative after:h-[14px] after:w-[1px] after:bg-neutral-300 after:content-[''] after:absolute after:right-0 flex items-center"
			></span>
			<button
				class="text-sm px-2.5 text-neutral-500 hover:text-neutral-600 transition-colors duration-200 bg-inherit dark:text-neutral-300"
			>
				Track Order
			</button>
		</div>
		<div class="flex flex-row items-center gap-x-2">
			<span class="text-sm px-2.5 text-neutral-500 flex flex-row items-center gap-x-1 dark:text-neutral-300">
				<svg
					class="w-4 h-4"
					fill="none"
					stroke="currentColor"
					stroke-width="1.5"
					viewBox="0 0 24 24"
					xmlns="http://www.w3.org/2000/svg"
					aria-hidden="true"
				>
					<path
						stroke-linecap="round"
						stroke-linejoin="round"
						d="M2.25 6.75c0 8.284 6.716 15 15 15h2.25a2.25 2.25 0 002.25-2.25v-1.372c0-.516-.351-.966-.852-1.091l-4.423-1.106c-.44-.11-.902.055-1.173.417l-.97 1.293c-.282.376-.769.542-1.21.38a12.035 12.035 0 01-7.143-7.143c-.162-.441.004-.928.38-1.21l1.293-.97c.363-.271.527-.734.417-1.173L6.963 3.102a1.125 1.125 0 00-1.091-.852H4.5A2.25 2.25 0 002.25 4.5v2.25z"
					></path>
				</svg>
				Help line +254-794 818 111
			</span>
			<span
				class="h-full relative after:h-[14px] after:w-[1px] after:bg-neutral-300 after:content-[''] after:absolute after:right-0 flex items-center"
			></span>
			<span class="text-sm px-2.5 text-neutral-500 font-normal dark:text-neutral-300">Wishlist (0)</span>
			<span
				class="h-full relative after:h-[14px] after:w-[1px] after:bg-neutral-300 after:content-[''] after:absolute after:right-0 flex items-center"
			></span>

			<button
				@click="toggleColor"
				class="ml-2 text-neutral-600 hover:text-neutral-800 w-5 h-5 flex items-center justify-center transition-colors duration-200 dark:text-neutral-300"
			>
				<Transition mode="out-in">
					<svg
						v-if="colorMode.value === 'system' || colorMode.value === 'light'"
						fill="none"
						stroke="currentColor"
						stroke-width="1.5"
						viewBox="0 0 24 24"
						xmlns="http://www.w3.org/2000/svg"
						aria-hidden="true"
					>
						<path
							stroke-linecap="round"
							stroke-linejoin="round"
							d="M12 3v2.25m6.364.386l-1.591 1.591M21 12h-2.25m-.386 6.364l-1.591-1.591M12 18.75V21m-4.773-4.227l-1.591 1.591M5.25 12H3m4.227-4.773L5.636 5.636M15.75 12a3.75 3.75 0 11-7.5 0 3.75 3.75 0 017.5 0z"
						></path>
					</svg>
					<svg
						v-else
						fill="none"
						stroke="currentColor"
						stroke-width="1.5"
						viewBox="0 0 24 24"
						xmlns="http://www.w3.org/2000/svg"
						aria-hidden="true"
					>
						<path
							stroke-linecap="round"
							stroke-linejoin="round"
							d="M21.752 15.002A9.718 9.718 0 0118 15.75c-5.385 0-9.75-4.365-9.75-9.75 0-1.33.266-2.597.748-3.752A9.753 9.753 0 003 11.25C3 16.635 7.365 21 12.75 21a9.753 9.753 0 009.002-5.998z"
						></path>
					</svg>
				</Transition>
			</button>
		</div>
	</div>
</template>
