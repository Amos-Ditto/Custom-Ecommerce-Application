<template>
    <section class="flex flex-col gap-y-2 px-12 w-full py-8">
        <div class="products-container grid grid-cols-10 w-full gap-x-14">
            <aside class="flex flex-col col-span-2">
                <LayoutFilterSidebar />
            </aside>
            <section class="container col-span-8 flex flex-col gap-y-3 w-full">
                <ContentsFilterHeader />
                <!-- <LazyContentsSearchContent></LazyContentsSearchContent> -->
                <ContentsSearchData />
            </section>
        </div>
    </section>
</template>
