<template>
	<footer class="w-full flex flex-col mt-4 pt-1 sm:pt-6 pb-4 px-4 md:px-8 lg:px-20 2xl:px-44 bg-[#212121]">
		<div class="w-full flex flex-row gap-x-2 items-center py-2 sm:py-3 border-b border-neutral-700">
			<div class="">
				<NuxtImg src="/logo.png" loading="lazy" class="h-[4rem] opacity-80" />
			</div>
			<h3 class="text-3xl font-extrabold text-neutral-100"><span class="text-custom">S</span>hop</h3>
		</div>
		<div class="w-full grid grid-cols-1 lg:grid-cols-6 gap-y-4 gap-x-12 pt-5 pb-4">
			<div class="lg:col-span-2 flex flex-col gap-y-4 lg:gap-y-7">
				<h4 class="text-base text-custom font-semibold truncate">Get your special offers, Coupons & More...</h4>
				<div class="flex flex-col items-start gap-y-3.5 w-full lg:pt-2">
					<input
						type="email"
						id="email-input"
						class="block w-[80%] sm:w-[56%] lg:w-full p-2 md:p-3 text-gray-800 rounded-sm border border-gray-300 bg-gray-100 text-base md:text-lg focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-blue-500 transition duration-200"
						placeholder="mail@example.com"
					/>
					<button
						type="button"
						class="text-white bg-inherit rounded-sm ring-1 ring-custom focus:ring-4 focus:outline-none font-light text-base md:text-lg px-6 py-2 text-center transition duration-200"
					>
						Subscribe
					</button>
				</div>
			</div>
			<div class="flex flex-col gap-y-4 mt-8 lg:mt-0 border-b border-neutral-700 lg:border-transparent pb-3">
				<h4 class="text-base text-custom font-semibold capitalize">Useful links</h4>
				<ul class="list hidden lg:flex flex-col gap-y-1 px-6 lg:px-0">
					<li>Home</li>
					<li>All categories</li>
					<li>All brands</li>
					<li>all products</li>
					<li>offers</li>
				</ul>
			</div>

			<div class="flex flex-col gap-y-4 border-b border-neutral-700 lg:border-transparent pb-3">
				<h4 class="text-base text-custom font-semibold capitalize">My Account</h4>
				<ul class="list hidden lg:flex flex-col gap-y-1 px-6 lg:px-0">
					<li>Login</li>
					<li>My wishlist</li>
					<li>track order</li>
					<li>my account</li>
				</ul>
			</div>
			<div class="flex flex-col gap-y-4 border-b border-neutral-700 lg:border-transparent pb-3">
				<h4 class="text-base text-custom font-semibold capitalize">contact us</h4>
				<div class="hidden lg:flex flex-col gap-y-4">
					<div class="flex flex-col gap-y-1 px-6 lg:px-0">
						<div class="flex flex-row gap-x-2 items-center text-sm font-extralight text-neutral-500">
							<div class="w-4 h-4">
								<IconsHome />
							</div>
							<span>Address</span>
						</div>
						<p class="text-white text-sm">Kabarak, Nakuru, KE</p>
					</div>
					<div class="flex flex-col gap-y-1 px-6 lg:px-0">
						<div class="flex flex-row gap-x-2 items-center text-sm font-extralight text-neutral-500">
							<div class="w-4 h-4">
								<IconsMail />
							</div>
							<span>Email</span>
						</div>
						<p class="text-white text-sm">amosk7793@gmail.com</p>
					</div>
					<div class="flex flex-col gap-y-1 px-6 lg:px-0">
						<div class="flex flex-row gap-x-2 items-center text-sm font-extralight text-neutral-500">
							<div class="w-4 h-4">
								<IconsPhone />
							</div>
							<span>Phone</span>
						</div>
						<p class="text-white text-sm">+254-794-818-111</p>
					</div>
				</div>
			</div>
			<div class="flex flex-col gap-y-4">
				<h4 class="text-base text-custom font-semibold capitalize">seller zone</h4>
				<ul class="list hidden lg:flex flex-col gap-y-1 px-6 lg:px-0">
					<li>Be a seller</li>
					<li>Login to seller account</li>
				</ul>
			</div>
		</div>
		<div id="rules" class="w-full flex flex-row gap-x-5 sm:gap-x-10 items-center py-4 sm:py-6 border-y border-neutral-700">
			<a href="#">Terms & Condition</a>
			<a href="#">Privacy policy</a>
		</div>
	</footer>
</template>

<style scoped>
.list li {
	@apply text-sm tracking-wide capitalize text-white font-medium py-1.5 hover:opacity-90 cursor-pointer;
}
#rules a {
	@apply text-sm sm:text-base font-medium text-white;
}
</style>
