<script setup lang="ts">
definePageMeta({
	layout: false,
});
const layout = "empty";
</script>
<template>
	<div class="w-full flex flex-col z-0">
		<NuxtLayout name="empty">
			<section class="w-full flex flex-col relative items-center justify-center pt-44">
				<div class="absolute left-0 top-0 right-0 h-screen -z-10">
					<NuxtImg src="/seller-auth.webp" class="w-full h-full" />
				</div>
				<div class="w-[40%] flex flex-col items-center justify-center z-0 bg-c-base backdrop-blur-[100px]">
					<p class="">
						Lorem ipsum, dolor sit amet consectetur adipisicing elit. Quisquam ipsam quia quod in, omnis aliquid! Aliquid
						voluptatibus possimus autem quos eligendi, harum repellat impedit eum magni? Labore autem est omnis!
					</p>
				</div>
			</section>
		</NuxtLayout>
	</div>
</template>
