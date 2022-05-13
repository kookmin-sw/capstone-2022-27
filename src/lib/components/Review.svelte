<script>
    import Rating from "./Rating.svelte"
    export let username="익명"
    export let date
    export let rating
    export let review
</script>

<div>
    <div class='col'>
        <div class="circle"></div>
        <div id='profile-wrapper'>
            <div id='username'>{username}</div>
            <div class="col">
                <div id='date'>{date}</div>
                <div id=''>{rating}</div>
                <Rating rating={rating}/>
            </div>
            
            <div id='content' class="cut-text">{review}</div>
        </div>
    </div>
</div>

<style>
#username{
    font-family: 'Pretendard';
    font-style: normal;
    font-weight: 700;
    font-size: 13px;
    line-height: 1rem;
    color: #000000;
}
#date{
    font-family: 'Pretendard';
    font-style: normal;
    font-weight: 400;
    font-size: 12px;
    line-height: 1rem;
    color: #9EA4AA;
}
#content{
    font-family: 'Pretendard';
    font-style: normal;
    font-weight: 400;
    font-size: 0.75rem;
    color: #000000;
    margin-top:0.75rem;
}
.cut-text{
    white-space: normal;
    line-height: 1.2rem;
    text-align: left;
    word-wrap: break-word;
}
.cut-text:not(:hover) {
    max-height: 5em;
    overflow: hidden;
    text-overflow: ellipsis;
}
.cut-text:hover{
    height: auto;
    overflow: visible;
}
#profile-wrapper{
    margin-left: 0.5rem;
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
.col{
    display: flex;
    vertical-align: middle;
}
</style>