<script>
    import { profileMockup } from '../lib/api'
    import '../../static/fonts/pretendard-subset.css'
    import { goto } from '$app/navigation';
    import { stores_TOKEN, stores_nickname, stores_first } from '$lib/stores';
import { onMount } from 'svelte';

    let _nickname, token=''
    stores_TOKEN.subscribe(value => {
        if (value) {
            token = value
        } else {
            token = ''
        }
    });
    stores_nickname.subscribe(value => {
        if (value) {
            _nickname = value
        }
    });

    let profileInit = profileMockup()
    let searchWord = ""

    function gotoSearch(){
        if(searchWord.charAt(0) == '#'){
            goto('/search/keyword/'+searchWord.substring(1)+'/0',)
        } else{
            goto('/search/'+searchWord+'/0', {replaceState: true})
        }

    }

    function logout(){
        console.log("logout")
        _nickname='', token=''
        stores_TOKEN.update(x => '')
        stores_nickname.update(x => '')
        stores_first.update(x => 'false')
        localStorage.setItem('token', '')
        localStorage.setItem('nickname', '')
        localStorage.setItem('isfirst', '')
        goto('login')
    }

    const onKeyPress = e => {
        if (e.charCode === 13) gotoSearch() // 13 : enterKey
    };

    onMount(async () => {
        if (token == '' || !token) {
            logout()
        }
    });
    
</script>
<svelte:head>
    <title>Booka</title>
    <link rel="icon" type="image/svg" href={'/favicon.ico'} />
</svelte:head>
<nav class='container'>
    <div class='col'></div>
    <div class='col space-between' >
        <div class='booka'>
            <a href="/"><img class ='booka-img' src="/booka.svg" alt=''/></a>
        </div>
        <div class='right'>
            <div class='search vertical-center-parent'> 
                <img src="/search.svg" alt=''/>
                <input type="text" name="" on:keypress={onKeyPress} bind:value="{searchWord}"
                placeholder="책 제목 또는 '#키워드'로 검색하세요"  class="custom-input">
            </div>
            {#if token!='null' && token != '' && token}
                <div class='profile vertical-center'>
                    {#await profileInit};
                    {:then profile} 
                        <div class="circle "></div>
                        <div class='username' on:click={() => {goto('/myreviews')}}>{_nickname}</div>
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

<div class="footer">
    <div class='booka'>
        <a href="/"><img class ='booka-img' src="/booka.svg" alt=''/></a>
    </div>
    <div class="info">Blueturtle X Flybook</div>
    <div class="info">Capstone project - Team 27</div>
</div>

<style>
    :global(body) {
        font-family: 'Pretendard', 'Noto Sans KR', sans-serif;
    }
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
        margin-left: 1rem;
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
        margin: -0.1rem .3rem 0 0;
        border-radius: 50%;
        background-color: #FFB4E6;
    }
    .username {
        cursor: pointer;
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
        width:16rem
    }
    .search>img{
        margin: 0rem 0.5rem 0rem 0;
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

.footer {
    margin: 5rem 0 0 0;
    width: 100%;
    height: 6rem;
    padding: 2rem 0;
    background-color: #dddddd;
    text-align: center;
    font-family: 'Pretendard';
    font-weight: bold;
    font-size: .8rem;
    color: #666;
}
.footer .info{
    margin: .5rem 0;
}
.footer .booka-img {
    width: 5.9rem;
    height: 1.31rem;
}
</style>