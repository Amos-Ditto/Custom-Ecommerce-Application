<template>
    <section class="w-full h-full flex flex-col gap-y-1.5">
        <nav>
            <LayoutHomeNavBar />
        </nav>
        <main class="w-full flex flex-col">
            <slot />
        </main>
    </section>
</template>
