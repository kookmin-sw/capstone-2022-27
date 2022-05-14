<script>
    import { bookDetail ,profileMockup} from '$lib/api'
    import { page } from '$app/stores';
    import BookIntro from '$lib/components/BookIntro.svelte';
    import RecomList from '$lib/components/RecomList.svelte';
    import BookSmall from '$lib/components/BookSmall.svelte';
    import Review from '$lib/components/Review.svelte';
    import Rating from '$lib/components/Rating.svelte'
import BookStatusBtn from '$lib/components/BookStatusBtn.svelte';

    let id = $page.params.id
    const bookP = bookDetail(id)

    function handleMessage(event) {
		alert(event.detail.text);
	}

</script>

<div class="book-detail">
    {#await bookP}
        <p>loading...</p>
    {:then book}
        <div class="book-container">
            <div class='col margin'>
                <div class="image" style="background-image: url('{book['book']['image']}');"></div>
                <div class='bookinfo'>
                    <div class="title">{book['book']['title']}</div>
                    <div class="summary">{book['book']['subtitle']}</div>
                    <div class="author"><b>{book['book']['author']}</b> 지음 | <b>{book['book']['publisher']}</b> 펴냄 </div>
                    <div class="keywords">
                        {#each book['book']['keywords'] as keyword}
                            <a href=' ' class='keyword'>#{keyword} </a>
                        {/each}
                    </div>
                    <div class='col button_container'>
                        {#if book.my_review == null}
                            <BookStatusBtn book_id={book.book.id} status='' content=''/>
                        {:else}
                            <BookStatusBtn book_id={book.book.id} status={book.my_review.read_state}
                                rating={book.my_review.score} content={book.my_review.content}/>
                        {/if}
                    </div>

                </div>
            </div>
        </div>
        <div class='margin'>
            <BookIntro title="책 소개" content="{book['book']['desc']}"/>
            <div class='index'><BookIntro  title="목차" content="{book['book']['desc_index']}"/></div>
            <div class='index'><BookIntro  title="출판사 책 소개" content="{book['book']['desc_pub']}"/></div>

            <div class='title index'> 리뷰 </div>
            <hr class='border'>
            <div>
                {#each book.reviews as review}
                <div id='review-wrapper'>
                    {review.score}
                    <Review username='{review.user_name}' date='{new Date(review.created_at).toLocaleDateString()}' 
                    review='{review.content}' bind:rating='{review.score}' on:message={handleMessage} />
                </div>
                {/each}
            </div>

            <div>
                <div class='col'>
                    <div class="circle"></div>
                    <div id='profile-wrapper'>
                        <div class="col">
                            <div id='my-rating-title'>나의 별점</div>
                            <Rating rating=0 enabled=true/>                            
                        </div>
                        <input id='write-review' placeholder="리뷰를 남겨주세요"/>
                    </div>
                </div>
                <div>
                    <div id='review-word-count'>/1000</div>
                    <div id='review-btn'>리뷰 등록</div>
                </div>
                </div>
            
            <div class='similar'>
                <div class='title'>비슷한 책</div>
                <hr class='border'>
                <div class='row'>
                {#each book['similar'] as book}
                    <a class='book' href={`./${book.id}`}><BookSmall image={book.image} title={book.title} author={book.author}/></a>
                {/each}
                </div>
            </div>
        </div>
    {:catch error}
        <p>error: {error.message}</p>
    {/await}
</div>

<style>
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
}
#write-review{
    background: #F7F8F9;
    border-radius: 2px;
    border: 0ch;
    flex-grow: 1;
    padding: 0.5rem;
}
#review-word-count{
    font-family: 'Pretendard';
    font-style: normal;
    font-weight: 400;
    font-size: 0.75rem;
    line-height: 0.875rem;
    text-align: right;
    color: #9EA4AA;
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

    color: #E9EBED;
}
.circle {
    margin: 0;
    /* width:36px;
    height:36px; */
    width: 2.25rem;
    height: 2.25rem;
    background-color: #23E771;
    border-radius: 50%;
    display: flex;
    flex-shrink: 0;
}

    
</style>