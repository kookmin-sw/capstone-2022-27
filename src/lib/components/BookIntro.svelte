<script>
export let title=""
export let content=""
</script>
<div>
    <div class='title'>{title}</div>
    <hr class='border'>
    <div class='content'>{content}</div>
</div>

<style>
.title{
    font-family: 'Pretendard';
    font-style: normal;
    font-weight: 700;
    font-size: 1rem;
    line-height: 1.25rem;
}
.border{
    border:solid 1px #26282B;
    margin-top: 1rem;
}
.content{
    margin-top: 1rem;
    font-family: 'Pretendard';
    font-style: normal;
    font-weight: 400;
    font-size: 0.938rem;
    line-height: 1.313rem;
    max-lines: 6;
}
</style>