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
            <section v-if="showproductstable" class="w-full flex flex-col gap-y-4">
                <header class="flex flex-row w-full justify-between items-center">
                    <h3 class="text-xl sm:text-2xl tracking-wide font-semibold">Products</h3>
                    <div class="actions flex flex-row items-center gap-x-4">
                        <button
                            class="px-4 py-2 text-base rounded bg-neutral-800 text-gray-50 tracking-wide flex flex-row items-center gap-x-2 hover:bg-opacity-80 transition duration-200"
                        >
                            <div class="i-carbon-add text-xl"></div>
                            Add product
                        </button>
                    </div>
                </header>
                <div class="table-context w-full min-h-[10rem] py-1 flex flex-col gap-y-2 rounded bg-gray-50 shadow">
                    <div class="table-header w-full border-b border-neutral-200 flex flex-row gap-x-3 px-4 pt-2">
                        <button>All</button>
                        <button>Active</button>
                        <button>Draft</button>
                        <button>Archived</button>
                    </div>
                    <div class="list-filters w-full py-2 px-4 grid grid-cols-10 gap-x-4">
                        <div class="search-input col-span-5 flex flex-row relative items-center">
                            <input type="search" name="filter" id="filter" placeholder="Filter products" />
                            <div class="icon w-5 text-neutral-600 flex items-center absolute left-2.5">
                                <IconsSearchIcon />
                            </div>
                        </div>
                        <div class="filters col-span-5 flex flex-row gap-x-3 items-center">
                            <div class="filter-items flex flex-row px-1">
                                <div class="filter-item">
                                    <button>
                                        <span>Product category</span>
                                        <div class="i-carbon-caret-down"></div>
                                    </button>
                                </div>
                                <div class="filter-item">
                                    <button>
                                        <span>Tagged with</span>
                                        <div class="i-carbon-caret-down"></div>
                                    </button>
                                </div>
                                <div class="filter-item">
                                    <button>
                                        <span>Date added</span>
                                        <div class="i-carbon-caret-down"></div>
                                    </button>
                                </div>
                            </div>
                            <div class="submit-filters flex flex-row items-center justify-end gap-x-2">
                                <button class="px-4 py-2.5 rounded bg-[steelblue] text-gray-50 text-sm tracking-wide">Done</button>
                            </div>
                        </div>
                    </div>

                    <div class="products-table w-full flex flex-col">
                        <div class="t-headers w-full grid grid-cols-10 pt-1 pb-2 border-b border-neutral-200">
                            <div class="p-name col-span-4 grid grid-cols-10 px-4 relative">
                                <div class="checkbox col-span-1 flex items-center">
                                    <input type="checkbox" id="ship" />
                                </div>
                                <div class="td-context col-span-9 flex items-center flex-row gap-x-3">
                                    <small class="text-neutral-500 tracking-wide text-sm font-light">Product</small>
                                </div>
                            </div>
                            <div class="s-name col-span-2 flex flex-row items-center px-2">
                                <small class="text-neutral-500 tracking-wide text-sm font-light">Status</small>
                            </div>
                            <div class="c-name col-span-2 flex flex-row items-center px-2">
                                <small class="text-neutral-500 tracking-wide text-sm font-light">Category</small>
                            </div>
                            <div class="t-name col-span-2 flex flex-row items-center px-2">
                                <small class="text-neutral-500 tracking-wide text-sm font-light">Type</small>
                            </div>
                        </div>
                        <div class="products-list w-full flex flex-col">
                            <div class="t-body w-full grid grid-cols-10 py-2 border-b border-neutral-200 text-dark">
                                <div class="td-name col-span-4 grid grid-cols-10 px-4 relative">
                                    <div class="checkbox col-span-1 flex items-center">
                                        <input type="checkbox" id="ship" />
                                    </div>
                                    <div class="td-context-name col-span-9 flex items-center flex-row gap-x-3">
                                        <div class="product-img flex items-center justify-center w-12 h-12 ring-1 ring-gray-200 rounded-sm">
                                            <img src="~/assets/images/Products/Mens_1.webp" alt="" class="w-full h-full" />
                                        </div>
                                        <p class="text-base">Unisex Sherpa Denim Jacket | Threadfast Apparel 372J</p>
                                    </div>
                                </div>
                                <div class="td-status col-span-2 flex flex-row items-center px-2">
                                    <button class="text-sm px-3 py-1 bg-teal-500 bg-opacity-25 text-dark tracking-wide rounded-3xl">
                                        Active
                                    </button>
                                </div>
                                <div class="td-category col-span-2 flex flex-row items-center px-2">
                                    <p class="text-base tracking-wide">Fashion & Clothes</p>
                                </div>
                                <div class="td-type col-span-2 flex flex-row items-center px-2">
                                    <p class="text-base tracking-wide">Jackets</p>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </section>
            <LazyContentsSellerAddProduct v-else />
        </main>
    </section>
</template>
<style scoped>
.table-header button {
    @apply px-2 py-2 first:bg-[length:100%_2px] text-base tracking-wide relative first:text-dark text-neutral-500 hover:text-dark focus:text-dark;
    background-image: linear-gradient(rgb(245 158 11 /1), rgb(245 158 11 /1));
    background-position: 50% 100%;
    background-repeat: no-repeat;
    background-size: 0% 2px;
    transition: background-size 0.15s;
}
.table-header button:hover,
.table-header button:focus {
    background-size: 100% 2px;
}

.search-input input[type='search'] {
    @apply w-full py-2 text-base tracking-wide pl-10 pr-4 ring-1 ring-neutral-200 rounded outline-none hover:ring-neutral-300 focus:ring-neutral-400;
}

.filter-item {
    @apply border border-neutral-200 first:border-r-transparent last:border-l-transparent first:rounded-l last:rounded-r hover:border-neutral-300 focus-within:border-neutral-400 transition duration-200;
}
.filter-item button {
    @apply relative flex flex-row gap-x-1 items-center px-3 py-2.5 bg-inherit hover:opacity-75 transition duration-200;
    @apply after:absolute after:right-0 after:h-full after:w-[1px] after:bg-gray-200 after:content-[''];
}
.filter-item button span {
    @apply text-sm tracking-wide;
}
.filter-item button .i-carbon-caret-down {
    @apply text-neutral-600;
}

.products-table input[type='checkbox'] {
    @apply w-4 h-4 appearance-none first:border rounded-sm border-gray-300;
    @apply flex items-center justify-center checked:after:content-['\2713'] after:text-lg checked:bg-teal-900 checked:border-none checked:after:text-gray-50;
}
</style>
