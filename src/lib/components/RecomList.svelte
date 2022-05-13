<script lang='ts'>
    export let recom
import { bookDetail } from '$lib/api'
    import BookSmall from '$lib/components/BookSmall.svelte'
    import Color from '../../routes/Color.svelte'
    import Flicking, { FlickingPanel } from "@egjs/svelte-flicking";
    import "@egjs/svelte-flicking/dist/flicking.css";

    let flicking= Flicking;
    
</script>

<div class="content">
    <!-- {#if recom.recommand.length > 0 }
        <div class='reason'>{recom.recommand}</div>
    {:else if recom.keywords.length>0 }
        <div class='row'>
            {#each recom.keywords as keyword}
                <div class='reason'>#{keyword} </div>
            {/each}
        </div>
    {/if} -->
    <div class='reason'>{recom.title}</div>
    <div class='row'>
        <!-- <Flicking options={{ align: "center", circular: true }}> -->
            {#each recom.books as book}
            <!-- <FlickingPanel></FlickingPanel>     -->
            <a class='book' href={`/book/${book.id}`}>
                    <BookSmall image={book.image} title={book.title} author={book.author}/></a>
            <!-- </FlickingPanel> -->
            {/each}
        <!-- </Flicking> -->
        <!-- <button on:click={() => { flicking.next(); }} /> -->
    </div>
</div>

<style>
    .content {
        display: flex;
        flex-direction: column;
        margin-top: 1rem;
        margin-bottom: 1rem;
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
        overflow: scroll;
        display: flex;
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
</style>