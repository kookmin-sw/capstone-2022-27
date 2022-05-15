<script>
    import { profileMockup } from '../lib/api'
    import '../../static/fonts/pretendard-subset.css'
    import { goto } from '$app/navigation';
    import { stores_TOKEN, stores_nickname, stores_first } from '$lib/stores';

    let _nickname, token=''
    stores_TOKEN.subscribe(value => {
        token = value;
    });
    stores_nickname.subscribe(value => {
        _nickname = value;
    });

    let profileInit = profileMockup()
    let searchWord = ""

    function gotoSearch(){
        if(searchWord.charAt(0) == '#'){
            goto('/search/keyword/'+searchWord.substring(1))
        } else{
            goto('/search/'+searchWord)
        }

    }

    function logout(){
        _nickname='', token=''
        stores_TOKEN.update(x => '')
        stores_nickname.update(x => '')
        stores_first.update(x => 'false')
        goto('login')
    }

    const onKeyPress = e => {
    if (e.charCode === 13) gotoSearch() // 13 : enterKey
    };
    
</script>

<nav class='container'>
    <div class='col'></div>
    <div class='col space-between' >
        <div class='booka'>
            <a href="/"><img class ='booka-img' src="../../static/booka.svg" alt=''/></a>
        </div>
        <div class='right'>
            <div class='search vertical-center-parent'> 
                <img src="../../static/search.svg" alt=''/>
                <input type="text" name="" on:keypress={onKeyPress} bind:value="{searchWord}"
                placeholder="책 제목 또는 '#키워드'로 검색하세요"  class="custom-input">
            </div>
            {#if token != ''}
                <div class='profile vertical-center'>
                    {#await profileInit};
                    {:then profile} 
                        <div class="circle "></div>
                        <div class='username'>{_nickname}</div>
                        <div class="logout" on:click={logout}>로그아웃</div>
                    {/await}
                </div>
            {:else}
                <div class='profile vertical-center'>
                    <a href="/login"><div>로그인</div></a>
                </div>
            {/if}
        </div>
    </div>
    <div class='col'></div>
</nav>

<slot></slot>

<style>
    .container .col:nth-child(1) { flex-grow: 1; width: 15rem;}
    .container .col:nth-child(2) {
         flex-grow: 1;
         width: 42rem;
         justify-content: space-between;
    }
    .container .col:nth-child(3) { flex-grow: 1; width: 15rem;}

    .container {
        display: flex;
        /* align-items: left; */
    }

    .col{
        display: flex;
        align-items: center;
    }
    .space-between{
        display: flex;
        justify-content: space-between;
    }

    nav {
        height: 3.75rem;
        display: flex;
        background-color: #37DBFF;
    }
    .right{
        display: inline-flex;
        align-items: center;
    }
    .profile{
        display: flex;
        flex-wrap: nowrap;
        flex-direction: row;
    }
    .username{
        margin-left: .3rem;
        margin-right: .3rem;
        font-size: 2rem;
        font-style: normal;
        font-weight: 600;
        font-size: 0.75rem;
        line-height: 1rem;
        vertical-align: middle;
    }
    .logout{
        margin-left: .3rem;
        margin-right: .5rem;
        font-size: 2rem;
        font-style: normal;
        font-weight: 600;
        font-size: 0.75rem;
        line-height: 1rem;
        vertical-align: middle;
        color: #444;
        cursor: pointer;
    }
    .circle{
        width:1.25rem;
        height:1.25rem;
        border-radius: 50%;
        background-color: #FFB4E6;
    }
    .vertical-center-parent {
        display: flex;
        height: 100%;
        justify-content: center;
        align-items: center;
        text-align: center;
    }
    .custom-input{
        border-width: 0px 0px 1px;
        font-size: 14px;
        text-align: left;
        letter-spacing: 0px;
        color: #323A47;
        padding-bottom: 5px;

        transition: 0.4s border-color ease;
    }
    .search{
        margin-right: 2.5rem;
        width:19.375rem
    }
    .search>img{
        margin: -0.1rem 0 0.3rem 0 ;
    }
    input{
        display: flex;
        font-family: 'Pretendard';
        font-style: normal;
        font-weight: 400;
        font-size: 0.9rem;
        flex-grow: 1;
        background-color: #00000000;
    }
    .custom-input:focus{
        outline: none;
        border-color: #323A47;
    }
    .booka{
        margin-left: 0.5rem;
    }
    .booka-img{
        width:5.9rem;
        height:1.31rem;
        
    }
    

:global(a){
    text-decoration: none;
    color: #26282B;
}
:global(a:link){
    text-decoration: none;
    color: #26282B;
}
:global(a:visited){
    text-decoration: none;
    color: #26282B;
}
</style>