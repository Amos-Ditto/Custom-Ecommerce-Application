<script setup lang="ts">
import Datepicker from '@vuepic/vue-datepicker';
import '@vuepic/vue-datepicker/dist/main.css';

const date = ref<Date[]>([]);

onMounted(() => {
    const endDate = new Date();
    const stardivate = new Date(new Date().setDate(endDate.getDate() - 30));
    date.value = [stardivate, endDate];
});
</script>
<template>
    <section class="w-full flex flex-col text-dark px-8 gap-y-6">
        <header class="flex flex-col md:flex-row justify-between gap-x-3 gap-y-4 items-start md:items-center py-4 w-full">
            <h3 class="text-2xl tracking-wide font-semibold">Dashboard</h3>
            <div class="dates flex flex-row gap-x-3 items-center py-1 ring-1 ring-neutral-300 rounded-sm bg-zinc-50 shadow-sm">
                <div class="date-labels flex flex-row gap-x-2 items-center relative px-2">
                    <div class="icon w-4 text-neutral-500">
                        <IconsCalendarIcon />
                    </div>
                    <small class="text-sm sm:text-base tracking-wide text-neutral-600">Dates</small>
                </div>
                <Datepicker
                    v-model="date"
                    range
                    multi-calendars
                    :text-size="8"
                    :enable-time-picker="false"
                    class="relative text-sm bg-inherit w-auto flex flex-row items-center gap-x-3"
                    menu-class-name="dp-custom-menu"
                >
                    <template #dp-input="{ value }">
                        <input
                            type="text"
                            :value="value"
                            placeholder="Select date range"
                            class="text-xs sm:text-sm py-1.5 px-2 w-[12rem] md:w-[13rem] bg-neutral-100 text-neutral-600 tracking-wide outline-none hover:ring-[dodgerblue] focus:ring-[dodgerblue] font-sans transition duration-200"
                        />
                    </template>
                    <template #clear-icon="{ clear }">
                        <div class="h-[20px] w-6 mr-1 flex items-center justify-center" @click="clear">
                            <div class="i-carbon-close text-lg"></div>
                        </div>
                    </template>
                </Datepicker>
            </div>
        </header>
        <div class="stats w-full grid grid-cols-3 gap-x-6">
            <div class="sales px-4 py-2 min-h-[6rem] bg-gray-50 rounded-lg flex flex-row items-center gap-x-4 ring-1 ring-neutral-200">
                <div class="logo w-14 h-14 flex items-center justify-center rounded-full bg-gray-100">
                    <div class="icon w-8 text-amber-400">
                        <IconsCartIcon />
                    </div>
                </div>
                <div class="stats-context flex flex-col gap-y-2">
                    <h5 class="text-base text-neutral-500 tracking-wide">Total Sales</h5>
                    <div class="stats-figures flex flex-row gap-x-8 items-center">
                        <div class="figure">
                            <span class="text-2xl tracking-wide font-bold">263k</span>
                        </div>
                        <div class="percentage flex flex-row items-center gap-x-0.5">
                            <div class="i-carbon-arrow-up text-teal-500 text-base"></div>
                            <small class="text-sm tracking-wide text-teal-500">15.6%</small>
                        </div>
                    </div>
                </div>
            </div>
            <div class="visitors px-4 py-2 min-h-[6rem] bg-gray-50 rounded-lg flex flex-row items-center gap-x-4 ring-1 ring-neutral-200">
                <div class="logo w-14 h-14 flex items-center justify-center rounded-full bg-gray-100">
                    <div class="icon w-8 text-amber-400">
                        <IconsUsersIcon />
                    </div>
                </div>
                <div class="stats-context flex flex-col gap-y-2">
                    <h5 class="text-base text-neutral-500 tracking-wide">Total Orders</h5>
                    <div class="stats-figures flex flex-row gap-x-8 items-center">
                        <div class="figure">
                            <span class="text-2xl tracking-wide font-bold">165k</span>
                        </div>
                        <div class="percentage flex flex-row items-center gap-x-0.5">
                            <div class="i-carbon-arrow-down text-tomato text-base"></div>
                            <small class="text-sm tracking-wide text-tomato">6.2%</small>
                        </div>
                    </div>
                </div>
            </div>

            <div class="visitors px-4 py-2 min-h-[6rem] bg-gray-50 rounded-lg flex flex-row items-center gap-x-4 ring-1 ring-neutral-200">
                <div class="logo w-14 h-14 flex items-center justify-center rounded-full bg-gray-100">
                    <div class="icon w-8 text-amber-400">
                        <IconsClipCheckIcon />
                    </div>
                </div>
                <div class="stats-context flex flex-col gap-y-2">
                    <h5 class="text-base text-neutral-500 tracking-wide">Total Visitors</h5>
                    <div class="stats-figures flex flex-row gap-x-8 items-center">
                        <div class="figure">
                            <span class="text-2xl tracking-wide font-bold">2k</span>
                        </div>
                        <div class="percentage flex flex-row items-center gap-x-0.5">
                            <div class="i-carbon-arrow-up text-teal-500 text-base"></div>
                            <small class="text-sm tracking-wide text-teal-500">3.5%</small>
                        </div>
                    </div>
                </div>
            </div>
        </div>
        <!-- <main class="flex flex-col w-full gap-y-2">
            <div class="products-context grid grid-cols-10 gap-x-2">
                <div class="p-div col-span-8 2xl:col-span-7 ring-1 ring-neutral-200 rounded pt-3 flex flex-col gap-y-1">
                    <div class="div-nav px-3 py-2 flex flex-row justify-between items-center">
                        <div class="div-nav-links px-3 py-2 bg-zinc-200 rounded flex flex-row gap-x-2 items-center">
                            <button>All</button>
                            <button>New product</button>
                            <button>archived</button>
                        </div>
                        <div class="others flex flex-row gap-x-3 items-center">
                            <button
                                class="px-3 py-1.5 text-base bg-[dodgerblue] text-gray-50 rounded flex flex-row items-center gap-x-2 hover:bg-opacity-80 transition duration-200"
                            >
                                <div class="i-carbon-add text-white text-lg"></div>
                                Add Product
                            </button>
                        </div>
                    </div>
                    <div class="p-table w-full pt-1">
                        <div class="grid grid-cols-10 py-3 gap-x-3 border-t border-neutral-200 px-3">
                            <div class="col-span-4 flex flex-row gap-x-3 items-center">
                                <input type="checkbox" />
                                <div class="name-group flex flex-row gap-x-1 w-full hover:opacity-80 cursor-pointer">
                                    <small class="text-neutral-500 tracking-wide">Name</small>
                                    <div class="i-carbon-caret-down"></div>
                                </div>
                            </div>
                            <div class="col-span-2 flex flex-row gap-x-1 hover:opacity-80 cursor-pointer">
                                <small class="text-neutral-500 tracking-wide">Product Added</small>
                                <div class="i-carbon-caret-down text-base text-neutral-500"></div>
                            </div>
                            <div class="col-span-2 flex flex-row gap-x-1 hover:opacity-80 cursor-pointer">
                                <small class="text-neutral-500 tracking-wide">Stock</small>
                                <div class="i-carbon-caret-down text-base text-neutral-500"></div>
                            </div>
                            <div class="col-span-2 flex flex-row gap-x-1 hover:opacity-80 cursor-pointer">
                                <small class="text-neutral-500 tracking-wide">Prices</small>
                                <div class="i-carbon-caret-down text-base text-neutral-500"></div>
                            </div>
                        </div>

                        <ul class="w-full flex flex-col gap-y-1">
                            <li>
                                <div class="col-span-4 flex flex-row gap-x-3 items-center">
                                    <input type="checkbox" />
                                    <div class="l-group flex flex-row items-center gap-x-2 w-[80%]">
                                        <div class="img flex items-center justify-center">
                                            <img src="~/assets/images/Products/Mens_1.webp" alt="" />
                                        </div>
                                        <small class="w-[88%] truncate text-sm capitalize"
                                            >Unisex Sherpa Denim Jacket | Threadfast Apparel 372J</small
                                        >
                                    </div>
                                </div>
                                <div class="col">
                                    <div class="icon w-4 text-neutral-500">
                                        <IconsCalendarIcon />
                                    </div>
                                    <small class="tracking-wide text-sm">19 Aug 22</small>
                                </div>
                                <div class="col">
                                    <small class="tracking-wide text-sm">60</small>
                                    <small class="text-blue-600 text-xs py-0.5 px-1.5 rounded bg-blue-100">12 Left</small>
                                </div>
                                <div class="col">
                                    <small class="tracking-wide text-sm">$16</small>
                                    <small class="tracking-wide text-teal-600 text-xs py-0.5 px-1.5 rounded bg-teal-100"
                                        >discount $20</small
                                    >
                                </div>
                                <div class="actions absolute right-3 h-full flex items-center justify-center">
                                    <div class="icon w-4 text-neutral-500 hover:text-dark cursor-pointer">
                                        <IconsDotsIcon />
                                    </div>
                                </div>
                            </li>
                            <li>
                                <div class="col-span-4 flex flex-row gap-x-3 items-center">
                                    <input type="checkbox" />
                                    <div class="l-group flex flex-row items-center gap-x-2 w-[80%]">
                                        <div class="img flex items-center justify-center">
                                            <img src="~/assets/images/Products/Phone_3.webp" alt="" />
                                        </div>
                                        <small class="w-[88%] truncate text-sm capitalize"
                                            >celular 2021NEW Smartphone S21 Cellphone 6.5 Inch 8 Core Smartphone 540*1200 3GB+64GB 16MP+8MP
                                            4150Amh Andriod 11 Cell Phone</small
                                        >
                                    </div>
                                </div>
                                <div class="col">
                                    <div class="icon w-4 text-neutral-500">
                                        <IconsCalendarIcon />
                                    </div>
                                    <small class="tracking-wide text-sm">19 Aug 22</small>
                                </div>
                                <div class="col">
                                    <small class="tracking-wide text-sm">20</small>
                                    <small class="text-tomato text-xs py-0.5 px-1.5 rounded bg-red-100">2 Left</small>
                                </div>
                                <div class="col">
                                    <small class="tracking-wide text-sm">$16</small>
                                    <small class="tracking-wide text-teal-600 text-xs py-0.5 px-1.5 rounded bg-teal-100"
                                        >discount $20</small
                                    >
                                </div>
                                <div class="actions absolute right-3 h-full flex items-center justify-center">
                                    <div class="icon w-4 text-neutral-500 hover:text-dark cursor-pointer">
                                        <IconsDotsIcon />
                                    </div>
                                </div>
                            </li>
                        </ul>
                    </div>
                </div>
                <div class="col-span-2 2xl:col-span-3"></div>
            </div>
        </main> -->
    </section>
</template>

<style scoped>
.date-labels::after {
    content: '';
    @apply bg-neutral-300 w-[1px] h-[80%] absolute right-0;
}

.dates:focus-within {
    @apply ring-orange-500;
}
.div-nav-links button {
    @apply tracking-wide text-sm capitalize px-3 py-1 hover:bg-gray-50 rounded hover:shadow;
    @apply first:bg-gray-50;
}

.p-table input[type='checkbox'],
ul li input[type='checkbox'] {
    @apply w-4 h-4 appearance-none first:border rounded-sm border-gray-300;
    @apply flex items-center justify-center checked:after:content-['\2713'] after:text-lg checked:bg-teal-900 checked:border-none checked:after:text-gray-50;
}

.p-table ul li {
    @apply grid grid-cols-10 gap-x-3 py-3 border-t border-neutral-200 px-3 relative;
}
.p-table ul li .col {
    @apply col-span-2 flex flex-row items-center gap-x-2;
}
li .l-group img {
    @apply w-[30px] h-[30px] rounded-md;
}
</style>
