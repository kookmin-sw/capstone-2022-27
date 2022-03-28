import axios from 'axios'

const BASEURL = import.meta.env.VITE_API_URL

const test = async (name) => {
    await (new Promise(res=>setTimeout(res, 1000)))
    const res = await axios.get(BASEURL+'/api/test', {params: {name: name}})
    return res.data.content
}

export {
    test
}