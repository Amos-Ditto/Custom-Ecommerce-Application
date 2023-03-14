import { defineStore } from "pinia";

export const useAppStore = defineStore("app", () => {
	const heightPos = ref<number>(0);

	const changeHeight = (payload: number) => {
		heightPos.value = payload;
	};

	return { heightPos, changeHeight };
});
