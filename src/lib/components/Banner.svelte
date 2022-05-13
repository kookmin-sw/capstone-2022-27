<script>
import BookaPickBox from "./BookaPickBox.svelte"
import PickBook from "./PickBook.svelte"
export let img= ""
export let desc= ""
export let keywords = []
export let bgColor=""
</script>

<div class="container">
    <div class='col'>
        <div class='left-banner' style="width:100%; position:relative">
            <div class='vertical-center'><PickBook img={img} starColor='#23E771'></PickBook></div>
        </div>
    </div>
    <div class='col'>
        <div style="width:50%">
            <BookaPickBox/>
            <div class='desc'>
                <div class="desctext">{@html desc}</div>
                {#each keywords as keyword}
                    <a class='keyword' href={`./book/${keyword}`}>#{keyword} </a>
                {/each}
            </div>
        </div>
        
        <div style="width:50%; position:relative">
            <div class='centered'><PickBook img={img} starColor='#23E771'></PickBook></div>
        </div>

    </div>
    <div class='col'>
        <div>
            <BookaPickBox backgroundColor="#FF68CC" textColor="#1B1D1F" />
            <div class="right-desc-container">
                <div class="right-desc">생각을 바꾸려면<br/> 왜 과학자의 태도가 필요할까</div>
                <div class="right-keyword">#알고리즘 #과학자 #편협성</div>
            </div>
        </div>
    </div>
</div>
    
<style>
    .container .col:nth-child(1) { flex-grow: 1; background-color: #9EA4AA; width: 15rem;}
    .container .col:nth-child(2) { flex-grow: 1; background-color: #26282B; width: 42rem;}
    .container .col:nth-child(3) { flex-grow: 1; background-color: #E9EBED; width: 15rem;}

    .container {
        /* display: flex; */
        display: inline-flex;
        align-items: left;
        height: 22.5rem;
    }

    .col{
        display: flex;
        /* justify-content: center; */
        /* align-items: center; */
    }

    .keyword{
        text-decoration: none !important;
        font-style: normal;
        font-weight: 400;
        font-size: 0.75rem;
        color: #23E771;
    }

    .desc{
        margin-left: 1.5rem;
        margin-top: 3.3rem;
    }
    .center{
        flex: auto;
        display: flex;
        justify-content: center;
    }
    .left-banner{
        padding: 3.3rem 1.5rem;
    }
    .right-desc-container{
        padding: 3.3rem 1.5rem;
    }
    .centered {
        position: absolute;
        top: 50%;
        left: 50%;
        transform: translate(-50%, -50%);
    }

    .desctext{
        font-size: 1.5rem;
        font-weight: 700;
        color:#FFFFFF;
    }

    .vertical-center {
        margin: 0;
        position: absolute;
        top: 50%;
        -ms-transform: translateY(-50%);
        transform: translateY(-50%);
    }

    .right-desc{
        font-weight: 700;
        font-size: 1.5rem;
    }

    .right-keyword{
        text-decoration: none !important;
        font-style: normal;
        font-weight: 400;
        font-size: 0.75rem;
        color: #FF68CC;
    }
    
</style>