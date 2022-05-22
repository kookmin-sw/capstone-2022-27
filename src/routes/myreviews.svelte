<script>
    import { myReviews } from '$lib/api'
    import { page } from '$app/stores';
    import SearchBookList from '$lib/components/SearchBookList.svelte';
    import { goto } from '$app/navigation';
    import Loading from '$lib/components/Loading.svelte';
    import Review from '$lib/components/Review.svelte';
    import Rating from '$lib/components/Rating.svelte';
    import { onMount } from 'svelte';
    import RecomList from '$lib/components/RecomList.svelte';

    let isloaded=false

    let reviews = []
    let recom = {
        title: '',
        books: []
    }
    
    async function getMyReviews(){
        isloaded=false
        try {
            let data = await myReviews()
            recom.books = data.filter(data => data.read_state == '읽고싶어요')
            recom.books = recom.books.map(data => data.book)
            reviews = data.filter(data => data.read_state == '읽었어요')
            isloaded=true
        } catch (e) {console.error(e)}
        
    }
    
    onMount(getMyReviews)
</script>

<div class="center outer">
    <div class='center'>
        <div class="container">
            {#if isloaded}
            <div class='result-bar top'><div class='result'>읽고 싶은 도서</div><div class="num_review"> {recom.books.length} </div></div>
            <hr style="border: 1px solid #26282B;"/>
            <RecomList recom={recom}/>
            <div class='result-bar'><div class='result'>내 리뷰</div><div class="num_review"> {reviews.length} </div></div>
            <hr style="border: 1px solid #26282B;"/>
    
            <div class='container'>
                {#each reviews as review}
                {#if review.read_state == '읽었어요'}
                <div class="review">
                    <div class="row">
                        <a href="/book/{review.book.id}"><div class="image-wrap"><div class="image" style="background-image: url('{review.book.image}');"></div></div></a>
                        <a href="/book/{review.book.id}" class="right-items"> 
                            <div class="right">
                                <div class='title'><div>{review.book.title}</div> <Rating rating={review.score}/></div>
                                <div class='date'><div>{(new Date()).toLocaleDateString()}</div></div>
                                <div class='{"content" + (review.content ? '' : ' grey')}'>{review.content?review.content:'리뷰를 작성하지 않았습니다.'}</div>
                            </div>
                        </a>
                    </div>
                </div>
                {/if}
                {/each}
            </div>
            {:else}
                <Loading></Loading>
            {/if}
        </div>
    </div>
</div>

<style>
    .top {
        margin-top: .5rem;
    }
    .num_review {
        margin-left: .5rem;
        font-family: 'Pretendard';
        font-style: normal;
        font-weight: 700;
        font-size: 15px;
        line-height: 1.313rem;
        color: #37DBFF;
        display: inline-block;
        padding: 0 0 0 0;
    }
    .date {
        font-family: 'Pretendard';
        font-style: normal;
        font-weight: 400;
        font-size: 12px;
        line-height: 1rem;
        color: #9EA4AA;
        padding-right: 0.5rem;
        display: flex;
        justify-content: space-between;
    }
    .content.grey{
        color: #aaa;
    }
    .state{
        margin-top: .3rem;
        color: #666;
        font-weight: 600;
    }
    .center{
        justify-content: center;
        align-items: center;
        display: flex;
    }
    .container.outer{
        width: 39.375rem;
    }
    .right-items{
        display: inline-block;
        width: 100%;
    }
    .inner-row{
        width: 100%;
        display: flex;
        justify-content: space-between;
    }
    .row {
        width: 39.375rem;
    }
    .result{
        margin: 2.563rem 0 1.5rem 0;
        font-family: 'Pretendard';
        font-style: normal;
        font-weight: 700;
        font-size: 1.313rem;
        line-height: 1.313rem;
        color: #1B1D1F;
        display: inline-block;
    }
    .content {
        font-family: 'Pretendard';
        font-style: normal;
        font-weight: 400;
        font-size: 0.8rem;
        color: #333;
        height: 2rem;
        margin-top: 0.25rem;
    }
    hr{
        margin-bottom: 1.5rem;
    }
    .title{
        font-family: 'Pretendard';
        font-style: normal;
        font-weight: 700;
        font-size: 1.063rem;
        line-height: 1.25rem;
        display: flex;
        justify-content: space-between;
        color: #1B1D1F;
    }

    .button-bar {
        display: flex;
        flex-direction: row;
        justify-content: center;
        align-items: center;
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
    .title {
        margin-bottom: .3rem;
    }
    .date {
        margin-bottom: .5rem;
    }
    .image-wrap {
        width: 4.4rem;
        height: 6.6rem;
        margin-right: 1.5rem;
        position: relative;
        display: inline-block;
    }
    .image{
        position: absolute;
        display: inline-block;
        width: 4.4rem;
        height: 6.6rem;
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
        margin-top: .5rem;
    }
    .row{
        display: flex;
        flex-direction: row;
        margin-bottom: .5rem;
        /* justify-content: space-between; */
    }
    .review {
        margin-bottom: 2.4rem;
    }
</style>
