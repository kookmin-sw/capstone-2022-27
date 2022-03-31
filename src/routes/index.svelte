<div class="content">

    {#await initBanner}
        <p>loading..</p>
    {:then banner}
        <Banner img={banner.image} desc={banner.desc} 
        keywords={banner.keyword} bgColor = {banner.bgColor} />
    {/await}
    
    
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

<script>
    import Banner from '$lib/components/Banner.svelte'
    import RecomList from '$lib/components/RecomList.svelte'
    import { mainBannerMockup, recomsMockup } from '../lib/api'
    
    const init = recomsMockup()
    const initBanner=  mainBannerMockup()
</script>

<style>
    .content {
        margin: 1rem;
        display: flex;
        flex-direction: column;
    }

    :global(.row) {
        display: flex;
        flex-wrap: nowrap;
        flex-direction: row;
    }
</style>