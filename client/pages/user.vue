<template>
	<main class="w-full flex flex-col px-4 md:px-8 lg:px-20 2xl:px-44 mb-6">
		<section class="w-full grid grid-cols-12 gap-x-6 py-2">
			<aside class="col-span-3 flex flex-col">
				<NavsUserAside />
			</aside>
			<div class="w-full col-span-9 flex flex-col">
				<NuxtPage />
			</div>
		</section>
	</main>
</template>
