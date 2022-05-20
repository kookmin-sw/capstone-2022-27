<script>
import { text } from "svelte/internal";


    export let starColor=''
    export let textColor=''
    export let img=''
</script>

<div class="container">
    <div class="img" style="background-image: url('{img}');">
        <div class="star">
            <svg width="52" height="52" viewBox="0 0 52 52" fill="none" xmlns="http://www.w3.org/2000/svg">
                <path d="M26 0L29.506 3.86393L34.0344 1.27253L36.1748 6.03076L41.2824 4.96556L41.8477 10.1523L47.0344 10.7176L45.9692 15.8252L50.7275 17.9656L48.1361 22.494L52 26L48.1361 29.506L50.7275 34.0344L45.9692 36.1748L47.0344 41.2824L41.8477 41.8477L41.2824 47.0344L36.1748 45.9692L34.0344 50.7275L29.506 48.1361L26 52L22.494 48.1361L17.9656 50.7275L15.8252 45.9692L10.7176 47.0344L10.1523 41.8477L4.96556 41.2824L6.03076 36.1748L1.27253 34.0344L3.86393 29.506L0 26L3.86393 22.494L1.27253 17.9656L6.03076 15.8252L4.96556 10.7176L10.1523 10.1523L10.7176 4.96556L15.8252 6.03076L17.9656 1.27253L22.494 3.86393L26 0Z" fill="{starColor}"/>
            </svg>
            <div class='picktext centered' style='color:{textColor}'>Pick!</div>
        </div>
    </div>
</div>
<style>
.container{
    position: relative;
    /* justify-content: center;
    align-items: center;
    display: flex; */
}
.img {
    display: inline-block;
    background-size: cover;
    width: 10rem;
    height: 15rem;

    border-radius: 0 10px 10px 0;
    filter: drop-shadow(5px 3px 5px rgba(27, 29, 31, 0.15));
}
.star{
    position: absolute;
    /* display: flex; */
    right:-1.2rem;
    top: -1.2rem;
    filter: drop-shadow(0px 1px 1px rgba(27, 29, 31, 0.2));
    /* margin-top:auto; margin-bottom:auto;
    margin-top:auto; margin-bottom:auto;
    text-align: center; */
}
.picktext{
    position: absolute;
    top: 0;
    font-family: 'Roc Grotesk';
    font-style: normal;
    font-weight: 900;
    font-size: 0.75rem;
    line-height: 2rem;
}
.centered {
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
}
</style>