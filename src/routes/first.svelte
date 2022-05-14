<script>
import { goto } from '$app/navigation';

    import { getFristPageList, setFristPageList } from '../lib/api'
    import { stores_TOKEN, stores_nickname, stores_first } from '../lib/stores.js'
    let books
    let loaded = false

    getFristPageList().then(res=> {
        loaded=true
        books = res
    }).catch(err=>{})
    
    async function clickSelectBtn(){
        let selectedBooks=[]
        console.log(books)
        for(let book of books){
            if(book.selected){
                console.log(book.title)
                selectedBooks.push(book.id)
            }
        }
        await setFristPageList(JSON.stringify(selectedBooks))
        stores_first.update(x => 'true')
        goto('/')
    }
</script>
<div class="margin">
    <div id='title-container'>
        <p class='foryou'>읽었던 책을 선택해주세요! </p>
        <hr style="borderr:solid 1px #26282B">
    </div>
    {#if !loaded}
        Loading....
    {:else} 
        <div class='container'>
        {#each books as book}
            <div id='book'>
                <div class="book_small">
                {#if book.selected==true}
                    <div class="image" style="background-image: url('{book.image}');"
                        on:click='{ e=> (book.selected = false)}'>
                        <div class='selected'></div>
                        <!-- <img src="/static/check.svg"> -->
                    </div>
                    
                {:else }
                    <div class="image" style="background-image: url('{book.image}');"
                    on:click='{ e=> (book.selected = true)}'
                    ></div>
                {/if}
                <div class="title">{book.title}</div>
                <div class="author">{book.author}</div>
                </div>
            </div>
        {/each}
        </div>
        <div class='row-reverse'>
            <div class='select-complete-btn' on:click="{clickSelectBtn}">선택 완료</div>
        </div>
    {/if}
    
</div>
<style>
.container{
    display: flex;
    flex-wrap: wrap;
}
.margin
{
    width: calc(18rem + 33%);
    margin: 0 auto;
}
#book{
    /* width: calc(18rem + 33%); */
    width:8rem;
    padding-top: 1rem;
    padding-bottom: 1rem;
    justify-content: center;
    display: flex;
}


.book_small {
    display: flex;
    flex-direction: column;
    align-items: left;
}

.image {
    display: inline-block;
    background-size: cover;
    width: 6rem;
    height: 9rem;
}

.title {
    width: 6rem;
    font-size: 0.825rem;
    text-align: center;
    color: #1B1D1F;
    font-weight: 600;
    margin-top: 0.75rem;
    text-align: left;
}

.author{
    font-size: 0.825rem;
    text-align: left;
    color: #72787F;
    font-weight: 400;
    margin-top:0.25rem ;
}

.selected{
    z-index: 1;
    background-color: #000000bb ;
    margin: 0 0 0 0;
    padding: 0 0 0 0;
    width: 6rem;
    height:9rem;
}
.foryou{
    font-family: 'Pretendard';
    font-style: normal;
    font-weight: 700;
    font-size: 1.5rem;
    line-height: 1.25px;
    }
#title-container{
    margin-top: 3rem;
}

.select-complete-btn{
    background-color: #37DBFF;
    width: 6rem;
    height: 4rem;
    line-height: 4rem;
    text-align: center;
    margin-bottom: 3rem;
}
.row-reverse{
    display: flex;
    flex-direction: row-reverse;
}
</style>