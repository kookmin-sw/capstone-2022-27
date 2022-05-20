<script>
    import { bookSearch, bookSearchKeywords} from '$lib/api'
    import { page } from '$app/stores';

    export let books
    export let nowKeyword = ''
</script>

<div class='container'>
    {#each books as book}
    <div class="row">
        
        <a href="/book/{book.id}"><div class="image-wrap"><div class="image" style="background-image: url('{book.image}');"></div></div></a>
        <a href="/book/{book.id}"> 
            <div class="right">
                <div class='title'>{book.title}</div>
                <div class='author'>{book.author} 지음 {book.publisher} 펴냄</div>
                <div class="keywords">
                    {#each book['keywords'] as keyword}
                        <a href='/search/keyword/{keyword}/0' class={'keyword' + (nowKeyword == keyword ? ' selected' : '')}>#{keyword} </a>
                    {/each}
                </div>
            </div>
        </a>
    </div>
    {/each}
</div>


<style>
    .center{
        justify-content: center;
        display: flex;
    }
    .container{
        width: 100%;
    }
    .result{
        margin: 2.563rem 0 1.5rem 0;
        font-family: 'Pretendard';
        font-style: normal;
        font-weight: 700;
        font-size: 1.313rem;
        line-height: 1.563rem;
        color: #1B1D1F;
    }
    hr{
        margin-bottom: 1.5rem;
    }
    .right {
        display: flex;
        flex-direction: column;
        justify-content: space-between;
    }
    .image-wrap {
        width: 6rem;
        height: 9rem;
        margin-right: 1.5rem;
        position: relative;
        display: inline-block;
    }
    .image{
        position: absolute;
        display: inline-block;
        width: 6rem;
        height: 9rem;
        background-size: contain;
        background-position: center;
        background-repeat: no-repeat;
        transition: .25s ease-in-out;
        filter: drop-shadow(0px 3px 4px rgba(27, 29, 31, 0.3));
    }
    .image:hover{
        transform: scale(1.15);
    }
    .title{
        font-family: 'Pretendard';
        font-style: normal;
        font-weight: 700;
        font-size: 1.063rem;
        line-height: 1.25rem;
        color: #1B1D1F;
        margin-top: 1.5rem;
    }

    .author{
        font-family: 'Pretendard';
        font-style: normal;
        font-weight: 400;
        font-size: 0.9rem;
        line-height: 1.125rem;
        color: #72787F;
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
        margin: 0 0.7rem .7rem 0;
        transition: .3s ease-in-out;
    }
    .keyword:hover, .keyword.selected{
        color: rgb(45, 189, 205);
        border-color: rgb(45, 189, 205);
    }
    .row{
        display: flex;
        flex-direction: row;
        margin-bottom: 2.25rem;
        /* justify-content: space-between; */
    }
</style>
