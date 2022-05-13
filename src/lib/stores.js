import { browser } from '$app/env';
import { writable } from 'svelte/store'
// import { browser } from "$app/env";

export const stores_TOKEN = writable(browser && localStorage.getItem("token"))
export const stores_nickname = writable(browser && localStorage.getItem("nickname"))

if(browser){
    stores_TOKEN.subscribe(value => {
        localStorage.setItem("token", value);
    });

    stores_nickname.subscribe(value => {
        localStorage.setItem("nickname", value);
    });
}
