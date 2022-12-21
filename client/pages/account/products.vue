<script setup lang="ts">
const emptyproducts = ref<boolean>(false);
const showproductstable = ref<boolean>(true);
</script>
<template>
    <section class="w-full flex flex-col text-dark px-2 sm:px-4 md:px-8 gap-y-6">
        <div v-if="emptyproducts" class="display-empty w-full flex flex-col gap-y-8 py-2">
            <header class="flex flex-row w-full justify-between items-center">
                <h3 class="text-xl sm:text-2xl tracking-wide font-semibold">Products</h3>
            </header>
            <div class="empty-context w-full min-h-[12rem] bg-white rounded shadow py-6 flex flex-col gap-y-1 items-center justify-center">
                <div class="img-label flex items-center justify-center">
                    <img src="~/assets/images/Icons/products.svg" alt="" />
                </div>
                <article class="flex flex-col gap-y-3 justify-center items-center">
                    <h3 class="text-xl font-bold">What are you selling?</h3>
                    <p class="text-neutral-500 text-sm">Before you open your store, first you need some products.</p>
                    <button
                        class="py-1 px-4 text-base tracking-wide bg-orange-500 text-gray-50 rounded-sm hover:bg-opacity-90 transition-colors duration-200"
                    >
                        Add your products
                    </button>
                </article>
            </div>
        </div>
        <main class="w-full flex flex-col py-4">
            <Transition mode="out-in" name="show-table">
                <ContentsSellerProductList v-if="showproductstable" @toggle-add-products-form="showproductstable = !showproductstable" />

                <LazyContentsSellerAddProduct v-else @toggle-add-products-form="showproductstable = !showproductstable" />
            </Transition>
        </main>
    </section>
</template>

<style scoped>
.show-table-enter-active,
.show-table-leave-active {
    transition: all 0.4s;
}
.show-table-enter-from {
    opacity: 0;
    @apply -translate-y-0.5;
}
.show-table-leave-to {
    opacity: 0;
}
</style>
