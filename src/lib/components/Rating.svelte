<script>
import { createEventDispatcher } from 'svelte';
const dispatch = createEventDispatcher()
export let enabled = false
export let rating = 7
let randkey = Math.random()

let ratings = [10 , 9 , 8 , 7 , 6 , 5 , 4 , 3 , 2 , 1]

const onchange = () => {
    console.log('123')
    dispatch('message', {
        text: 'Hello!'
    })
}
</script>

<fieldset class="rate">
    {#each ratings as r}
        <input on:click={onchange} type="radio" id="rand{randkey}{r}" disabled={!enabled} bind:group={rating} name="rand{randkey}" value="{r}" />
        <label on:click={onchange} for="rand{randkey}{r}" class="{r%2==1?'half':''} {enabled?'enabled':'disabled'}"></label>
    {/each}
</fieldset>

<style>
/* Base setup */
@import url(//netdna.bootstrapcdn.com/font-awesome/3.2.1/css/font-awesome.css);

/* Ratings widget */
.rate {
    display: inline-block;
    border: 0;
}
/* Hide radio */
.rate > input {
    display: none;
}
/* Order correctly by floating highest to the right */
.rate > label {
    float: right;
}
/* The star of the show */
.rate > label:before {
    display: inline-block;
    /* padding: .3rem .1rem; */
    padding-right:0.1rem ;
    margin: 0;
    cursor: pointer;
    font-family: FontAwesome;
    content: "\f005 "; /* full star */
    
    font-size: 16px;
}

/* Half star trick */
.rate .half:before {
    content: "\f089 "; /* half star no outline */
    position: absolute;
    /* padding-right: 0; */

    font-size: 16px;
}

label {
    color: #E9EBED;
}
/* Click + hover color */
input:checked ~ label, /* color current and previous stars on checked */
label.enabled:hover, label.enabled:hover ~ label { color: #07ABCF;  } /* color previous stars on hover */

/* Hover highlights */
input:checked + label.enabled:hover, input:checked ~ label:hover, /* highlight current and previous stars */
input:checked ~ label.enabled:hover ~ label, /* highlight previous selected stars for new rating */
label.enabled:hover ~ input:checked ~ label /* highlight previous selected stars */ { color: #37DBFF;  } 

fieldset {
    padding: 0;
}
</style>
