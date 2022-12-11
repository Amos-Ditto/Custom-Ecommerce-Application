<template>
    <main class="w-full grid grid-cols-10 gap-x-4 grid-rows-1 min-h-screen">
        <aside class="col-span-2 flex flex-col py-2 border-r border-neutral-300">
            <LayoutAccountSidebar />
        </aside>
        <div class="body-context col-span-8 py-2 flex flex-col">
            <slot />
        </div>
    </main>
</template>
