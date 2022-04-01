<div class="content">

    {#if recom.recommand.length >0 }
        <p>{recom.recommand}</p>
    {:else if recom.keywords.length>0 }
        <div class='row'>
            {#each recom.keywords as keyword}
                <p>#{keyword} </p>
            {/each}
        </div>
    {/if}

    <div class='row'>
        {#each recom.books as book}
            <a href={`./book/${book.id}`}><BookSmall image={book.image} title={book.title} /></a>
        {/each}
    </div>
</div>

<script>
    export let recom

    import BookSmall from '$lib/components/BookSmall.svelte'
    import Color from '../../routes/Color.svelte'
</script>

<style>
    .content {
        margin: 1rem;
        display: flex;
        flex-direction: column;
    }

    :global(.row) {
        display: flex;
        flex-wrap: nowrap;
        flex-direction: row;
    }
    div{
        font-size: 1.5rem;
        font-weight: 500;
        color:var(--main-flybook)
    }
    a{
        text-decoration: none !important;
    }
</style>