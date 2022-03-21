<script>
import { test } from '../lib/api'

const init = test('noye')
</script>

<h1>Booka Gazua~~~</h1>
{#await init}
    <p>waiting..</p>
{:then res}
    <p>server: {res}</p>
{:catch error}
    <p>error: {error.message}</p>
{/await}