import { IPayload, IRefreshToken } from "~~/types";
import { useAuthStore } from "~~/stores/authStore";

export default defineNuxtPlugin((nuxtApp) => {
	const user_payload = useCookie("user_payload");
	const refresh_token = useCookie("user_refresh_token");
	const authStore = useAuthStore()
	const { onLogout } = useApollo();
	const today = new Date();

	// Check refresh token if it's expired
	if (typeof refresh_token.value === "object") {
		let obj_refresh_token = refresh_token.value as unknown as IRefreshToken;
		if (today > new Date(obj_refresh_token.refreshExpiresIn * 1000)) {
			refresh_token.value = null;
			return;
		}
	}

	// Check Bearer token if it's expired
	if (typeof user_payload.value === "object") {
		let obj_user_payload = user_payload.value as unknown as IPayload;
		if (today > new Date(obj_user_payload.exp * 1000)) {
			onLogout();
			user_payload.value = null;
			return;
		}
		authStore.updateIsLoggedIn();
	}
});
