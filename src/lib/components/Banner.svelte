<script>
import BookaPickBox from "./BookaPickBox.svelte"
import Flicking, { FlickingPanel } from "@egjs/svelte-flicking";
import "@egjs/svelte-flicking/dist/flicking.css";

import PickBook from "./PickBook.svelte"
export let banners
let flicking= Flicking;

</script>

<div class="container">
    <Flicking bind:this={flicking} options={{ align: "center", circular: true, defaultIndex:0 }}>
        {#each banners as banner}
        <FlickingPanel>
            <div class='col' style="background-color:{banner.bgColor}">
                <div style="width:50%;" >
                    <BookaPickBox/>
                    <div class='desc'>
                        <div class="desctext">{@html banner.desc}</div>
                        <!-- {#each banners.keywords as keyword}
                            <a clㄴass='keyword' href={`./book/${keyword}`}>#{keyword} </a>
                        {/each} -->
                    </div>
                </div>
                <div style="width:50%; position:relative">
                    <div class='centered'>
                        <PickBook img={banner.image} starColor='#23E771'></PickBook>
                    </div>
                </div>
            </div>
            <svelte:fragment slot="viewport">
                <span class="item-inside-viewport">sdfsdf</span>
                <span class="item-inside-viewport">fdsf</span>
            </svelte:fragment>
        </FlickingPanel>
        {/each}
    </Flicking>
    <div>
        <img class='btn-img' src="/static/prev-black.svg"/>
        <img class='btn-img' src="/static/next-black.svg"/>
    </div>
</div>
    
<style>
    /* .container .col:nth-child(1) { flex-grow: 1; background-color: #9EA4AA; width: 15rem;}
    .container .col:nth-child(2) { flex-grow: 1; background-color: #26282B; width: 42rem;}
    .container .col:nth-child(3) { flex-grow: 1; background-color: #E9EBED; width: 15rem;} */

    .container {
        /* display: flex; */
        display: inline-flex;
        align-items: left;
        height: 22.5rem;
    }

    .col{
        display: flex;
        width:60rem;
        /* width: calc(18rem + 33%); */
        height: 22.5rem;
        /* justify-content: center; */
        /* align-items: center; */
    }

    .keyword{
        text-decoration: none !important;
        font-style: normal;
        font-weight: 400;
        font-size: 0.75rem;
        color: #23E771;
    }

    .desc{
        margin-left: 1.5rem;
        margin-top: 3.3rem;
    }
    .center{
        flex: auto;
        display: flex;
        justify-content: center;
    }
    .centered {
        position: absolute;
        top: 50%;
        left: 50%;
        transform: translate(-50%, -50%);
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