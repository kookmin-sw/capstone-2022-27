<script>
import BookSmall from '$lib/components/BookSmall.svelte'
import Card from '$lib/components/Card.svelte'
import { booksMockup } from '../lib/api'

const init = booksMockup()
</script>

<div class="content">
<h1>Booka Gazua~</h1>
<Card className="row">
    {#await init}
        <p>waiting..</p>
    {:then books}
        {#each books as book}
            <BookSmall image={book.image} title={book.title} />
        {/each}
    {:catch error}
        <p>error: {error.message}</p>
    {/await}
</Card>
</div>

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