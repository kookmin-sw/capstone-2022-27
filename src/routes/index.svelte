<div class="content">
    <h1>Booka Gazua~</h1>
    <Card className="row">
        {#await init}
            <p>waiting..</p>
        {:then books}
            {#each books as book}
                <a href={`./book/${book.id}`}><BookSmall image={book.image} title={book.title} /></a>
            {/each}
        {:catch error}
            <p>error: {error.message}</p>
        {/await}
    </Card>
</div>

<script>
    import BookSmall from '$lib/components/BookSmall.svelte'
    import Card from '$lib/components/Card.svelte'
    import { booksMockup } from '../lib/api'
    
    const init = booksMockup()
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
</style>