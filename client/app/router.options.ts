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
					component: () => import("~~/pages/products/all-products.vue"),
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
				{
					name: "Product",
					path: "product-:productId",
					component: () => import("~~/pages/products/product-[productId].vue"),
				},
			],
		},
		{
			name: "Shops",
			path: "/shops",
			component: () => import("~/pages/shops.vue"),
			children: [
				{
					name: "All-shops",
					path: "",
					component: () => import("~/pages/shops/all-shops.vue"),
				},
				{
					name: "Shop-ID",
					path: "shop-:shopId",
					component: () => import("~/pages/shops/shop-[shopId].vue"),
					children: [
						{
							name: "Shop-Name",
							path: "",
							component: () => import("~/pages/shops/shop-[shopId]/shop.vue"),
						},
						{
							name: "Shop-offers",
							path: "offers",
							component: () => import("~/pages/shops/shop-[shopId]/offers.vue"),
						},
						{
							name: "Shop-products",
							path: "products",
							component: () => import("~/pages/shops/shop-[shopId]/products.vue"),
							children: [
								{
									name: "Shop-All-Products",
									path: "",
									component: () => import("~/pages/shops/shop-[shopId]/products/all-products.vue"),
								},
								{
									name: "Shop-Products-Category",
									path: ":categoryName",
									component: () => import("~~/pages/shops/shop-[shopId]/products/[categoryName].vue"),
								},
							],
						},
					],
				},
			],
		},
		{
			name: "User",
			path: "/user",
			component: () => import("~/pages/user.vue"),
			children: [
				{
					name: "User-Dashboard",
					path: "",
					component: () => import("~/pages/user/dashboard.vue"),
				},
			],
		},
	],
};
