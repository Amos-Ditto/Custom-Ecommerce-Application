import type { RouterConfig } from '@nuxt/schema';

const home_links = {
    path: '/',
    component: () => import('~/pages/index.vue'),
    name: 'HomeDashBoard',
    children: [
        {
            path: '',
            component: () => import('~/pages/index/index.vue'),
            name: 'Home',
        },
        {
            path: 'item',
            component: () => import('~/pages/index/item.vue'),
            name: 'HomeItem',
        },

        {
            path: 'shoppingcart',
            component: () => import('~/pages/index/shoppingcart.vue'),
            name: 'ShoppingCart',
        },
    ],
};

const search_links = {
    path: '/search',
    component: () => import('~/pages/search.vue'),
    name: 'Search',
    children: [
        {
            path: '',
            component: () => import('~/pages/search/index.vue'),
            name: 'HomeSearch',
        },
    ],
};

const account_links = {
    path: '/account',
    component: () => import('~/pages/account.vue'),
    name: 'Account',
    children: [
        {
            path: '',
            component: () => import('~/pages/account/index.vue'),
            name: 'Account-Dashboard',
        },
        {
            path: 'products',
            component: () => import('~/pages/account/products.vue'),
            name: 'Products',
        },
        {
            path: 'orders',
            component: () => import('~/pages/account/Orders.vue'),
            name: 'Orders',
        },
        {
            path: 'customers',
            component: () => import('~/pages/account/Customers.vue'),
            name: 'Customers',
        },
        {
            path: 'discounts',
            component: () => import('~/pages/account/Discounts.vue'),
            name: 'Discounts',
        },
    ],
};

const sellers_view = {
    path: '/sellers',
    component: () => import('~/pages/sellers/index.vue'),
    name: 'Seller',
};

export default <RouterConfig>{
    routes: (_routes) => [home_links, search_links, account_links, sellers_view],
};
