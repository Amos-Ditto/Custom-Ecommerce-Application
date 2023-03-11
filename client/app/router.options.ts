import type { RouterConfig } from "@nuxt/schema";

// https://router.vuejs.org/api/interfaces/routeroptions.html
export default <RouterConfig>{
	routes: (_routes) => [
		{
			name: "Users",
			path: "/",
			component: () => import("~/pages/index.vue"),
			children: [
				{
					name: "Home",
					path: "",
					component: () => import("~/pages/index/home.vue"),
				},
				{
					name: "Authentication",
					path: "auth",
					component: () => import("~/pages/index/auth.vue"),
					children: [
						{
							name: "Login",
							path: "",
							component: () => import("~/pages/index/auth/login.vue"),
						},
						{
							name: "Register",
							path: "register",
							component: () => import("~/pages/index/auth/register.vue"),
						},
					],
				},
				{
					name: "All-Products",
					path: "products",
					component: () => import("~/pages/index/products.vue"),
					children: [
						{
							name: "Products",
							path: "",
							component: () => import("~/pages/index/products/all-products.vue"),
						},
						{
							name: "Categories",
							path: "category",
							component: () => import("~/pages/index/products/category.vue"),
							children: [
								{
									name: "Category",
									path: ":category",
									component: () => import("~/pages/index/products/category/[category].vue"),
								},
							],
						},
						{
							name: "Product",
							path: "product-:productId",
							component: () => import("~/pages/index/products/product-[productId].vue"),
						},
					],
				},
				{
					name: "Shops",
					path: "shops",
					component: () => import("~/pages/index/shops.vue"),
					children: [
						{
							name: "All-shops",
							path: "",
							component: () => import("~/pages/index/shops/all-shops.vue"),
						},
						{
							name: "Shop-ID",
							path: "shop-:shopId",
							component: () => import("~/pages/index/shops/shop-[shopId].vue"),
							children: [
								{
									name: "Shop-Name",
									path: "",
									component: () => import("~/pages/index/shops/shop-[shopId]/shop.vue"),
								},
								{
									name: "Shop-offers",
									path: "offers",
									component: () => import("~/pages/index/shops/shop-[shopId]/offers.vue"),
								},
								{
									name: "Shop-products",
									path: "products",
									component: () => import("~/pages/index/shops/shop-[shopId]/products.vue"),
									children: [
										{
											name: "Shop-All-Products",
											path: "",
											component: () => import("~/pages/index/shops/shop-[shopId]/products/all-products.vue"),
										},
										{
											name: "Shop-Products-Category",
											path: ":categoryName",
											component: () => import("~/pages/index/shops/shop-[shopId]/products/[categoryName].vue"),
										},
									],
								},
							],
						},
					],
				},
				{
					name: "User",
					path: "user",
					component: () => import("~/pages/index/user.vue"),
					children: [
						{
							name: "User-Dashboard",
							path: "dashboard",
							component: () => import("~/pages/index/user/dashboard.vue"),
						},
						{
							name: "Purchases",
							path: "purchase",
							component: () => import("~/pages/index/user/purchases.vue"),
							children: [
								{
									name: "Purchase-Home",
									path: "",
									component: () => import("~/pages/index/user/purchases/home.vue"),
								},
								{
									name: "Purchase-Order",
									path: ":orderID",
									component: () => import("~/pages/index/user/purchases/[orderID].vue"),
								},
							],
						},
						{
							name: "User-Wishlist",
							path: "wishlist",
							component: () => import("~/pages/index/user/wishlist.vue"),
						},
						{
							name: "User-Profile",
							path: "profile",
							component: () => import("~/pages/index/user/profile.vue"),
						},
					],
				},
				{
					name: "Register-Shop",
					path: "register-shop",
					component: () => import("~/pages/index/register-shop.vue"),
				},
			],
		},
		{
			name: "Sellers",
			path: "/seller",
			component: () => import("~/pages/seller.vue"),
			children: [
				{
					name: "Seller-Account",
					path: "",
					component: () => import("~/pages/seller/main.vue"),
					children: [
						{
							name: "Seller-Home",
							path: "",
							component: () => import("~/pages/seller/main/home.vue"),
						},
						{
							name: "Seller-Products",
							path: "products",
							component: () => import("~/pages/seller/main/products.vue"),
							children: [
								{
									name: "Seller-Product-List",
									path: "",
									component: () => import("~/pages/seller/main/products/products.vue"),
								},
								{
									name: "Seller-Add-Product",
									path: "add",
									component: () => import("~/pages/seller/main/products/add-product.vue"),
								},
								{
									name: "Seller-View-Product",
									path: "view-:productID",
									component: () => import("~/pages/seller/main/products/view-[productID].vue"),
								},
							],
						},
						{
							name: "Seller-Orders",
							path: "orders",
							component: () => import("~/pages/seller/main/orders.vue"),
						},
						{
							name: "Seller-Reviews",
							path: "reviews",
							component: () => import("~/pages/seller/main/reviews.vue"),
						},
						{
							name: "Seller-Settings",
							path: "settings",
							component: () => import("~/pages/seller/main/settings.vue"),
						},
						{
							name: "Seller-Queries",
							path: "queries",
							component: () => import("~/pages/seller/main/product-queries.vue"),
						},
					],
				},
				{
					name: "Login-Seller",
					path: "login",
					component: () => import("~/pages/seller/login.vue"),
				},
			],
		},
	],
};
