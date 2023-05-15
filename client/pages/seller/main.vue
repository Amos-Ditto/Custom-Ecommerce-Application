<script setup lang="ts"></script>
<template>
	<div class="w-full flex flex-col bg-[#f4f5ff]">
		<NuxtLayout name="seller">
			<NuxtLoadingIndicator />
			<section class="w-full grid grid-cols-12 gap-x-4 px-6 h-[calc(100vh-80px)] mt-1">
				<div class="col-span-3 lg:col-span-2 h-full flex flex-col overflow-y-auto pr-0.5">
					<NavsSellerAsidebar />
				</div>
				<div class="col-span-9 lg:col-span-10 h-full w-full flex flex-col overflow-y-auto pr-1.5 pb-4">
					<NuxtPage
						:transition="{
							name: 'page',
							mode: 'out-in',
						}"
					/>
					<footer class="w-full flex flex-col items-center justify-center py-2 mt-6">
						<span class="text-base text-neutral-600">@The Shop</span>
					</footer>
				</div>
			</section>
		</NuxtLayout>
	</div>
</template>
<style scoped>
::-webkit-scrollbar {
	width: 3px;
}

.page-enter-active,
.page-leave-active {
	transition: all 0.25s;
}
.page-enter-from,
.page-leave-to {
	opacity: 0;
	filter: blur(1rem);
}
</style>
