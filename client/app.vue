<script setup lang="ts">
useHead({
	title: "Ecommerce",
	meta: [{ name: "description", content: "Full app ecommerce" }],
	link: [
		{ href: "https://fonts.googleapis.com", rel: "preconnect" },
		{ href: "https://fonts.gstatic.com", rel: "preconnect" },
		{
			href: 'https://fonts.googleapis.com/css2?family=Inter:wght@200;400;600;800&display=swaphttps://fonts.googleapis.com/css2?family=Inter:wght@200;300;400;500;600;700;800&display=swap" rel="stylesheet',
		},
	],
});
</script>
<template>
	<NuxtLayout>
		<NuxtLoadingIndicator />
		<NuxtPage />
	</NuxtLayout>
</template>
