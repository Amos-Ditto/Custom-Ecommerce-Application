<script setup lang="ts">
import { watch } from "vue";
import { useAppStore } from "./stores/appStore";

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
const store = useAppStore();

const el = ref<HTMLElement | null>(null);
const { y } = useScroll(el, { behavior: "smooth" });
watch(y, (newY) => {
	store.changeHeight(newY);
});
</script>
<template>
	<div ref="el" class="w-full h-screen flex flex-col overflow-y-auto">
		<NuxtPage />
	</div>
</template>
<style>
.page-enter-active,
.layout-enter-active .page-leave-active,
.layout-leave-active {
	transition: all 0.25s;
}
.page-enter-from,
.layout-enter-from .page-leave-to,
.layout-leave-to {
	opacity: 0;
	filter: blur(1rem);
}
</style>
