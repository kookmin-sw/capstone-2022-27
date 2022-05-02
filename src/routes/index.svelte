<div class="content">
    
        {#await initBanner}
            <p>loading..</p>
        {:then banner}
            <Banner img={banner.image} desc={banner.desc} 
            keywords={banner.keyword} bgColor = {banner.bgColor} />
        {/await}
    
    
    <div class=' horizontal-center'>
        <div class='RecomLists'>
        <p class='foryou'>당신을 위한 추천</p>
        <hr style="borderr:solid 1px #26282B">
        {#await init}
            <p>waiting..</p>
        {:then recoms}
            {#each recoms as recom}
                <div><RecomList recom={recom}/></div>
            {/each}
        {:catch error}
            <p>error: {error.message}</p>
        {/await}
        </div>
    </div>

</div>

<script>
    import Banner from '$lib/components/Banner.svelte'
    import RecomList from '$lib/components/RecomList.svelte'
    import { mainBannerMockup, recomsMockup } from '../lib/api'
    
    const init = recomsMockup()
    const initBanner=  mainBannerMockup()
</script>

<style>
    .content {
        display: flex;
        flex-direction: column;
    }

    :global(.row) {
        display: flex;
        flex-wrap: nowrap;
        flex-direction: row;
    }
    .foryou{
        font-family: 'Pretendard';
        font-style: normal;
        font-weight: 700;
        font-size: 1rem;
        line-height: 1.25px;
    }
    .RecomLists{
        width: 42rem;
    }

    .horizontal-center {
        display: flex;
        justify-content: center;
    }

</style>