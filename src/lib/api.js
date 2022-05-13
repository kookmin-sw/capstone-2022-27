import axios from 'axios'
import { identity } from 'svelte/internal'
import { stores_TOKEN } from './stores.js'

const BASEURL = import.meta.env.VITE_API_URL+"api/"
// const token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VybmFtZSI6Im5veWUxIiwiaWQiOjE0NzI2NDgzfQ.YHU6KxEIE1ndzBNdbP4-j7Rt4Uzf1QWgMZnDrwdvhtA"
let token = ""
stores_TOKEN.subscribe(value => {
    token = value;
});

const safe_return = async (promise) => {
    let res;
    try {
        res = await promise
    } catch (e) {
        console.error(e)
        throw {
            code: -2,
            msg: '요청 실패'
        }
    }
    if (res.status === 200) {
        if (res.data.status.code == 0) {
            console.log(res.data.content)
            return res.data.content
        } else {
            throw {
                code: res.data.status.code,
                msg: res.data.status.msg
            }
        }
    }
}

const api = async (url, params) => {
    const promise = axios.get(`${BASEURL}/api/${url}`, {params: params})
    return safe_return(promise)
    // return promise
}

const test = async (name) => {
    await (new Promise(res=>setTimeout(res, 1000)))
    return api('test', {name: name})
}
const booksMockup = async() =>{
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

const recomsMockup = async () => {
    const recoms =
        [
            {
                recommand: "20대가 좋아하는 책",
                keywords: [],
                books: [
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
            },
            {
                recommand: "",
                keywords: ['유령', '공포'],
                books: [
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
                ]
            },
        ]
    return recoms;
}

const bookDetail = async (idx) => {
    return safe_return(axios.get(`${BASEURL}book/detail/${idx}`,{ headers: { TOKEN: token,}, withCredentials: true}))
}

const bookSearch = async (keyword, page) => {
    return safe_return(axios.get(`${BASEURL}book/search/${keyword}/${page}`))
}

const bookSearchKeywords = async (keywords, page) => {
    return safe_return(axios.get(`${BASEURL}book/search_keyword/${keywords}/${page}`))
}

const mainpage = async () => {
    return safe_return(axios.get(`${BASEURL}book/mainpage/`, { headers: { TOKEN: token}, withCredentials: true}))
}

const login = async (username, password ) => {
    return safe_return(axios.post(`${BASEURL}user/login/`, 
    {
        username : username,
        password : password
     }))
}

const register = async (username,nickname, password ) => {
    return safe_return(axios.post(`${BASEURL}user/register/`, 
    {
        username : username,
        nickname : nickname,
        password : password,
     }))
}

const getFristPageList = async () => {
    return safe_return(axios.get(`${BASEURL}book/firstpage_list/`, ))
}
const setFristPageList = async (selected_books) => {
    return safe_return(axios.post(`${BASEURL}book/firstpage/`, 
    {
        selected_books : selected_books,
        TOKEN : token,
     },
     { headers: { TOKEN: token,}, withCredentials: true}))
}


const mainBannerMockup = async () => {
    const book = {
            id: 0,
            image: 'https://image.aladin.co.kr/product/29045/74/cover500/k192836746_2.jpg',
            title: '불편한 편의점',
            author: '김호연',
            publisher: '나무옆의자',
            intro: '설명 별로 안긴거',
            desc: '설명 완전 긴거 블라블ㄹ라 <br> sfsdkfasfs<br>dsfadsfdsfsd <br> 최고의 책!\n',
            keyword: ['키워드1', '키워드2', '키워드3'],
            bgColor: '#A9D0F5'
        }
    return book
}

const profileMockup = async () => {
    const profile = {
        userId:0,
        profileImg:"https://cdn-icons.flaticon.com/png/512/3177/premium/3177440.png?token=exp=1648532054~hmac=e1e0e0aa4e891febcd2cf65054766972",
        username:"김유진",
        }
    return profile
}

export {
    api,
    test,
    booksMockup, bookDetail,
    mainBannerMockup,profileMockup,
    recomsMockup,
    bookSearchKeywords,
    bookSearch,
    mainpage,
    login,
    register,
    getFristPageList, setFristPageList,

}