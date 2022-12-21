import { defineStore } from 'pinia';

export const useLayoutStore = defineStore('layout', () => {
    const account_side_toggle = ref<boolean>(false);

    const toggleAccountSideBar = (): void => {
        account_side_toggle.value = !account_side_toggle.value;
    };

    // Authentications
    const showauth = ref<boolean>(false);
    const toggleauths = ref<boolean>(false);

    // Methods
    const toggleAuth = (): void => {
        showauth.value = !showauth.value;
    };
    const closeAuth = (payload: boolean): void => {
        showauth.value = payload;
    };

    const toggleAuthType = (payload: boolean): void => {
        toggleauths.value = payload;
    };

    return {
        account_side_toggle,
        toggleAccountSideBar,
        showauth,
        toggleAuth,
        closeAuth,
        toggleauths,
        toggleAuthType,
    };
});
