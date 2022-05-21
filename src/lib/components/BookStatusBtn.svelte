<script>
    import { writeReview } from '$lib/api'
    export let book_id
    export let status = ''
    export let rating
    export let content = ''

    if(rating==0){
        console.log("10으로 바꿈")
        rating=10;
    }

    let enabled = true
    let randkey = Math.random()
    let btnColors = ['#FF68CC', '#23E771']
    let ratings = [10 , 9 , 8 , 7 , 6 , 5 , 4 , 3 , 2 , 1]

    async function reviewBtnClicked(){
        console.log(rating)
        const res = await writeReview(book_id, status, rating, content)
    }

    async function changeStar(e){
        let res = await writeReview(book_id, '읽었어요', Number(e.target.value), content)
    }
    
</script>
<div class='container'>
    <div class='status-container col'>
        {#if status=='읽고싶어요'}
            <div class='btn btn-selected' on:click='{e=> { status=''; reviewBtnClicked()}}'>
                <img alt='' src='/hope_selected.svg' >
                <div style='color:{btnColors[0]}'>읽고싶어요</div>
            </div>
        {:else}
            <div class='btn' on:click={e=> {status='읽고싶어요'; reviewBtnClicked()}}>
                <img alt='' src='/hope.svg' >
                <div>읽고싶어요</div>
            </div>
        {/if}

        {#if status=='읽었어요'}
            <div class='btn btn-selected' on:click={e=> {status=''; reviewBtnClicked()}}>
                <img alt='' src='/read_selected.svg' >
                <div style='color:{btnColors[1]}'>읽었어요</div>
            </div>
        {:else}
            <div class='btn' on:click={e=> {status='읽었어요'; reviewBtnClicked()}}>
                <img alt='' src='/read.svg' >
                <div>읽었어요</div>
            </div>
        {/if}
    </div>

    {#if status=='읽었어요'}
        <div class='rating-container'>
            <div id='rating-text-container' class='col'>
                <div id='my-rating-text'>나의 별점</div>
                <div id='rating-text'>{rating/2}</div>
            </div>
            <fieldset class="rate">
                {#each ratings as r}
                    <input on:change={changeStar} type="radio" id="rand{randkey}{r}" disabled={!enabled} bind:group={rating} name="rand{randkey}" value="{r}" />
                    <label for="rand{randkey}{r}" class="{r%2==1?'half':''} {enabled?'enabled':'disabled'}"></label>
                {/each}
            </fieldset>
        </div>
    {/if}

</div>

<style>
.container{
    width:100%;
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
    margin-right: 0.5rem;
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
.rating-container{
    width: 100%;
    background-color: #FFFFFF;
    display: flex;
    justify-content: space-between;
}
#my-rating-text{
    font-family: 'Pretendard';
    font-style: normal;
    font-weight: 400;
    font-size: 0.815rem;
    line-height: 1rem;
    color: #72787F;
    margin-right: 0.25rem;

}
#rating-text{
    font-family: 'Pretendard';
    font-style: normal;
    font-weight: 700;
    font-size: 0.75rem;
    line-height: 0.875rem;
    color: #C9CDD2;
}
.col{
    display: flex;
}
#rating-text-container{
    align-items: center;
    margin-left: 0.5rem;
}
.status-container{
    margin-bottom: 1rem;
}

/**Rating**/
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
    padding: .3rem .1rem;
    margin: 0;
    cursor: pointer;
    font-family: FontAwesome;
    content: "\f005 "; /* full star */
    font-size: 16px;
}

/* Half star trick */
.rate .half:before {
    content: "\f089 "; /* half star no outline */
    position: absolute;
    padding-right: 0;

    font-size: 16px;
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
</style>