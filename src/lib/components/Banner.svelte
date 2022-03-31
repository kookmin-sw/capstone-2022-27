<script>
    export let img= ""
    export let desc= ""
    export let keywords = []
    export let bgColor=""    
</script>
    
<div class="banner" style="background-color:{bgColor}">
    <div class='col'>
        <div class="img" style="background-image: url('{img}');"></div>
        <div class='desc'>
            <p class="desctext">{@html desc}</p>
            {#each keywords as keyword}
                <a class='keyword' href={`./book/${keyword}`}>#{keyword} </a>
            {/each}
        </div>
    </div>
</div>
    
<style>
    
    .banner {
    display: flex;
    flex-direction: column;
    align-items: left;
    justify-content: center;
    /* margin: .5rem; */
    padding: 1rem;
    }

    .col{
        display: flex;
        flex-wrap: nowrap;
        flex-direction: row;
        margin: 2em;
    }

    .img {
    display: inline-block;
    background-size: cover;
    width: 16rem;
    height: 25rem;
    
    box-shadow: 0px 5px 12px 0px rgba(0, 0, 0, 0.14);
    }

    .keyword{
        color:midnightblue;
        font-size: 3em;
        font-weight: 500;
        text-decoration: none !important;

    }

    .desc{
        margin-left: 3em;
        margin-top: 3em;
        font-size: .7em;
    }

    .desctext{
        font-size: 3em;
        font-weight: 100;
    }
    
</style>