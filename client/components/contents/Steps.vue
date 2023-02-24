<template>
	<!-- component -->
	<div class="w-full py-6">
		<div class="flex">
			<div class="w-1/4">
				<div class="relative mb-2">
					<div
						class="w-6 sm:w-8 h-6 sm:h-8 mx-auto bg-green-500 rounded-full border-2 border-green-500 text-lg text-white flex items-center justify-center"
					>
						<div class="w-1/2 h-1/2">
							<IconsCheck />
						</div>
					</div>
				</div>

				<div class="text-xs text-center md:text-base dark:text-c-mode">Order Placed</div>
			</div>

			<div class="w-1/4">
				<div class="relative mb-2">
					<div
						class="absolute flex align-center items-center align-middle content-center"
						style="width: calc(100% - 2.5rem - 1rem); top: 50%; transform: translate(-50%, -50%)"
					>
						<div class="w-full bg-gray-200 rounded items-center align-middle align-center flex-1">
							<div class="w-0 bg-green-300 py-[1px] sm:py-0.5 rounded" style="width: 100%"></div>
						</div>
					</div>

					<div
						class="w-6 sm:w-8 h-6 sm:h-8 mx-auto bg-inherit rounded-full border-2 border-green-500 text-lg text-white flex items-center justify-center"
					>
						<div class="w-1/2 h-1/2 bg-green-500 rounded-full"></div>
					</div>
				</div>

				<div class="text-xs text-center md:text-base dark:text-c-mode">Confirmed</div>
			</div>

			<div class="w-1/4">
				<div class="relative mb-2">
					<div
						class="absolute flex align-center items-center align-middle content-center"
						style="width: calc(100% - 2.5rem - 1rem); top: 50%; transform: translate(-50%, -50%)"
					>
						<div class="w-full bg-gray-200 rounded items-center align-middle align-center flex-1">
							<div class="w-0 bg-green-300 py-[1px] sm:py-0.5 rounded" style="width: 40%"></div>
						</div>
					</div>

					<div
						class="w-6 sm:w-8 h-6 sm:h-8 mx-auto bg-white border-2 border-gray-300 rounded-full text-lg text-white flex items-center justify-center dark:bg-inherit dark:border-neutral-400"
					>
						<div class="w-1/2 h-1/2 bg-gray-300 rounded-full dark:bg-neutral-400"></div>
					</div>
				</div>

				<div class="text-xs text-center md:text-base dark:text-c-mode">Processed</div>
			</div>

			<div class="w-1/4">
				<div class="relative mb-2">
					<div
						class="absolute flex align-center items-center align-middle content-center"
						style="width: calc(100% - 2.5rem - 1rem); top: 50%; transform: translate(-50%, -50%)"
					>
						<div class="w-full bg-gray-200 rounded items-center align-middle align-center flex-1">
							<div class="w-0 bg-green-300 py-[1px] sm:py-0.5 rounded" style="width: 0%"></div>
						</div>
					</div>

					<div
						class="w-6 sm:w-8 h-6 sm:h-8 mx-auto bg-white border-2 border-gray-300 rounded-full text-lg text-white flex items-center justify-center dark:bg-inherit dark:border-neutral-400"
					>
						<div class="w-1/2 h-1/2 bg-gray-300 rounded-full dark:bg-neutral-400"></div>
					</div>
				</div>

				<div class="text-xs text-center md:text-base dark:text-c-mode">Delivered</div>
			</div>
		</div>
	</div>
</template>
