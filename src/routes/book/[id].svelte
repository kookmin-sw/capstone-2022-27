<div class="book-detail">
    <h1>Booka Gazua~</h1>
    <Card>
        {#await bookP}
            <p>loading...</p>
        {:then book} 
            <div class="book">
                <div class="image" style="background-image: url('{book.image}');"></div>
                <div class="title">{book.title}</div>
                <div class="author">{book.author}</div>
                <div class="desc">{book.desc}</div>
            </div>
        {:catch error}
            <p>error: {error.message}</p>
        {/await}
    </Card>
</div>

<script>
    import Card from '$lib/components/Card.svelte'
    import { bookDetailMockup } from '$lib/api'

    const bookP = bookDetailMockup()
</script>

<style>
    .book {
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        margin: .5rem 1rem;
    }

    .image {
        display: inline-block;
        background-size: cover;
        width: 6rem;
        height: 9rem;
        margin-bottom: 1rem;
        box-shadow: 0px 5px 12px 0px rgba(0, 0, 0, 0.14);
    }

    .title {
        font-size: 0.9rem;
        text-align: center;
        color: #444;
        font-weight: bold;
    }

    .author {
        font-size: 0.8rem;
        text-align: center;
        color: #444;
        font-weight: bold;
    }

    .desc {
        font-size: 0.8rem;
        text-align: center;
        color: #444;
        font-weight: bold;
    }

    .book-detail {
        margin: 1rem;
        display: flex;
        flex-direction: column;
    }
</style>