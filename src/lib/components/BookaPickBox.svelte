<script>
export let backgroundColor="#1B1D1F"
export let textColor="#24E772"
</script>

<div class="abs">
    <div class='booka-pick center' style="background-color:{backgroundColor}; color:{textColor}">booka Pick</div>
</div>

<style>
.booka-pick{
    width: 8.1rem;
    height: 2.4rem;
    justify-content: center;
    align-items: center;
    text-align: center;
    font-family: 'Museo Slab';
    font-style: normal;
    font-weight: 900;
    font-size: 1rem;
}

.abs{
    position: absolute;
    top: 0;
    left: 0;
}

.center{
    flex: auto;
    display: flex;
    justify-content: center;
    }
</style>