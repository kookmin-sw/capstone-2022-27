import axios from 'axios'

const BASEURL = import.meta.env.VITE_API_URL

const safe_return = async (promise) => {
    try {
        const res = await promise
        if (res.status === 200) {
            if (res.data.status.code == 0) {
                return res.data.content
            } else {
                throw new Error(res.data.status.msg)
            }
        }
    } catch (e) {
        throw new Error('서버와 통신 중 알 수 없는 에러가 발생했습니다.')
    }
}

const api = async (url, params) => {
    const promise = axios.get(`${BASEURL}/api/${url}`, {params: params})
    return safe_return(promise)
}

const test = async (name) => {
    await (new Promise(res=>setTimeout(res, 1000)))
    return api('test', {name: name})
}

const booksMockup = async () => {
    const books = [
        {
            id: 0,
            image: 'https://image.aladin.co.kr/product/29045/74/cover500/k192836746_2.jpg',
            title: '불편한 편의점',
            author: '김호연',
            publisher: '나무옆의자',
        },
        {
            id: 1,
            image: 'https://image.aladin.co.kr/product/29045/74/cover500/k192836746_2.jpg',
            title: '불편한 편의점',
            author: '김호연',
            publisher: '나무옆의자',
        },
        {
            id: 2,
            image: 'https://image.aladin.co.kr/product/29045/74/cover500/k192836746_2.jpg',
            title: '불편한 편의점',
            author: '김호연',
            publisher: '나무옆의자',
        },
        {
            id: 3,
            image: 'https://image.aladin.co.kr/product/29045/74/cover500/k192836746_2.jpg',
            title: '불편한 편의점',
            author: '김호연',
            publisher: '나무옆의자',
        },
        {
            id: 4,
            image: 'https://image.aladin.co.kr/product/29045/74/cover500/k192836746_2.jpg',
            title: '불편한 편의점',
            author: '김호연',
            publisher: '나무옆의자',
        }
    ]
    return books
}

const bookDetailMockup = async () => {
    const book = {
            id: 0,
            image: 'https://image.aladin.co.kr/product/29045/74/cover500/k192836746_2.jpg',
            title: '불편한 편의점',
            author: '김호연',
            publisher: '나무옆의자',
            intro: '설명 별로 안긴거',
            desc: '설명 완전 긴거',
            keyword: ['키워드1', '키워드2', '키워드3']
        }
    return book
}

export {
    api,
    test,
    booksMockup, bookDetailMockup
}