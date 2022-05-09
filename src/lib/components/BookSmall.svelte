<script>

export let image
export let title
export let author

</script>

<div class="book_small">
    <div class="image" style="background-image: url('{image}');"></div>
    <div class="title">{title}</div>
    <div class="author">{author}</div>
</div>

<style>

.book_small {
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
}

.image {
    display: inline-block;
    background-size: cover;
    width: 6rem;
    height: 9rem;
}

.title {
    font-size: 0.825rem;
    text-align: center;
    color: #1B1D1F;
    font-weight: 600;
    margin-top: 0.75rem;
}

.author{
    font-size: 0.825rem;
    text-align: center;
    color: #72787F;
    font-weight: 400;
    margin-top:0.25rem ;
}

</style>