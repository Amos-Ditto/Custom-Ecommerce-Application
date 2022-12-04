<template>
    <main>
        <NuxtLayout name="default">
            <section class="hero w-full py-2 px-2 sm:px-4 xl:px-12 2xl:px-32 grid grid-cols-10 gap-x-4 xl:gap-x-6">
                <aside class="col-span-2 flex flex-col">
                    <div class="w-full rounded bg-gray-50 shadow-sm min-h-[10rem]">
                        <LayoutCategoriesSideBar />
                    </div>
                </aside>
                <div
                    class="hero-body w-full min-h-[24rem] bg-[url('assets/images/Banner.webp')] bg-no-repeat bg-top object-cover rounded-md col-span-8"
                ></div>
            </section>
        </NuxtLayout>
    </main>
</template>

<style scoped></style>
