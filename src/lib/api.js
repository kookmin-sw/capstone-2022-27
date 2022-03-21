import axios from 'axios'

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
    const promise = axios.get(`/api/${url}`, {params: params})
    return safe_return(promise)
}

const test = async (name) => {
    await (new Promise(res=>setTimeout(res, 1000)))
    return api('test', {name: name})
}

const booksMockup = async () => {
    const books = [
        {
            image: 'https://image.aladin.co.kr/product/29045/74/cover500/k192836746_2.jpg',
            title: '불편한 편의점',
            author: '김호연',
            publisher: '나무옆의자',
        },
        {
            image: 'https://image.aladin.co.kr/product/29045/74/cover500/k192836746_2.jpg',
            title: '불편한 편의점',
            author: '김호연',
            publisher: '나무옆의자',
        },
        {
            image: 'https://image.aladin.co.kr/product/29045/74/cover500/k192836746_2.jpg',
            title: '불편한 편의점',
            author: '김호연',
            publisher: '나무옆의자',
        },
        {
            image: 'https://image.aladin.co.kr/product/29045/74/cover500/k192836746_2.jpg',
            title: '불편한 편의점',
            author: '김호연',
            publisher: '나무옆의자',
        },
        {
            image: 'https://image.aladin.co.kr/product/29045/74/cover500/k192836746_2.jpg',
            title: '불편한 편의점',
            author: '김호연',
            publisher: '나무옆의자',
        }
    ]
    return books
}

export {
    api,
    test,
    booksMockup
}