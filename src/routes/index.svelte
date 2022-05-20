<script>
    import { goto } from '$app/navigation';

    import Banner from '$lib/components/Banner.svelte'
    import Loading from '$lib/components/Loading.svelte';
    import RecomList from '$lib/components/RecomList.svelte'
    import { getBanners, mainBannerMockup, mainpage } from '../lib/api'
    import { stores_first } from '../lib/stores.js'
    import { onMount } from 'svelte'
    let recom_types = [0,1,2,3,4]

    let recoms = []
    let loaded = false

    let isfirst
    stores_first.subscribe(value => {
        isfirst = value;
    });
    
    console.log(isfirst)
    if(isfirst=='true'){
        console.log(isfirst)
        goto('/first')
    }
    
    const initBanner=  mainBannerMockup()

    onMount(async () => {
        let futures = recom_types.map(type => mainpage(type))
        Promise.all(futures).then(values => {
            recoms = values
            loaded = true
        })
    })
</script>

<div class="content">    
    {#await initBanner}
        <p>loading..</p>
    {:then banner}
        <Banner banners={banner} />
    {/await}
    
    {#if !loaded}
    <Loading></Loading>
    {:else}
    <div class='container'>
        <div class='col'></div>
        <div class='col'>
            <div class=''>
                <div class='recomlists'>
                    <p class='foryou'>당신을 위한 추천</p>
                    <hr style="border: solid 1px #66686B">
                    
                    {#each recoms as recom}
                        <div class='recomlist'><RecomList recom={recom}/></div>
                    {/each}
                    
                </div>
            </div>
        </div>
        <div class='col'></div>
    </div>
    {/if}
</div>

<style>
    
    .container .col:nth-child(1) { flex-grow: 1; width: 15rem;}
    .container .col:nth-child(2) {
        flex-grow: 1; width: 42rem;
    }
    .container .col:nth-child(3) { flex-grow: 1; width: 15rem;}

    .container {
        /* display: flex; */
        display: flex;
        align-items: center;
    }

    .content {
        display: flex;
        flex-direction: column;
    }

    .row {
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

    .horizontal-center {
        display: flex;
        justify-content: center;
    }
    .recomlists{
        margin-top: 3rem;
        margin-left: 1.5rem;
    }
    .recomlist{
        margin-top: 1rem;
        margin-bottom: 2rem;
    }
</style>