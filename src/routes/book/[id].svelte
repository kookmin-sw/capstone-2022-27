<script>
    import { bookDetail ,writeReview, getReviewPage} from '$lib/api'
    import { page } from '$app/stores';
    import BookIntro from '$lib/components/BookIntro.svelte';
    import RecomList from '$lib/components/RecomList.svelte';
    import BookSmall from '$lib/components/BookSmall.svelte';
    import Review from '$lib/components/Review.svelte';
    import Rating from '$lib/components/Rating.svelte'
    import BookStatusBtn from '$lib/components/BookStatusBtn.svelte';
    import BookList from '$lib/components/BookList.svelte';
    import Loading from '$lib/components/Loading.svelte';
    import {onMount} from 'svelte';

    let id = $page.params.id
    let loaded=false;
    let book, reviews, num_review
    let reviewpage = 0
    let randkey = Math.random()

    let rating = 0;
    const ratings = [10 , 9 , 8 , 7 , 6 , 5 , 4 , 3 , 2 , 1]
    let myreview = ''
    let read_state = ''

    async function mount () {
        loaded = false
        bookDetail(id).then(res=> {
            book = res
            reviews = book.reviews
            if (book.my_review) {
                myreview = book.my_review.content
                rating = book.my_review.score
                read_state = book.my_review.read_state
            } else {
                myreview = ''
                rating = 0
                read_state = ''
            }

            num_review = book.book.num_review
            reviewpage = 0
            randkey = Math.random()
            loaded = true
        }).catch(err=>{})
    }
    
    function loadReviews(page){
        getReviewPage(id, page).then(res =>{
            reviews = res
        })
    }
    function loadMoreReviews(){
        reviewpage++
        getReviewPage(id, reviewpage).then(res =>{
            reviews = reviews.concat(res)
        })
    }

    $: reviews
    
    async function writeReviewClicked(){
        console.log(rating)
        let res = await writeReview(id, '읽었어요', rating, myreview)
        loadReviews(0)
        myreview=''
    }

    $: {
        if (loaded && id != $page.params.id) {
            id = $page.params.id
            mount()
        }
    }
    onMount(mount)

</script>

<div class="book-detail">
    {#if !loaded}
        <Loading></Loading>
    {:else}
        <div class="book-container">
            <div class='col margin'>
                <div class="image" style="background-image: url('{book['book']['image']}');"></div>
                <div class='bookinfo'>
                    <div class="title">{book['book']['title']}</div>
                    <div class="summary">{book['book']['subtitle']}</div>
                    <div class="author"><b>{book['book']['author']}</b> 지음 | <b>{book['book']['publisher']}</b> 펴냄 </div>
                    <div class="keywords">
                        {#each book['book']['keywords'] as keyword}
                            <a href='/search/keyword/{keyword}/0' class='keyword'>#{keyword} </a>
                        {/each}
                    </div>
                    <div class='col button_container'>
                        <BookStatusBtn book_id={id} status={read_state}
                            rating={rating} content={myreview}/>
                    </div>

                </div>
            </div>
        </div>
        <div class='margin'>
            <BookIntro title="책 소개" content="{book['book']['desc']}"/>
            <div class='index'><BookIntro  title="목차" content="{book['book']['desc_index']}"/></div>
            <div class='index'><BookIntro  title="출판사 책 소개" content="{book['book']['desc_pub']}"/></div>

            <div class='title index'> 리뷰 <div class="num_review"> {num_review} </div> </div> 
            <hr class='border'>
            <div>
                {#each reviews as review}
                <div id='review-wrapper'>
                    <Review username='{review.user_name}' date='{new Date(review.created_at).toLocaleDateString()}' 
                    review='{review.content}' bind:rating='{review.score}' />
                </div>
                {/each}
                
                {#if num_review > reviews.length}
                    <div class='load-more' on:click={loadMoreReviews}>{Math.min(3, num_review - reviews.length)}개의 리뷰 더 보기<img src="../static/bottom_arrow.svg" on:click="{e=> opened = !opened}" alt=''/></div>
                {/if}
            </div>
            <div>
                <div class='col'>
                    <div class="circle"></div>
                    <div id='profile-wrapper'>
                        <div class="col" >
                            <div id='my-rating-title'>나의 별점</div>
                            <fieldset class="rate">
                                {#each ratings as r}
                                    <input type="radio" id="rand{randkey}{r}" disabled={false} bind:group={rating} name="rand{randkey}" value="{r}" />
                                    <label for="rand{randkey}{r}" class="{r%2==1?'half':''} 'enabled'"></label>
                                {/each}
                            </fieldset>
                        </div>
                        <textarea id='write-review' placeholder="리뷰를 남겨주세요"
                        bind:value={myreview}/>
                    </div>
                </div>
                <div class='right'>
                    <div id='review-word-count'>{myreview.length}/10000</div>
                    <div id='review-btn' class={myreview.length && rating!=0?'filled':''} on:click='{() => {if (myreview.length && rating!=0) {writeReviewClicked()}}}'><p>리뷰 등록</p></div>
                </div>
            </div>
            <div class='similar'>
                <div class='title'>비슷한 책</div>
                <hr class='border'>
                <div class='row'>
                <BookList books={book['similar']}/>
                </div>
            </div>
        </div>
    {/if}
</div>

<style>
    .num_review {
        margin-left: .3rem;
        font-family: 'Pretendard';
        font-style: normal;
        font-weight: 700;
        font-size: 15px;
        line-height: 18px;
        /* identical to box height */
        color: #37DBFF;
        display: inline-block;
    }
    .load-more {
        margin: 2rem 1rem 3rem;
        box-sizing: border-box;
        display: flex;
        flex-direction: row;
        justify-content: center;
        align-items: center;
        padding: 12px;
        gap: 8px;

        background: #FFFFFF;
        border: 0.5px solid #26282B;
        border-radius: 2px;
        cursor: pointer;
        transition: .2s ease-in-out;
    }
    .load-more:hover {
        background: #EEE;
    }
    #review-wrapper{
        margin-bottom: 1.375rem;
    }
    .book-container {
        width: 100%;
        display: flex;
        flex-direction: column;
        align-items:flex-start;
        margin-bottom: 1rem;
        padding-top: 3rem;
        padding-bottom: 4rem;
        background-color: #F7F8F9;
    }
    .margin {
        width: calc(18rem + 33%);
        margin: 0 auto;
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
    #profile-wrapper{
        /* display: flex; */
        padding-left: 0.5rem;
        width:100%;
    }

    .book-detail {
        display: flex;
        flex-direction: column;
    }

    .bookinfo{
        margin-left: 2rem;
        margin-top: 2rem;
        width:80%;
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
        color: #26282B;
        border-color: #26282B;
        transition: .3s ease-in-out;
    }
    .keyword:hover{
        color: rgb(45, 189, 205);
        border-color: rgb(45, 189, 205);
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

    .button_container{
        margin-top: 2rem;
    }

    .index{
        margin-top:3rem;
    }

    .title{
    font-family: 'Pretendard';
    font-style: normal;
    font-weight: 700;
    font-size: 1rem;
    line-height: 1.25rem;
    }
    .border{
        border:solid 1px #26282B;
        margin-top: 1rem;
    }

    .similar{
        margin-top: 3rem;
    }
    .title{
    font-family: 'Pretendard';
    font-style: normal;
    font-weight: 700;
    font-size: 1rem;
    line-height: 1.25rem;
}
#my-rating-title{
    font-family: 'Pretendard';
    font-style: normal;
    font-weight: 400;
    font-size: 0.75rem;
    line-height: 0.875rem;
    color: #9EA4AA;
    padding-right: 0.75rem;
}
#profile-wrapper {
    text-align: center;
}
#write-review{
    resize: none;
    background: #F7F8F9;
    border-radius: 2px;
    border: 0ch;
    padding: 0.5rem;
    margin: 0 auto;
    width: calc(100% - 1rem);
    height: 4.25rem;
    vertical-align: text-top;
}
#write-review:focus{
    outline: none;
}
#review-word-count{
    font-family: 'Pretendard';
    font-style: normal;
    font-weight: 400;
    font-size: 0.75rem;
    line-height: 0.875rem;
    text-align: right;
    color: #9EA4AA;
    padding-right: 0.75rem;
}
#review-btn{
    width: 4.5rem;
    height: 2.25rem;
    background: #9EA4AA;
    border-radius: 2px;
    font-family: 'Pretendard';
    font-style: normal;
    font-weight: 700;
    font-size: 13px;
    line-height: 16px;
    /* identical to box height */

    display: flex;
    align-items: center;
    text-align: center;
    justify-content: center;

    color: #E9EBED;
}
#review-btn.filled {
    background-color: rgb(55, 219, 255);
    color: #ffffff;
}
.circle {
    margin: 0 .2rem 0 0;
    /* width:36px;
    height:36px; */
    width: 2.25rem;
    height: 2.25rem;
    background-color: #23E771;
    border-radius: 50%;
    display: flex;
    flex-shrink: 0;
}
.right{
    display: flex;
    justify-content: flex-end;
    align-items: center;
    padding-top: 0.75rem;
}



/* Base setup */
@import url(//netdna.bootstrapcdn.com/font-awesome/3.2.1/css/font-awesome.css);

/* Ratings widget */
.rate {
    display: inline-block;
    border: 0;
}
/* Hide radio */
.rate > input {
    display: none;
}
/* Order correctly by floating highest to the right */
.rate > label {
    float: right;
}
/* The star of the show */
.rate > label:before {
    display: inline-block;
    /* padding: .3rem .1rem; */
    padding-right:0.1rem ;
    margin: 0;
    cursor: pointer;
    font-family: FontAwesome;
    content: "\f005 "; /* full star */
    
    font-size: 16px;
    padding-top: 0.1rem;
}

/* Half star trick */
.rate .half:before {
    content: "\f089 "; /* half star no outline */
    position: absolute;
    /* padding-right: 0; */

    font-size: 16px;
    padding-top: 0.1rem;
}

label {
    color: #E9EBED;
}
/* Click + hover color */
input:checked ~ label, /* color current and previous stars on checked */
label.enabled:hover, label.enabled:hover ~ label { color: #07ABCF;  } /* color previous stars on hover */

/* Hover highlights */
input:checked + label.enabled:hover, input:checked ~ label:hover, /* highlight current and previous stars */
input:checked ~ label.enabled:hover ~ label, /* highlight previous selected stars for new rating */
label.enabled:hover ~ input:checked ~ label /* highlight previous selected stars */ { color: #37DBFF;  } 

fieldset {
    padding: 0;
}


    
</style>