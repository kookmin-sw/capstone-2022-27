<script>
    import { bookSearch, bookSearchKeywords, booksMockup} from '$lib/api'
    import { page } from '$app/stores';
    import SearchBookList from '$lib/components/SearchBookList.svelte';
    import { goto } from '$app/navigation';

    export let buttons = [-2, -1, 0, 1, 2];
    let keyword = $page.params.keyword
    const pageNum = 10
    
    let currentPage = Number($page.params.page)
    let isloaded=false
    let books
    let pageCount;
    
    async function getBookSearch(){
        isloaded=false
        try {
            console.log('page'+$page.params.page+' '+currentPage)
            books = await bookSearch(keyword, currentPage)
            console.log(books)
            isloaded=true
            pageCount = Math.floor( pageNum / books.count);
        } catch (e) {console.error(e)}
        
    }
    
    getBookSearch()

    $: {
        if (keyword != $page.params.keyword) {
            keyword = $page.params.keyword
            currentPage = Number($page.params.page)
            isloaded = false
            bookSearch(keyword, currentPage).then((data) => {
                books = data
                isloaded = true
                pageCount = Math.floor( pageNum / books.count);
            })
        }
    }
</script>

<div class='center'>
<div class="container">
    <div class='result'>'{keyword}' 검색 결과</div>
    <hr style="border: 1px solid #26282B;"/>

    <div class='container'>
        {#if isloaded}
           <SearchBookList books = {books.books}/>
           <div style='col'>
                {#each buttons as button}
                    {#if currentPage + button >= 0 && currentPage + button <= pageCount}
                    <li>
                        <button
                            class:active={currentPage === currentPage + button}
                            on:click={e => goto(`/search/${keyword}/${currentPage + button}`)}>
                            {currentPage + button + 1}
                        </button>
                    </li>
                    {/if}
                {/each}
            </div>
        {/if}

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
        margin-right: 1.5rem;
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
    .row{
        display: flex;
        flex-direction: row;
        margin-bottom: 2.25rem;
        /* justify-content: space-between; */
    }
</style>
