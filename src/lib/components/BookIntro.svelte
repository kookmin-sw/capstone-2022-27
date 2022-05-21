<script>
export let title=""
export let content=""
let opened = false
let maxCharacters = 200
let shortContent = content.length > maxCharacters ? content.substring(0, maxCharacters)+"..." : content

</script>
<div>
    <div class='col'>
        <div class='title'>{title} </div>
        <div class='img'>
            {#if shortContent.length != content.length}
                {#if opened}
                    <img src="/top_arrow.svg" on:click="{e=> opened = !opened }" alt=''/>
                {:else}
                    <img src="/bottom_arrow.svg" on:click="{e=> opened = !opened}" alt=''/>
                {/if}
            {/if}
        </div>
    </div>
    <hr class='border'>
    <div class='content'>{@html opened?content:shortContent }</div>
</div>

<style>
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
.content{
    margin-top: 1rem;
    font-family: 'Pretendard';
    font-style: normal;
    font-weight: 400;
    font-size: 0.938rem;
    line-height: 1.313rem;
    overflow: hidden;
    white-space:pre-wrap;
}
/* .content.opened{
    max-height: auto;
    height: auto;
} */
.col{
    display: flex;
    flex-wrap: nowrap;
    flex-direction: row;
    vertical-align:middle;
    justify-content: space-between;
}
</style>