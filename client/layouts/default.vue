<template>
	<main class="w-full flex flex-col text-neutral-800 pb-16 md:pb-0">
		<NavsNavTop />
		<slot />
		<!-- <div id="break" class="py-8 w-full"></div> -->
		<NavsNavBottom />
		<Footer />

		<!-- Cart floating container -->
		<div
			class="fixed right-0 bottom-1/2 translate-y-1/2 hidden md:flex flex-col gap-y-2 py-3 pl-3 pr-1 rounded-l-xl bg-custom cursor-pointer"
		>
			<div class="flex flex-row justify-between items-center gap-x-2 text-c-base">
				<div class="w-5 h-5">
					<IconsCart />
				</div>
				<div class="flex flex-row items-center gap-x-1">
					<span class="text-sm tracking-wide leading-tight">0</span>
					<span class="text-sm tracking-wide leading-tight">items(s)</span>
				</div>
			</div>
			<div class="flex flex-col w-full">
				<button class="bg-c-base py-1.5 px-2 rounded text-custom text-sm tracking-wide w-full">$0.00</button>
			</div>
		</div>
	</main>
</template>
