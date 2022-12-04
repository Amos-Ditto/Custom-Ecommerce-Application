<template>
    <div class="side-container px-2 lg:px-3 xl:px-4 py-4 ring-1 ring-neutral-300 rounded-md flex flex-col gap-y-3">
        <h3 class="text-dark tracking-wide font-bold text-base xl:text-lg">Filter</h3>

        <div class="supplier-types w-full flex flex-col gap-y-2 pt-2">
            <h4 class="text-sm xl:text-base font-semibold tracking-wide text-dark">Supplier Types</h4>
            <div class="seller-category w-full">
                <label for="assured" class="flex flex-row gap-x-2 xl:gap-x-3 items-center py-2">
                    <input
                        type="checkbox"
                        name="assured"
                        id="assured"
                        class="checked:bg-orange-400 checked:border-none checked:after:text-gray-50"
                    />
                    <div class="seller flex flex-row gap-x-1 xl:gap-x-2 w-full items-center" id="assured">
                        <div class="flex items-center justify-center w-5 xl:w-6 h-5 xl:h-6 text-amber-500">
                            <IconsCrownIcon />
                        </div>
                        <small class="text-xs xl:text-sm text-gray-700 tracking-wide">Trade Assurance</small>
                    </div>
                </label>
                <label for="verified" class="flex flex-row gap-x-2 xl:gap-x-3 items-center py-2">
                    <input
                        type="checkbox"
                        name="verified"
                        id="verified"
                        class="checked:bg-orange-400 checked:border-none checked:after:text-gray-50"
                    />
                    <div class="seller flex flex-row gap-x-1 xl:gap-x-2 w-full items-center">
                        <div class="flex items-center justify-center w-5 xl:w-6 h-5 xl:h-6 text-[dodgerblue]">
                            <IconsVerifiedIcon />
                        </div>
                        <small class="text-xs xl:text-sm text-gray-700 tracking-wide">Verified Sellers</small>
                    </div>
                </label>
            </div>
        </div>

        <div class="condition-types w-full flex flex-col gap-y-2 pt-2">
            <h4 class="text-sm xl:text-base font-semibold tracking-wide text-dark">Condition</h4>
            <div class="condition-category w-full">
                <label for="new-stuff" class="flex flex-row gap-x-3 items-center py-2">
                    <input
                        type="checkbox"
                        name="new-stuff"
                        id="new-stuff"
                        class="checked:bg-orange-400 checked:border-none checked:after:text-gray-50"
                    />
                    <div class="seller flex flex-row gap-x-2 w-full items-center">
                        <small class="text-xs xl:text-sm text-gray-700 tracking-wide">New Stuff</small>
                    </div>
                </label>
                <label for="second-hand" class="flex flex-row gap-x-3 items-center py-2">
                    <input
                        type="checkbox"
                        name="second-hand"
                        id="second-hand"
                        class="checked:bg-orange-400 checked:border-none checked:after:text-gray-50"
                    />
                    <div class="seller flex flex-row gap-x-2 w-full items-center">
                        <small class="text-xs xl:text-sm text-gray-700 tracking-wide">Second Hand</small>
                    </div>
                </label>
            </div>
        </div>

        <div class="prices w-full flex flex-col gap-y-3 pt-2">
            <h4 class="text-sm xl:text-base font-semibold tracking-wide text-dark">Price</h4>
            <div class="price-inputs flex flex-col gap-y-3 w-full">
                <div class="input flex flex-row w-full">
                    <div class="icon flex justify-center items-center bg-gray-200 rounded-l px-2 py-1 ring-1 ring-neutral-200">
                        <div class="flex items-center justify-center w-5 xl:w-6 h-5 xl:h-6 text-neutral-400">
                            <IconsCoinIcon />
                        </div>
                    </div>
                    <input type="text" name="low-price" id="low-price" placeholder="10" />
                </div>
                <div class="input flex flex-row w-full">
                    <div class="icon flex justify-center items-center bg-gray-200 rounded-l px-2 py-1 ring-1 ring-neutral-200">
                        <div class="flex items-center justify-center w-5 xl:w-6 h-5 xl:h-6 text-neutral-400">
                            <IconsCoinIcon />
                        </div>
                    </div>
                    <input type="text" name="low-price" id="low-price" placeholder="200" />
                </div>
            </div>
            <div class="price-groups flex flex-col gap-y-3 w-full">
                <button>Under - $500</button>
                <button>$500 - $1000</button>
                <button>$1000 - $1500</button>
            </div>
        </div>
    </div>
</template>

<style scoped>
.seller-category label input[type='checkbox'],
.condition-category label input[type='checkbox'] {
    @apply w-5 w-5 h-5 h-5 appearance-none first:border rounded-sm border-gray-300;
    @apply flex items-center justify-center checked:after:content-['\2713'] checked:after:text-xl;
}

.price-inputs input {
    @apply w-full bg-inherit ring-1 ring-neutral-200 rounded-r outline-none px-3 text-dark text-base tracking-wide;
}

.price-groups button {
    @apply border border-neutral-200 rounded text-neutral-500 tracking-wide w-full px-3 py-1.5 xl:py-1 flex flex-row justify-start text-xs xl:text-sm hover:bg-gray-100 hover:border-neutral-300 transition duration-200;
}
</style>
