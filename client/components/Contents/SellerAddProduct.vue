<script setup lang="ts">
import { QuillEditor } from '@vueup/vue-quill';
import '@vueup/vue-quill/dist/vue-quill.snow.css';

const emits = defineEmits<{
    (e: 'toggleAddProductsForm'): void;
}>();

const description = ref<string>('<p>Content of the editor.</p>');
</script>
<template>
    <main class="w-full flex flex-col gap-y-4 py-6">
        <header class="w-full items-center flex gap-x-4 flex-row">
            <div
                @click="emits('toggleAddProductsForm')"
                class="icon p-1 rounded-sm flex items-center justify-center ring-1 ring-neutral-300 cursor-pointer hover:bg-neutral-100 hover:opacity-80"
            >
                <div class="i-carbon-arrow-left text-neutral-700 text-xl sm:text-2xl"></div>
            </div>
            <h3 class="text-xl sm:text-2xl font-bold tracking-wide">Add product</h3>
        </header>
        <div class="form-body grid grid-cols-1 md:grid-cols-10 gap-x-6 gap-y-4">
            <div class="main-forms md:col-span-7 flex flex-col gap-y-8">
                <div class="title w-full min-h-[6rem] flex flex-col gap-y-3 px-4 py-4 rounded bg-gray-50 shadow">
                    <div class="name flex flex-col w-full gap-y-2">
                        <h5 class="text-base tracking-wide">Title</h5>
                        <input type="text" name="name" id="name" />
                    </div>
                    <div class="name flex flex-col w-full gap-y-2">
                        <h5 class="text-base tracking-wide">Description</h5>
                        <ClientOnly>
                            <QuillEditor theme="snow" toolbar="full" v-model:content="description" class="min-h-[12rem]" />
                        </ClientOnly>
                    </div>
                </div>

                <div class="media w-full min-h-[6rem] flex flex-col gap-y-2 px-4 py-4 rounded bg-gray-50 shadow">
                    <h5 class="text-base font-semibold tracking-wide">Media</h5>
                    <div
                        class="media-body flex flex-col items-center justify-center w-full min-h-[8rem] border-dashed border border-neutral-400 rounded-md px-3 py-2"
                    >
                        <div class="flex flex-col gap-y-3">
                            <div class="flex flex-row gap-x-4 items-center justify-center">
                                <button
                                    class="text-[steelblue] font-semibold tracking-wide text-sm px-2 py-0.5 rounded bg-blue-400 bg-opacity-20 hover:bg-opacity-40 transition duration-200"
                                >
                                    Add files
                                </button>
                            </div>
                            <small class="text-neutral-500 text-sm">Accepts images or videos</small>
                        </div>
                        <!-- <div
                                class="imgs grid grid-cols-4"
                            ></div> -->
                    </div>
                </div>

                <div class="prices w-full min-h-[6rem] flex flex-col gap-y-3 px-4 py-4 rounded bg-gray-50 shadow">
                    <h5 class="text-base font-semibold tracking-wide">Pricing</h5>
                    <div class="price flex flex-col w-full gap-y-2">
                        <h5 class="text-sm tracking-wide">Price</h5>
                        <input type="text" name="price" id="price" placeholder="KES 0.00" />
                    </div>
                    <div class="cost flex flex-col w-full gap-y-2">
                        <h5 class="text-sm tracking-wide">Cost per item</h5>
                        <input type="text" name="cost" id="cost" placeholder="KES 0.00" />
                        <small class="text-sm text-neutral-500">Customers won't see this</small>
                    </div>
                </div>

                <div class="prices w-full min-h-[6rem] flex flex-col gap-y-3 py-4 rounded bg-gray-50 shadow">
                    <h5 class="text-base font-semibold tracking-wide px-4">Shipping</h5>
                    <div class="ship-status w-full flex flex-row gap-x-2 items-center pb-4 pt-2 px-4 border-b border-neutral-200">
                        <input type="checkbox" id="ship" />
                        <label for="ship" class="text-sm">This is a physical product</label>
                    </div>
                    <div class="price flex flex-col w-full gap-y-2 px-4">
                        <h5 class="text-sm tracking-wide">County/Region</h5>
                        <input type="text" name="price" id="price" placeholder="Select county/region" />
                    </div>
                </div>
            </div>
            <!-- Other form features -->
            <div class="other-forms md:col-span-3 flex flex-col gap-y-6">
                <div class="status w-full flex flex-col gap-y-3 px-4 py-4 rounded bg-gray-50 shadow">
                    <h5 class="text-base font-semibold tracking-wide">Product status</h5>
                    <div class="select w-full flex flex-col">
                        <button
                            class="w-full px-3 py-1 ring-1 ring-neutral-200 hover:ring-neutral-300 focus:ring-neutral-300 rounded text-start transition duration-200"
                        >
                            <span class="text-sm tracking-wide text-neutral-600">Active</span>
                        </button>
                    </div>
                    <small class="text-sm font-light text-neutral-500">This product will be available for sale.</small>
                </div>

                <div class="status w-full flex flex-col gap-y-3 px-4 py-4 rounded bg-gray-50 shadow">
                    <h5 class="text-base font-semibold tracking-wide">Product organization</h5>
                    <div class="category flex flex-col w-full gap-y-2">
                        <h5 class="text-sm tracking-wide">Product Category</h5>
                        <input type="text" name="category" id="category" placeholder="Search product category" />
                    </div>
                    <div class="type flex flex-col w-full gap-y-2">
                        <h5 class="text-sm tracking-wide">Product Type</h5>
                        <input type="text" name="type" id="type" placeholder="e.g Shoes" />
                    </div>
                    <div class="tag flex flex-col w-full gap-y-2">
                        <h5 class="text-sm tracking-wide">Tags</h5>
                        <input type="text" name="tag" id="tag" placeholder="Find or create tags" />
                    </div>
                </div>
            </div>
        </div>
        <div class="submit w-full flex flex-row gap-x-8 py-8 px-4 items-center">
            <button
                class="px-8 py-1.5 text-lg tracking-wide text-gray-50 font-bold bg-teal-500 rounded-3xl hover:bg-opacity-80 focus:bg-opacity-80 duration-200"
            >
                Save
            </button>
            <button
                class="px-8 py-1.5 text-lg tracking-wide text-gray-50 font-bold bg-teal-500 rounded-3xl hover:bg-opacity-80 focus:bg-opacity-80 duration-200"
            >
                Save and add another
            </button>
        </div>
    </main>
</template>

<style scoped>
.main-forms input[type='text'],
.other-forms input[type='text'] {
    @apply outline-none rounded-sm bg-inherit px-3 py-1.5 text-base tracking-wide ring-1 ring-neutral-200 hover:ring-neutral-400 focus:ring-neutral-400 transition duration-200;
}
.main-forms input[type='checkbox'] {
    @apply w-4 h-4 appearance-none first:border rounded-sm border-gray-300;
    @apply flex items-center justify-center checked:after:content-['\2713'] after:text-lg checked:bg-teal-900 checked:border-none checked:after:text-gray-50;
}
</style>
