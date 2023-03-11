<script setup lang="ts">
useHead({
	title: "Ecommerce",
	meta: [{ name: "description", content: "Full app ecommerce" }],
	link: [
		{ href: "https://fonts.googleapis.com", rel: "preconnect" },
		{ href: "https://fonts.gstatic.com", rel: "preconnect" },
		{
			href: "https://fonts.googleapis.com/css2?family=Inter:wght@200;400;600;800&display=swap",
			rel: "stylesheet",
		},
	],
});
if (process.client) {
	await new Promise((resolve) => setTimeout(resolve, 2000));
}
</script>
<template>
	<div class="w-full flex flex-col">
		<NuxtLoadingIndicator />
		<NuxtPage />
	</div>
</template>
<style>
.page-enter-active,
.page-leave-active {
	transition: all 0.4s;
}
.page-enter-from,
.page-leave-to {
	opacity: 0;
	filter: blur(1rem);
}
</style>
