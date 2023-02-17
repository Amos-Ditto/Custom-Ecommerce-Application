import type { RouterConfig } from "@nuxt/schema";

// https://router.vuejs.org/api/interfaces/routeroptions.html
export default <RouterConfig>{
	routes: (_routes) => [
		{
			name: "Home",
			path: "/",
			component: () => import("~/pages/index.vue"),
		},
		{
			name: "Authentication",
			path: "/auth",
			component: () => import("~/pages/auth.vue"),
			children: [
				{
					name: "Login",
					path: "",
					component: () => import("~/pages/auth/login.vue"),
				},
				{
					name: "Register",
					path: "register",
					component: () => import("~/pages/auth/register.vue"),
				},
			],
		},
		{
			name: "All-Products",
			path: "/products",
			component: () => import("~/pages/products.vue"),
			children: [
				{
					name: "Products",
					path: "",
					component: () => import("~/pages/products/index.vue"),
				},
				{
					name: "Categories",
					path: "category",
					component: () => import("~/pages/products/category.vue"),
					children: [
						{
							name: "Category",
							path: ":category",
							component: () => import("~/pages/products/category/[category].vue"),
						},
					],
				},
			],
		},
	],
};
