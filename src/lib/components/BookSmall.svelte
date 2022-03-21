<script>

export let image
export let title

</script>

<div class="book_small">
    <div class="image" style="background-image: url('{image}');"></div>
    <div class="title">{title}</div>
</div>

<style>

.book_small {
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    margin: .5rem 1rem;
}

.image {
    display: inline-block;
    background-size: cover;
    width: 6rem;
    height: 9rem;
    margin-bottom: 1rem;
    box-shadow: 0px 5px 12px 0px rgba(0, 0, 0, 0.14);
}

.title {
    font-size: 0.9rem;
    text-align: center;
    color: #444;
    font-weight: bold;
}

</style>