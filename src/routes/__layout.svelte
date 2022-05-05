<script>
    // export let userId=0
    // export let userToken=""

    import { profileMockup } from '../lib/api'
    import '../../static/fonts/pretendard-subset.css'
    let profileInit = profileMockup()
    let searchWord = ""
</script>

<nav class='container'>
    <div class='col'></div>
    <div class='col' >
        <div class='booka'>
            <img class ='booka-img' src="../../static/booka.svg" alt=''/>
        </div>
        <div class='search vertical-center-parent'> 
            <img src="../../static/search.svg" alt=''/>
            <input type="text" name="" placeholder="책 제목 또는 '#키워드'로 검색하세요"  class="custom-input">
        </div>
            <div class='profile vertical-center'>
                {#await profileInit};
                {:then profile} 
                    <div class="circle "></div>
                    <div class='username'>{profile.username}</div>
                {/await}
            </div>
    </div>
    <div class='col'></div>
    
</nav>

<slot></slot>

<style>
    .container .col:nth-child(1) { flex-grow: 1; width: 15rem;}
    .container .col:nth-child(2) { flex-grow: 1; width: 42rem;}
    .container .col:nth-child(3) { flex-grow: 1; width: 18rem;}

    .container {
        display: flex;
        /* align-items: left; */
    }

    .col{
        display: flex;
        /* justify-content: center; */
        align-items: center;
    }

    nav {
        height: 3.75rem;
        display: flex;
        background-color: #37DBFF;
    }
    .right{
        text-align: right;
        margin-left: auto; 
        margin-right: 0;
    }
    .profile{
        display: flex;
        flex-wrap: nowrap;
        flex-direction: row;
    }
    .username{
        margin-left: 1rem;
        margin-right: 1rem;
        font-size: 2rem;
        font-style: normal;
        font-weight: 600;
        font-size: 0.75rem;
        line-height: 0.875rem;
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
</style>