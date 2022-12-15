import { defineStore } from 'pinia';

export const useLayoutStore = defineStore('layout', () => {
    const account_side_toggle = ref<boolean>(false);

    const toggleAccountSideBar = (): void => {
        account_side_toggle.value = !account_side_toggle.value;
    };

    return {
        account_side_toggle,
        toggleAccountSideBar,
    };
});
