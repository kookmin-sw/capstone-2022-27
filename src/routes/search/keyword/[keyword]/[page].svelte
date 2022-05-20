<script>
    import { bookSearch, bookSearchKeywords, booksMockup} from '$lib/api'
    import { page } from '$app/stores';
    import SearchBookList from '$lib/components/SearchBookList.svelte';
    import { goto } from '$app/navigation';
    import Loading from '$lib/components/Loading.svelte';

    export let buttons = [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5];
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
            books = await bookSearchKeywords(keyword, currentPage)
            console.log(books)
            isloaded=true
            pageCount = Math.floor(books.count/pageNum);
        } catch (e) {console.error(e)}
        
    }
    
    getBookSearch()
    $: {
        if (keyword != $page.params.keyword || currentPage != Number($page.params.page)) {
            keyword = $page.params.keyword
            currentPage = Number($page.params.page)
            getBookSearch()
        }
    }
</script>

<div class='center'>
    <div class="container">
        {#if isloaded}
        <div class='result'>'#{keyword}' 검색 결과</div>
        <hr style="border: 1px solid #26282B;"/>

        <div class='container'>
            <SearchBookList nowKeyword = {keyword} books = {books.books}/>
            <div class='col'>
                    {#each buttons as button}
                        {#if currentPage + button >= 0 && currentPage + button <= pageCount}
                        
                        <button
                            class:active={currentPage === currentPage + button}
                            on:click={e => goto(`/search/${keyword}/${currentPage + button}`)}>
                            {currentPage + button + 1}
                        </button>

                        {/if}
                    {/each}
                </div>
        </div>
        {:else}
            <Loading></Loading>
        {/if}
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
    
    button {
        background-color: #EEE;
        border: none;
        border-radius: 10px;
        color: #454C53;
        padding: 7px 12px;
        text-align: center;
        text-decoration: none;
        display: inline-block;
        font-size: 12px;
        margin: 3px 8px 3px 0;
        cursor: pointer;
        transition: .2s ease-in-out;
    }
    button:hover, button.active {
        background-color: rgb(45, 189, 205);
        color: white;
    }
</style>
