<script lang='ts'>
    // export let recom
    export let recom_type
    import { mainpage } from '$lib/api'
    import BookSmall from '$lib/components/BookSmall.svelte'
    import Flicking, { FlickingPanel } from "@egjs/svelte-flicking";
    import "@egjs/svelte-flicking/dist/flicking.css";

    let flicking = Flicking;
    const init = mainpage(recom_type)
    
</script>

<div class="content">
    {#await init}
        
    {:then recom} 
        <div class='reason'>{recom.title}</div>
        <div class='btn prev' on:click={() => { flicking.moveTo(flicking.index-6); }} >
            <img class='btn-img' src="/static/prev.svg"/>
        </div>
        <div class='row'>
            <Flicking bind:this={flicking} options={{ align: "prev", circular: false, defaultIndex:2 }}>
                {#each recom.books as book}
                <FlickingPanel style="margin: 0 .5rem; display:flex; align-items:center;">
                    <a class='book' href={`/book/${book.id}`}>
                        <BookSmall image={book.image} title={book.title} author={book.author}/>
                    </a>
                </FlickingPanel>
                {/each}
            </Flicking>
        </div>
        <div class='btn next'  on:click={() => { flicking.moveTo(flicking.index+6); }} >
            <img class='btn-img' src="/static/next.svg"/>
        </div>
    {/await}
    
</div>

<style>
    .content {
        display: flex;
        flex-direction: column;
        margin-top: 1rem;
        margin-bottom: 1rem;
        position: relative;
    }
    
    .reason{
        color: #1B1D1F;
        font-family: 'Pretendard';
        font-style: normal;
        font-weight: 700;
        font-size: 1rem;
        margin-bottom: 1.25rem;
    }

    .row { 
        position: relative;
        display: flex;
        align-items: center;
        flex-wrap: nowrap;
        flex-direction: row;
    }
    div{
        font-size: 0.8rem;
        font-weight: 500;
        color:var(--main-flybook)
    }
    a{
        text-decoration: none !important;
    }
    .book{
        margin-right: 1.125rem;
    }
    .btn-img{
        width: 1rem;
        padding: 0.5rem;
    }
    .btn{
        display: none;
        position: absolute;
        background-color: #00000052;
        height: 4rem;
        margin: 0 0 3rem;
        border-radius: 5px;
        justify-content: center;
        z-index: 100000000000000;
    }
    .content:hover .btn {
        display: flex;
    }
    .btn.prev{
        top: 5rem;
        left: -1.5rem;
    }
    .btn.next{
        top: 5rem;
        right: -1.5rem;
    }
    .next{

    }
</style>