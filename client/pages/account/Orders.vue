<template>
    <section class="w-full flex flex-col text-dark px-8 gap-y-6">
        <div class="display-empty w-full flex flex-col gap-y-8 py-2">
            <header class="flex flex-row w-full justify-between items-center">
                <h3 class="text-2xl tracking-wide font-semibold">Orders</h3>
            </header>
            <div class="empty-context w-full min-h-[12rem] bg-white rounded shadow py-6 flex flex-col gap-y-1 items-center justify-center">
                <div class="img-label flex items-center justify-center">
                    <img src="~/assets/images/Icons/orders.svg" alt="" />
                </div>
                <article class="flex flex-col gap-y-3 justify-center items-center">
                    <h3 class="text-xl font-bold">Your orders will show here</h3>
                    <p class="text-neutral-500 text-sm">
                        To get orders and accept payment from customers, you need to add and sell your products.
                    </p>
                    <button
                        class="py-1 px-4 text-base tracking-wide bg-orange-500 text-gray-50 rounded-sm hover:bg-opacity-90 transition-colors duration-200"
                    >
                        Sell products
                    </button>
                </article>
            </div>
        </div>
    </section>
</template>
