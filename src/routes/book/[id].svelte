<script>
    import Card from '$lib/components/Card.svelte'
    import { bookDetailMockup } from '$lib/api'

    const bookP = bookDetailMockup()
</script>

<div class="book-detail">
    {#await bookP}
        <p>loading...</p>
    {:then book} 
        <div class="book col">
            <div class="image" style="background-image: url('{book.image}');"></div>
            <div class='bookinfo'>
                <div class='col'>
                    <div class="title">{book.title}</div>
                    <div class="bookstate">읽었어요</div>
                </div>
                
                <div class="author"><b>{book.author}</b> 지음 | <b>{book.publisher}</b> 펴냄 </div>
                <div class="keyword">
                    {#each book.keywords as keyword}
                        <a>#{keyword} </a>
                    {/each}
                </div>
            </div>
        </div>
        <hr width='100%'/>
        <div class="desc">{@html book.desc}</div>
    {:catch error}
        <p>error: {error.message}</p>
    {/await}
</div>

<style>
    .book {
        display: flex;
        flex-direction: column;
        align-items:flex-start;
        margin: .8rem 1rem;
        background-color: #F7F8F9;
    }

    .image {
        display: inline-block;
        background-size: cover;
        width: 16rem;
        height: 23rem;
        margin-bottom: 1rem;
        box-shadow: 0px 5px 12px 0px rgba(0, 0, 0, 0.14);
    }

    .title {
        font-size: 2rem;
        color: #444;
        font-weight: bold;
    }

    .author {
        font-size: 0.8rem;
        color: #444;
        font-weight: 400;
    }

    .desc {
        font-size: 0.8rem;
        color: #444;
        font-weight: bold;
        margin: 2rem;
    }

    .book-detail {
        margin: 0rem;
        display: flex;
        flex-direction: column;
    }

    .bookinfo{
        margin-left: 2rem;
        margin-top: 2rem;
    }

    .row {
        display: flex;
        flex-wrap: nowrap;
        flex-direction: row;
    }

    .col{
        display: flex;
        flex-wrap: nowrap;
        flex-direction: row;
        vertical-align:middle;
        line-height: normal;
    }
    
    .keyword{
        font-size: 2rem;
        font-weight: 500;
    }
</style>