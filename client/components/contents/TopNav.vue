<template>
	<div
		class="w-full backdrop-blur-[100px] bg-c-base/90 hidden md:flex flex-row justify-between items-center py-2 px-8 lg:px-20 2xl:px-36 text-neutral-500 border-b border-neutral-200"
	>
		<div class="flex flex-row items-center gap-x-2">
			<button class="text-sm px-2.5 text-neutral-500 hover:text-neutral-600 transition-colors duration-200 bg-inherit">
				Be a Seller
			</button>
			<span
				class="h-full relative after:h-[14px] after:w-[1px] after:bg-neutral-300 after:content-[''] after:absolute after:right-0 flex items-center"
			></span>
			<button class="text-sm px-2.5 text-neutral-500 hover:text-neutral-600 transition-colors duration-200 bg-inherit">
				Track Order
			</button>
		</div>
		<div class="flex flex-row items-center gap-x-2">
			<span class="text-sm px-2.5 text-neutral-500 flex flex-row items-center gap-x-1">
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
			<span class="text-sm px-2.5 text-neutral-500 font-normal">Wishlist (0)</span>
			<span
				class="h-full relative after:h-[14px] after:w-[1px] after:bg-neutral-300 after:content-[''] after:absolute after:right-0 flex items-center"
			></span>

			<button
				class="ml-2 text-neutral-600 hover:text-neutral-800 w-5 h-5 flex items-center justify-center transition-colors duration-200"
			>
				<svg
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
			</button>
		</div>
	</div>
</template>
