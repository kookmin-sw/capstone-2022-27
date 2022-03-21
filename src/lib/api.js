import axios from 'axios'

const test = async (name) => {
    await (new Promise(res=>setTimeout(res, 1000)))
    const res = await axios.get('/api/test', {params: {name: name}})
    return res.data.content
}

export {
    test
}