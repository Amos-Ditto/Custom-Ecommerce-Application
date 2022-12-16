<script setup lang="ts">
import { QuillEditor } from '@vueup/vue-quill';
import '@vueup/vue-quill/dist/vue-quill.snow.css';

const emptyproducts = ref<boolean>(false);

const description = ref<string>('<p>Content of the editor.</p>');
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
                        Add you products
                    </button>
                </article>
            </div>
        </div>
        <main v-else class="w-full flex flex-col gap-y-4 py-6">
            <header class="w-full items-center flex gap-x-4 flex-row">
                <div
                    class="icon p-1 rounded-sm flex items-center justify-center ring-1 ring-neutral-300 cursor-pointer hover:bg-neutral-100 hover:opacity-80"
                >
                    <div class="i-carbon-arrow-left text-neutral-700 text-xl sm:text-2xl"></div>
                </div>
                <h3 class="text-xl sm:text-2xl font-bold tracking-wide">Add product</h3>
            </header>
            <div class="form-body grid grid-cols-10 gap-x-4 gap-y-4">
                <div class="main-forms col-span-6 flex flex-col gap-y-8">
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
                        <h5 class="text-base tracking-wide">Media</h5>
                        <div
                            class="imgs grid grid-cols-4 w-full min-h-[8rem] border-dashed border border-neutral-400 rounded-md px-3 py-2"
                        ></div>
                    </div>
                </div>
            </div>
        </main>
    </section>
</template>

<style scoped>
.main-forms input[type='text'] {
    @apply outline-none rounded-sm bg-inherit px-3 py-1.5 text-base tracking-wide ring-1 ring-neutral-200 hover:ring-neutral-400 focus:ring-neutral-400 transition duration-200;
}
</style>
