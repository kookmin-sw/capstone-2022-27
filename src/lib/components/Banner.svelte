<script>
import BookaPickBox from "./BookaPickBox.svelte"
import Flicking, { FlickingPanel } from "@egjs/svelte-flicking";
import "@egjs/svelte-flicking/dist/flicking.css";

import { goto } from '$app/navigation';

import PickBook from "./PickBook.svelte"
export let banners
let flicking= Flicking;

setInterval(() => {
    flicking.next();
}, 3000);

</script>

<div class="container">
    {#if banners.length > 0}
    <Flicking bind:this={flicking} options={{ align: "center", circular: true, defaultIndex:1 }}>
        {#each banners as banner}
        <FlickingPanel>
            <div class='col' style="background-color:{banner.bgColor}" on:click="{() => {goto(`./book/${banner.id}`)}}">
                <BookaPickBox backgroundColor={banner.pointColor} textColor={banner.textColor}/>
                <div class="descdiv">
                    <div class='desc'>
                        <div class="desctext" style="color:{banner.textColor}">{@html banner.desc}</div>
                        <div class="keywords">
                            {#each banner.keywords as keyword}
                                <a class='keyword' style='color:{banner.pointColor}'href={`./search/keyword/${keyword}/0`}>#{keyword} </a>
                            {/each}
                        </div>
                    </div>
                </div>
                <div style="imgdiv">
                    <div class='centered'>
                        <PickBook img={banner.image} starColor={banner.pointColor} textColor={banner.textColor}></PickBook>
                    </div>
                </div>
            </div>
        </FlickingPanel>
        {/each}
    </Flicking>
    {/if}
</div>
    
<style>
    .container {
        /* display: flex; */
        display: inline-flex;
        align-items: left;
        height: 22.5rem;
    }

    .col{
        width: calc(18rem + 33vw);
        height: 22.5rem;
        position: relative;
        cursor: pointer;
    }

    .keyword{
        text-decoration: none !important;
        font-style: normal;
        font-weight: 400;
        font-size: 0.9rem;
        color: #23E771;
        margin-top: 3vw;
    }

    .descdiv{
        display: flex;
        flex-direction: column;
        justify-content: center;
        padding: 0 0 0 3vw;
        width: 50%;
        height: 100%;
    }
    .desc {
        padding: 0 0 2rem 0;
    }
    .center{
        flex: auto;
        display: flex;
        justify-content: center;
    }
    .centered {
        position: absolute;
        top: 50%;
        right: calc(3vw + .5rem);
        transform: translate(0%, -50%);
    }

    .keywords {
        margin-top: .5rem;
    }

    .desctext{
        font-size: 1.5rem;
        font-weight: 700;
        color:#FFFFFF;
    }

    .vertical-center {
        margin: 0;
        position: absolute;
        top: 50%;
        -ms-transform: translateY(-50%);
        transform: translateY(-50%);
    }
    
</style>