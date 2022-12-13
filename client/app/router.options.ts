import type { RouterConfig } from '@nuxt/schema';

export default <RouterConfig>{
    routes: (_routes) => [
        {
            name: 'Home',
            path: '/',
            component: () => import('~/pages/index/index.vue'),
        },
    ],
};
