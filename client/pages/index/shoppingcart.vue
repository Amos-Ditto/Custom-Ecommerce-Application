<template>
    <section class="w-full flex flex-col">
        <div id="details " class="grid grid-cols-10 gap-x-10 py-3 px-2 sm:px-4 xl:px-8 2xl:px-20">
            <div class="col-span-7 flex flex-col gap-y-4">
                <div id="header-cart" class="w-full flex flex-col gap-y-4 pt-4 pb-3 px-6 bg-gray-50 shadow-sm rounded">
                    <h3 class="text-gray-900 font-semibold text-2xl">Shopping cart (1)</h3>
                    <div class="w-full flex flex-row justify-between items-center">
                        <div class="flex items-center flex-row gap-x-2">
                            <input
                                id="default-checkbox"
                                type="checkbox"
                                value=""
                                class="w-5 h-5 text-amber-500 bg-gray-100 border-gray-300 rounded focus:ring-amber-500 focus:ring-2"
                            />
                            <label for="default-checkbox" class="text-base font-light text-gray-900"> Select all items</label>
                        </div>
                        <div class="flex flex-row gap-x-4 justify-end items-center">
                            <button class="text-sm font-semibold px-3 py-1 capitalize opacity-60 hover:opacity-100 transition duration-200">
                                delete
                            </button>
                        </div>
                    </div>
                </div>
                <div class="flex flex-col gap-y-6">
                    <CardsCartItem />
                    <CardsCartItem />
                </div>
            </div>
            <div class="col-span-3 flex flex-col sticky top-0">
                <div class="bg-gray-50 shadow-sm rounded w-full flex flex-col gap-y-4 py-4 px-3">
                    <h4 class="text-gray-900 font-semibold text-2xl">Summary</h4>
                    <div class="w-full flex flex-row items-center justify-between">
                        <small class="text-sm font-semibold tracking-wide">Total</small>
                        <span class="text-xl font-semibold tracking-wide">KES 0.00</span>
                    </div>
                    <div class="w-full flex flex-row items-center">
                        <button
                            class="bg-amber-500 rounded-3xl text-gray-50 text-lg tracking-wide font-semibold capitalize w-full py-2 bg-opacity-60 hover:bg-opacity-80 transition duration-200"
                        >
                            checkout
                        </button>
                    </div>
                </div>
            </div>
        </div>
    </section>
</template>

<style scoped></style>
