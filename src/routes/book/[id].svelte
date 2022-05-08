<script>
    import { bookDetail ,profileMockup} from '$lib/api'
    import { page } from '$app/stores';
    import BookIntro from '$lib/components/BookIntro.svelte';
    import RecomList from '$lib/components/RecomList.svelte';
    import BookSmall from '$lib/components/BookSmall.svelte';

    let id = $page.params.id
    const bookP = bookDetail(id)
    let btnColors = ['#FF68CC', '#37DBFF', '#23E771']
</script>

<div class="book-detail">
    {#await bookP}
        <p>loading...</p>
    {:then book}
        <div class="book col">
            <div class="image" style="background-image: url('{book['book']['image']}');"></div>
            <div class='bookinfo'>
                <div class="title">{book['book']['title']}</div>
                <div class="summary">{book['book']['intro']}</div>
                <div class="author"><b>{book['book']['author']}</b> 지음 | <b>{book['book']['publisher']}</b> 펴냄 </div>
                <div class="keywords">
                    {#each book['book']['keywords'] as keyword}
                        <a href=' ' class='keyword'>#{keyword} </a>
                    {/each}
                </div>
                <div class='col button_container'>
                    {#if !true}
                        <div class='btn btn-selected'>
                            <img alt='' src='/static/hope_selected.svg' >
                            <div style='color:{btnColors[0]}'>읽고싶어요</div>
                        </div>
                    {/if}

                    {#if true}
                    <div class='btn'>
                        <img alt='' src='../static/hope.svg' >
                        <div>읽고싶어요</div>
                    </div>
                    {/if}

                </div>
            </div>
        </div>
        <BookIntro title="책 소개" content="{book['book']['desc']}"/>
        <BookIntro title="목차" content="{book['book']['desc_index']}"/>
        <div class='row'>
        {#each book['similar'] as book}
            <a class='book' href={`./book/${book.id}`}><BookSmall image={book.image} title={book.title} /></a>
        {/each}
        </div>
        
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
        width: 10.5rem;
        height: 15.18rem;
        margin-bottom: 1rem;
        box-shadow: 0px 5px 12px 0px rgba(0, 0, 0, 0.14);
    }

    .title {
        font-family: 'Pretendard';
        font-style: normal;
        font-weight: 700;
        font-size: 1.5rem;
        color: #1B1D1F;
    }

    .author {
        font-size: 0.8rem;
        color: #444;
        font-weight: 400;
        margin-top: 1rem;
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
    
    .keywords{
        /* font-size: 2rem;
        font-weight: 500; */
        margin-top: 1.2rem;
    }
    .keyword{
        display: inline-flex;
        flex-direction: row;
        align-items: flex-start;
        padding: 7px 12px;

        border: 0.5px solid #454C53;
        box-sizing: border-box;
        border-radius: 100px;

        font-family: 'Pretendard';
        font-style: normal;
        font-weight: 400;
        font-size: 12px;
        line-height: 14px;
        text-align: center;
        margin-right: 0.7rem;
    }
    .summary{
        font-family: 'Pretendard';
        font-style: normal;
        font-weight: 400;
        font-size: 1rem;
        line-height: 1rem;
        margin-top: 0.25rem;
        color: #1B1D1F;
    }

    .btn{
        display: flex;
        align-items: center; 
        justify-content: center;
        border: 0.5px solid #1B1D1F;
        box-sizing: border-box;
        border-radius: 2px;
        width: 5.813rem;
        height: 2.25rem;
    }
    .btn div{
        font-family: 'Pretendard';
        font-style: normal;
        font-weight: 400;
        font-size: 0.813rem;
        line-height: 1.063rem;
    }
    .btn img{
        margin-right: 0.25rem;
    }
    .btn-selected{
        background-color: #26282B;
    }

    .btn-selected div{
        font-family: 'Pretendard';
        font-style: normal;
        font-weight: 700;
        font-size: 0.813rem;
        line-height: 1.063rem;
        text-align: center;
    }

    .button_container{
        margin-top: 2rem;
    }

    
    
</style>