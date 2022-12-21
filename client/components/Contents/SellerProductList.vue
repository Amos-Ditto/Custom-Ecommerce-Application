<script setup lang="ts">
const emits = defineEmits<{
    (e: 'toggleAddProductsForm'): void;
}>();
</script>
<template>
    <section class="w-full flex flex-col gap-y-4">
        <header class="flex flex-row w-full justify-between items-center">
            <h3 class="text-xl sm:text-2xl tracking-wide font-semibold">Products</h3>
            <div class="actions flex flex-row items-center gap-x-4">
                <button
                    @click="emits('toggleAddProductsForm')"
                    class="px-4 py-2 text-base rounded bg-neutral-800 text-gray-50 tracking-wide flex flex-row items-center gap-x-2 hover:bg-opacity-80 transition duration-200"
                >
                    <div class="i-carbon-add text-xl"></div>
                    Add product
                </button>
            </div>
        </header>
        <div class="table-context w-full min-h-[10rem] py-1 flex flex-col gap-y-2 rounded bg-white shadow">
            <div class="table-header w-full border-b border-neutral-200 flex flex-row gap-x-3 px-4 pt-2">
                <button>All</button>
                <button>Active</button>
                <button>Draft</button>
                <button>Archived</button>
            </div>
            <div class="list-filters w-full py-2 px-4 grid grid-cols-10 gap-x-4">
                <div class="search-input col-span-6 lg:col-span-5 flex flex-row relative items-center">
                    <input type="search" name="filter" id="filter" placeholder="Filter products" />
                    <div class="icon w-5 text-neutral-600 flex items-center absolute left-2.5">
                        <IconsSearchIcon />
                    </div>
                </div>
                <div class="filters col-span-4 lg:col-span-5 flex flex-row gap-x-3 items-center justify-end lg:justify-between">
                    <div class="filter-items hidden lg:flex flex-row justify-end px-1">
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
                    <div class="flex flex-row items-center gap-x-2 ms:gap-x-4 justify-end">
                        <div class="mob-filters lg:hidden flex flex-row items-center">
                            <button
                                class="py-2 px-2 whitespace-nowrap text-sm text-neutral-600 tracking-wide ring-1 ring-neutral-200 rounded hover:ring-neutral-300 focus:ring-neutral-400"
                            >
                                More filters
                            </button>
                        </div>
                        <div class="submit-filters flex flex-row items-center justify-end gap-x-2">
                            <button class="px-4 py-2 rounded bg-[steelblue] text-gray-50 text-sm tracking-wide">Done</button>
                        </div>
                    </div>
                </div>
            </div>
            <div class="product-table w-full overflow-x-auto flex flex-col">
                <table class="table table-auto min-w-full w-full whitespace-nowrap">
                    <thead>
                        <tr>
                            <th>
                                <input type="checkbox" id="product" />
                            </th>
                            <th>
                                <span class="hidden">Image</span>
                            </th>
                            <th><small class="text-neutral-500 tracking-wide text-sm font-light">Product</small></th>
                            <th><small class="text-neutral-500 tracking-wide text-sm font-light">Status</small></th>
                            <th><small class="text-neutral-500 tracking-wide text-sm font-light">Category</small></th>
                            <th><small class="text-neutral-500 tracking-wide text-sm font-light">Type</small></th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr>
                            <td>
                                <input type="checkbox" id="product" />
                            </td>
                            <td>
                                <div
                                    class="product-img col-span-2 flex items-center justify-center w-12 h-12 ring-1 ring-gray-200 rounded-sm"
                                >
                                    <img src="~/assets/images/Products/Mens_1.webp" alt="" class="w-full h-full" />
                                </div>
                            </td>
                            <td>
                                <p class="text-base col-span-8 line-clamp-2 font-semibold hover:underline cursor-pointer">
                                    Unisex Sherpa Denim Jacket
                                </p>
                            </td>
                            <td>
                                <button class="text-xs px-3 py-1 bg-teal-500 bg-opacity-25 text-dark tracking-wide rounded-3xl">
                                    Active
                                </button>
                            </td>
                            <td>
                                <p class="text-base tracking-wide">Fashion & Clothes</p>
                            </td>
                            <td>
                                <p class="text-base tracking-wide">Jackets</p>
                            </td>
                        </tr>
                        <tr>
                            <td>
                                <input type="checkbox" id="product" />
                            </td>
                            <td class="sticky left-0">
                                <div
                                    class="product-img col-span-2 flex items-center justify-center w-12 h-12 ring-1 ring-gray-200 rounded-sm"
                                >
                                    <img src="~/assets/images/Products/Phone_1.webp" alt="" class="w-full h-full" />
                                </div>
                            </td>
                            <td>
                                <p class="text-base col-span-8 line-clamp-2 font-semibold hover:underline cursor-pointer">
                                    Nokia 6.1 plus original
                                </p>
                            </td>
                            <td>
                                <button class="text-xs px-3 py-1 bg-red-500 bg-opacity-25 text-dark tracking-wide rounded-3xl">
                                    Not active
                                </button>
                            </td>
                            <td>
                                <p class="text-base tracking-wide">Phones & Telecommunications</p>
                            </td>
                            <td>
                                <p class="text-base tracking-wide">Nokia</p>
                            </td>
                        </tr>
                    </tbody>
                </table>
            </div>
        </div>
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
    @apply w-full py-1.5 text-base tracking-wide pl-10 pr-4 ring-1 ring-neutral-200 rounded outline-none hover:ring-neutral-300 focus:ring-neutral-400;
}

.filter-item {
    @apply border border-neutral-200 first:border-r-transparent last:border-l-transparent first:rounded-l last:rounded-r hover:border-neutral-300 focus-within:border-neutral-400 transition duration-200;
}
.filter-item button {
    @apply relative flex flex-row gap-x-1 items-center px-3 py-2 bg-inherit hover:opacity-75 transition duration-200;
    @apply after:absolute after:right-0 after:h-full after:w-[1px] after:bg-gray-200 after:content-[''];
}
.filter-item button span {
    @apply text-sm tracking-wide;
}
.filter-item button .i-carbon-caret-down {
    @apply text-neutral-600;
}

.products-table input[type='checkbox'],
.product-table input[type='checkbox'] {
    @apply w-4 h-4 appearance-none first:border rounded-sm border-gray-300;
    @apply flex items-center justify-center checked:after:content-['\2713'] after:text-lg checked:bg-teal-900 checked:border-none checked:after:text-gray-50;
}

.products-list .t-data {
    @apply last:border-none;
}

.product-table table thead tr {
    @apply border-b border-neutral-200;
}
.product-table table thead tr th {
    @apply pt-1 pb-2 px-2 first:px-4 text-start first:sticky left-0 first:z-10 first:bg-white;
}
.product-table table tbody tr {
    @apply border-b border-neutral-200 last:border-none hover:bg-[#f5f5f5] transition-colors duration-200;
}
.product-table table tbody tr td {
    @apply py-1.5 px-2 first:px-4 first:sticky left-0 first:z-10 bg-inherit first:bg-white;
}
</style>
