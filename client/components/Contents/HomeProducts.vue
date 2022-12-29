<script setup lang="ts">
const viewItem = (): void => {
    useRouter().push('/item');
};
</script>
<template>
    <section id="home-products" class="w-full flex flex-col gap-y-2 px-2 lg:px-4 xl:px-8 2xl:px-20 pb-8">
        <div id="products-header" class="w-full flex flex-row items-center gap-x-3 px-0 md:px-4 py-2">
            <div class="w-6 h-6 flex items-center justify-center">
                <img src="~/assets/images/Icons/icon_hot.webp" alt="" class="w-full h-full" />
            </div>
            <h3 class="text-xl sm:text-xl font-bold text-dark tracking-wide">Featured</h3>
        </div>
        <div id="list-products" class="w-full flex flex-col gap-y-2 gap-x-4 px-0 md:px-4">
            <div
                id="products-list"
                class="w-full flex flex-row sm:grid grid-cols-3 md:grid-cols-4 lg:grid-cols-5 xl:grid-cols-6 gap-x-3 gap-y-4 py-1 overflow-x-auto"
            >
                <CardsHomeProductCard>
                    <template #image>
                        <img
                            @click="viewItem"
                            src="~/assets/images/Products/Mens_1.webp"
                            alt="item"
                            class="w-full h-full object-fill rounded-t-md"
                            loading="lazy"
                        />
                    </template>
                </CardsHomeProductCard>
                <CardsHomeProductCard>
                    <template #image>
                        <img
                            @click="viewItem"
                            src="~/assets/images/Products/Lap_2.webp"
                            alt="item"
                            class="w-full h-full object-fill rounded-t-md"
                            loading="lazy"
                        />
                    </template>
                </CardsHomeProductCard>
                <CardsHomeProductCard>
                    <template #image>
                        <img
                            @click="viewItem"
                            src="~/assets/images/Products/Lap_3.webp"
                            alt="item"
                            class="w-full h-full object-fill rounded-t-md"
                            loading="lazy"
                        />
                    </template>
                </CardsHomeProductCard>
                <CardsHomeProductCard>
                    <template #image>
                        <img
                            @click="viewItem"
                            src="~/assets/images/Products/Phone_2.webp"
                            alt="item"
                            class="w-full h-full object-fill rounded-t-md"
                            loading="lazy"
                        />
                    </template>
                </CardsHomeProductCard>
                <CardsHomeProductCard>
                    <template #image>
                        <img
                            @click="viewItem"
                            src="~/assets/images/Products/Lap_4.webp"
                            alt="item"
                            class="w-full h-full object-fill rounded-t-md"
                            loading="lazy"
                        />
                    </template>
                </CardsHomeProductCard>
                <CardsHomeProductCard>
                    <template #image>
                        <img
                            @click="viewItem"
                            src="~/assets/images/Products/Mens_1.webp"
                            alt="item"
                            class="w-full h-full object-fill rounded-t-md"
                            loading="lazy"
                        />
                    </template>
                </CardsHomeProductCard>
                <CardsHomeProductCard>
                    <template #image>
                        <img
                            @click="viewItem"
                            src="~/assets/images/Products/Phone_2.webp"
                            alt="item"
                            class="w-full h-full object-fill rounded-t-md"
                            loading="lazy"
                        />
                    </template>
                </CardsHomeProductCard>
                <CardsHomeProductCard>
                    <template #image>
                        <img
                            @click="viewItem"
                            src="~/assets/images/Products/Lap_4.webp"
                            alt="item"
                            class="w-full h-full object-fill rounded-t-md"
                            loading="lazy"
                        />
                    </template>
                </CardsHomeProductCard>
                <CardsHomeProductCard>
                    <template #image>
                        <img
                            @click="viewItem"
                            src="~/assets/images/Products/Mens_1.webp"
                            alt="item"
                            class="w-full h-full object-fill rounded-t-md"
                            loading="lazy"
                        />
                    </template>
                </CardsHomeProductCard>
                <CardsHomeProductCard>
                    <template #image>
                        <img
                            @click="viewItem"
                            src="~/assets/images/Products/Mens_1.webp"
                            alt="item"
                            class="w-full h-full object-fill rounded-t-md"
                            loading="lazy"
                        />
                    </template>
                </CardsHomeProductCard>
                <CardsHomeProductCard>
                    <template #image>
                        <img
                            @click="viewItem"
                            src="~/assets/images/Products/Lap_2.webp"
                            alt="item"
                            class="w-full h-full object-fill rounded-t-md"
                            loading="lazy"
                        />
                    </template>
                </CardsHomeProductCard>
                <CardsHomeProductCard>
                    <template #image>
                        <img
                            @click="viewItem"
                            src="~/assets/images/Products/Phone_3.webp"
                            alt="item"
                            class="w-full h-full object-fill rounded-t-md"
                            loading="lazy"
                        />
                    </template>
                </CardsHomeProductCard>
            </div>
            <div id="load-more" class="w-full flex flex-row items-center py-4 justify-center">
                <button
                    class="bg-gradient-to-r from-orange-500 to-amber-500 hover:bg-gradient-to-l focus:bg-gradient-to-l rounded-3xl px-12 py-2 text-base text-gray-50 tracking-wide transition duration-200"
                >
                    View more
                </button>
            </div>
        </div>
    </section>
</template>

<style scoped>
::-webkit-scrollbar {
    width: 0px;
    height: 1px;
    border-radius: 32px;
}
::-webkit-scrollbar-thumb {
    @apply bg-neutral-400;
    border-radius: 32px;
}
::-webkit-scrollbar-track {
    background-color: #f9fbff;
}
</style>
