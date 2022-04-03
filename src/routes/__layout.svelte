<script>
    // export let userId=0
    // export let userToken=""

    import { profileMockup } from '../lib/api'
    let profileInit = profileMockup()
</script>

<nav>
    <div class="right"> 
        <div class='profile'>
            {#await profileInit};
            {:then profile} 
                <div class="profileImg" style="background-image: url('{profile.profileImg}');"></div>
                <div class='username'>{profile.username}</div>
            {/await}
        </div>
    </div>

</nav>
<slot></slot>

<style>
    nav {
        display: flex;
        align-items: center;
        justify-content: space-between;
    
        box-shadow: 0px 5px 12px 0px rgba(0,0,0,0.11);
        
        padding: 1rem;
        z-index: 1;
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
    .profileImg{
        width: 3rem;
        height: 3rem;
        background: #333;
    }
    .username{
        margin-left: 2rem;
        margin-right: 2rem;
        font-size: 2rem;
    }
</style>