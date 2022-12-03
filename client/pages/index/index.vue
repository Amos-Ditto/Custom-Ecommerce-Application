<template>
    <section class="flex flex-col gap-y-2 px-12 w-full py-8">
        <div class="products-container grid grid-cols-10 w-full gap-x-14">
            <aside class="flex flex-col col-span-2">
                <LayoutFilterSidebar />
            </aside>
            <div class="container col-span-8 flex flex-col gap-y-3">
                <ContentsSearchContent />
            </div>
        </div>
    </section>
</template>
