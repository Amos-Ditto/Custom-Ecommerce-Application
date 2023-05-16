export default defineNuxtPlugin(() => {
    return {
        provide: {
            validEmail(email: string) {
                const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
                return emailRegex.test(email);
            }
        }
    }
})
