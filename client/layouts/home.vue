<template>
    <section id="home-nav" class="w-full h-full flex flex-col gap-y-1.5">
        <nav>
            <LayoutHomeNavBar />
        </nav>
        <main class="w-full flex flex-col">
            <slot />
        </main>
        <footer>
            <LayoutFooterView />
        </footer>
    </section>
</template>
