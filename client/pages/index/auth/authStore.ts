import { defineStore } from "pinia";
import { IPayload, IUserAuth } from "~~/types";

export const useAuthStore = defineStore("user", () => {
	const appUser = ref<IUserAuth>();
	const userPayload = ref<IPayload>();
	const updateAppUser = (payload: IUserAuth) => {
		appUser.value = payload;
	};
	const updateUserPayload = (payload: IPayload) => {
		userPayload.value = payload;
	};
	return { appUser, userPayload, updateAppUser, updateUserPayload };
});
