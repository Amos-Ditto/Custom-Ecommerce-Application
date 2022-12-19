import { defineStore } from 'pinia';

export const useLayoutStore = defineStore('layout', () => {
    const account_side_toggle = ref<boolean>(false);

    const toggleAccountSideBar = (): void => {
        account_side_toggle.value = !account_side_toggle.value;
    };

    // Authentications
    const showauth = ref<boolean>(false);
    const toggleAuth = (): void => {
        showauth.value = !showauth.value;
    };
    return {
        account_side_toggle,
        toggleAccountSideBar,
        showauth,
        toggleAuth,
    };
});
