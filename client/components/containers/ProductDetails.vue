<template>
	<div class="w-full flex flex-col gap-y-8">
		<div class="description w-full flex flex-col gap-y-2 ring-1 ring-neutral-200">
			<button class="w-full bg-custom text-gray-100 flex flex-row justify-between px-8 py-4 text-xl">
				<div class="flex flex-row gap-x-4 items-center">
					<div class="w-8 h-8">
						<svg fill="currentColor" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg" aria-hidden="true">
							<path
								d="M5.625 3.75a2.625 2.625 0 100 5.25h12.75a2.625 2.625 0 000-5.25H5.625zM3.75 11.25a.75.75 0 000 1.5h16.5a.75.75 0 000-1.5H3.75zM3 15.75a.75.75 0 01.75-.75h16.5a.75.75 0 010 1.5H3.75a.75.75 0 01-.75-.75zM3.75 18.75a.75.75 0 000 1.5h16.5a.75.75 0 000-1.5H3.75z"
							></path>
						</svg>
					</div>
					<span class="text-lg font-medium">Description</span>
				</div>
			</button>
			<div class="w-full flex flex-col px-4 py-3">
				<p>
					Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard
					dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen
					book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially
					unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more
					recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.
				</p>
			</div>
		</div>
		<div class="ratings w-full flex flex-col gap-y-2 ring-1 ring-neutral-200">
			<button class="w-full bg-custom text-gray-100 flex flex-row justify-between px-8 py-4 text-xl">
				<div class="flex flex-row gap-x-4 items-center">
					<div class="w-8 h-8">
						<svg fill="currentColor" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg" aria-hidden="true">
							<path
								d="M5.625 3.75a2.625 2.625 0 100 5.25h12.75a2.625 2.625 0 000-5.25H5.625zM3.75 11.25a.75.75 0 000 1.5h16.5a.75.75 0 000-1.5H3.75zM3 15.75a.75.75 0 01.75-.75h16.5a.75.75 0 010 1.5H3.75a.75.75 0 01-.75-.75zM3.75 18.75a.75.75 0 000 1.5h16.5a.75.75 0 000-1.5H3.75z"
							></path>
						</svg>
					</div>
					<span class="text-lg font-medium">Ratings & Reviews</span>
				</div>
			</button>
			<div class="w-full flex flex-col gap-y-4 px-4 py-3">
				<div class="w-full grid grid-cols-2 gap-y-4 py-4">
					<div class="col-span-1 flex flex-col gap-y-1 justify-center items-center border-r border-neutral-200">
						<span class="text-5xl text-neutral-500 leading-tight">3.0</span>
						<span class="text-base font-light leading-tight">Out of 5.00</span>
						<div class="flex flex-row gap-x-0.5 items-center">
							<button class="w-4 h-4 text-yellow-400">
								<IconsStar />
							</button>
							<button class="w-4 h-4 text-yellow-400">
								<IconsStar /></button
							><button class="w-4 h-4 text-yellow-400">
								<IconsStar /></button
							><button class="w-4 h-4 text-yellow-400">
								<IconsStar /></button
							><button class="w-4 h-4 text-gray-300">
								<IconsStar />
							</button>
						</div>
						<span class="text-base">3 ratings</span>
					</div>
					<div class="col-span-1 flex flex-col gap-y-1 justify-center items-center">
						<ul class="flex flex-col gap-y-0">
							<li class="flex flex-row gap-x-2 items-center">
								<div class="flex flex-row gap-x-0.5 items-center">
									<button class="w-3 h-3 text-yellow-400">
										<IconsStar />
									</button>
									<button class="w-3 h-3 text-yellow-400">
										<IconsStar /></button
									><button class="w-3 h-3 text-yellow-400">
										<IconsStar /></button
									><button class="w-3 h-3 text-yellow-400">
										<IconsStar /></button
									><button class="w-3 h-3 text-yellow-400">
										<IconsStar />
									</button>
								</div>
								<span class="text-neutral-500 text-sm">1</span>
							</li>
							<li class="flex flex-row gap-x-2 items-center">
								<div class="flex flex-row gap-x-0.5 items-center">
									<button class="w-3 h-3 text-yellow-400">
										<IconsStar />
									</button>
									<button class="w-3 h-3 text-yellow-400">
										<IconsStar /></button
									><button class="w-3 h-3 text-yellow-400">
										<IconsStar /></button
									><button class="w-3 h-3 text-yellow-400">
										<IconsStar /></button
									><button class="w-3 h-3 text-gray-300">
										<IconsStar />
									</button>
								</div>
								<span class="text-neutral-500 text-sm">0</span>
							</li>
							<li class="flex flex-row gap-x-2 items-center">
								<div class="flex flex-row gap-x-0.5 items-center">
									<button class="w-3 h-3 text-yellow-400">
										<IconsStar />
									</button>
									<button class="w-3 h-3 text-yellow-400">
										<IconsStar /></button
									><button class="w-3 h-3 text-yellow-400">
										<IconsStar /></button
									><button class="w-3 h-3 text-gray-300">
										<IconsStar /></button
									><button class="w-3 h-3 text-gray-300">
										<IconsStar />
									</button>
								</div>
								<span class="text-neutral-500 text-sm">1</span>
							</li>
							<li class="flex flex-row gap-x-2 items-center">
								<div class="flex flex-row gap-x-0.5 items-center">
									<button class="w-3 h-3 text-yellow-400">
										<IconsStar />
									</button>
									<button class="w-3 h-3 text-yellow-400">
										<IconsStar /></button
									><button class="w-3 h-3 text-gray-300">
										<IconsStar /></button
									><button class="w-3 h-3 text-gray-300">
										<IconsStar /></button
									><button class="w-3 h-3 text-gray-300">
										<IconsStar />
									</button>
								</div>
								<span class="text-neutral-500 text-sm">0</span>
							</li>
							<li class="flex flex-row gap-x-2 items-center">
								<div class="flex flex-row gap-x-0.5 items-center">
									<button class="w-3 h-3 text-yellow-400">
										<IconsStar />
									</button>
									<button class="w-3 h-3 text-gray-300">
										<IconsStar /></button
									><button class="w-3 h-3 text-gray-300">
										<IconsStar /></button
									><button class="w-3 h-3 text-gray-300">
										<IconsStar /></button
									><button class="w-3 h-3 text-gray-300">
										<IconsStar />
									</button>
								</div>
								<span class="text-neutral-500 text-sm">1</span>
							</li>
						</ul>
					</div>
				</div>
			</div>
		</div>
	</div>
</template>
