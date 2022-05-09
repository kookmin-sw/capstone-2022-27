import { browser } from '$app/env';
import { writable } from 'svelte/store'
// import { browser } from "$app/env";

export const TOKEN = writable(browser && localStorage.getItem("token"))

if(browser){
    TOKEN.subscribe(value => {
        localStorage.setItem("token", value);
    });
}
