<script>

export let image
export let title
export let author


</script>

<div class="book_small">
    <div class="image-wrap"><div class="image" style="background-image: url('{image}');"></div></div>
    <div class="title">{title}</div>
    <div class="author">{author}</div>
</div>

<style>

.book_small {
    display: flex;
    flex-direction: column;
    align-items: left;
    justify-content: center;
}

.image-wrap {
    width: 6rem;
    height: 9rem;
    position: relative;
}
.image {
    position: absolute;
    top: 0;
    display: inline-block;
    background-size: cover;
    width: 6rem;
    height: 9rem;
    border-radius: 0 10px 10px 0;
    filter: drop-shadow(0px 2px 3px rgba(27, 29, 31, 0.3));
    transition: 0.2s ease-in-out;
    z-index: 99999999999999999999;
}
.image:hover {
    width: 6.6rem;
    height: 9.9rem;
    transform: translate(-0.3rem, -0.45rem);
}

.title {
    width: 6rem;
    font-size: 0.825rem;
    text-align: center;
    color: #1B1D1F;
    font-weight: 600;
    margin-top: 0.75rem;
    text-align: left;
    word-break: keep-all;
}

.author{
    font-size: 0.825rem;
    text-align: left;
    color: #72787F;
    width: 6rem;
    font-weight: 400;
    margin-top:0.25rem;
    text-overflow: ellipsis;
    white-space: nowrap;
    overflow: hidden;
}

</style>