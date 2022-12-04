<template>
    <section class="flex flex-col gap-y-2 px-4 xl:px-8 2xl:px-12 w-full py-8">
        <div class="products-container flex flex-col md:grid grid-cols-1 md:grid-cols-10 md:gap-x-6 xl:gap-x-14 w-full">
            <aside class="hidden md:flex flex-col md:col-span-2">
                <LayoutFilterSidebar />
            </aside>
            <section class="col-span-1 md:col-span-8 flex flex-col gap-y-3">
                <ContentsFilterHeader />
                <ContentsSearchData />
            </section>
        </div>
    </section>
</template>
