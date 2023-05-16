import { defineStore } from "pinia";
import { IPayload, IUserAuth } from "../types";

export const useAuthStore = defineStore("user", () => {
	const appUser = ref<IUserAuth>();
	const userPayload = ref<IPayload>();
	const from_registration = ref<boolean>(false);
	const updateAppUser = (payload: IUserAuth) => {
		appUser.value = payload;
	};
	const updateUserPayload = (payload: IPayload) => {
		userPayload.value = payload;
	};
	const updateFromRegistration = (): void => {
		from_registration.value = !from_registration.value;
	};
	return { appUser, userPayload, from_registration, updateAppUser, updateUserPayload, updateFromRegistration };
});
