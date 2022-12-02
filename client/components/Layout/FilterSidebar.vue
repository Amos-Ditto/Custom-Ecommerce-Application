<template>
    <div class="side-container px-4 py-4 ring-1 ring-neutral-300 rounded-md flex flex-col gap-y-3">
        <h3 class="text-dark tracking-wide font-bold text-lg">Filter</h3>

        <div class="supplier-types w-full flex flex-col gap-y-2 pt-2">
            <h4 class="text-base font-semibold tracking-wide text-dark">Supplier Types</h4>
            <div class="seller-category flex flex-row gap-x-3 items-center w-full">
                <label for="assured">
                    <input
                        type="checkbox"
                        name="assured"
                        id="assured"
                        class="checked:bg-orange-400 checked:border-none checked:after:text-gray-50"
                    />
                </label>
                <div class="seller flex flex-row gap-x-2 w-full items-center" id="assured">
                    <div class="flex items-center justify-center w-6 h-6 text-orange-500">
                        <IconsCrownIcon />
                    </div>
                    <small class="text-sm text-gray-700 tracking-wide">Trade Assurance</small>
                </div>
            </div>
        </div>
    </div>
</template>

<style scoped>
.seller-category label input[type='checkbox'] {
    @apply w-8 md:w-5 h-8 md:h-5 appearance-none first:border rounded-sm border-gray-300;
    @apply flex items-center justify-center checked:after:content-['\2713'] checked:after:text-xl;
}
</style>
