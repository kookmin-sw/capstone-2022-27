<script>
    import { bookSearch, bookSearchKeywords} from '$lib/api'
    import { page } from '$app/stores';
    let keyword = $page.params.keyword
    let pageNum = 0 

    const bookSearchP = bookSearch(keyword,pageNum)
    
</script>

<div class='center'>
<div class="container">
    <div class='result'>'{keyword}' 검색 결과</div>
    <hr style="border: 1px solid #26282B;"/>

    <div class='container'>
        {#await bookSearchP}
            loading...
        {:then books} 
            {#each books as book}
                <div class="image" style="background-image: url('{book['image']}');"/>
                <div>
                    <div class='title'>{book.title}</div>
                    <div class='author'>{book.author} 지음 {book.publisher} 펴냄</div>
                    <div class="keywords">
                        {#each book['keywords'] as keyword}
                            <a href='keyword/{keyword}' class='keyword'>#{keyword} </a>
                        {/each}
                    </div>
                </div>
            {/each}
        {/await}
    </div>
</div>

</div>


<style>
    .center{
        justify-content: center;
        display: flex;
    }
    .container{
        width: 39.375rem;
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
    .image{
        width: 8.25rem;
        height: 11.875rem;
    }
    .title{
        font-family: 'Pretendard';
        font-style: normal;
        font-weight: 700;
        font-size: 1.063rem;
        line-height: 1.25rem;
        color: #1B1D1F;
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
        margin-right: 0.7rem;
    }
</style>
