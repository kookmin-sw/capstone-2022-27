<script>

export let className

</script>

<div class="card {className}">
    <slot />
</div>

<style>

.card {
    background: #fff;
    border-radius: 5px;
    box-shadow: 0px 5px 12px 0px rgba(0, 0, 0, 0.11);
    padding: 1rem;
    margin: 1rem;
}

</style>