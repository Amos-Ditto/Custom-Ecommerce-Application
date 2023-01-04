<template>
    <div
        class="cart-dropdown flex flex-col w-[80vw] sm:min-w-[22rem] sm:max-w-[12vw] sm:w-auto min-h-[10rem] h-[100vh] overflow-y-auto bg-white shadow rounded z-50 px-2 pb-14 sm:pb-10 fixed top-0 right-0 text-dark"
    >
        <div class="cart-header flex flex-row items-center justify-between px-2 py-3 border-b border-neutral-200 sticky top-0 bg-white">
            <div class="cart-title flex flex-row gap-x-2 items-center text-neutral-600">
                <h3 class="text-base sm:text-lg font-bold">My Cart</h3>
                <span class="text-sm sm:text-base tracking-wide font-bold">(1)</span>
            </div>
            <div
                class="redirect-cart flex flex-row gap-x-1 items-center text-[dodgerblue] hover:text-[steelblue] transition-colors duration-200 cursor-pointer"
            >
                <span class="text-sm sm:text-base">View</span>
                <div class="i-carbon-arrow-right text-base transition-transform duration-200"></div>
            </div>
        </div>
        <ul class="flex flex-col w-full gap-y-1 pb-3">
            <CardsCartList />
            <CardsCartList />
            <CardsCartList />
            <CardsCartList />
            <CardsCartList />
            <CardsCartList />
            <CardsCartList />
            <CardsCartList />
            <CardsCartList />
        </ul>
    </div>
</template>

<style scoped>
.cart-dropdown ul li {
    @apply py-1 px-1 grid grid-cols-10 gap-x-1 border-b border-neutral-200 last:border-b-0;
}

.redirect-cart:hover .i-carbon-arrow-right {
    @apply translate-x-0.5;
}

::-webkit-scrollbar {
    width: 2px;
    height: 5px;
    border-radius: 32px;
}
::-webkit-scrollbar-corner {
    background-color: #f9fbff;
}
::-webkit-scrollbar-thumb {
    @apply bg-neutral-400;
    border-radius: 32px;
}
::-webkit-scrollbar-track {
    background-color: #f9fbff;
}
</style>
