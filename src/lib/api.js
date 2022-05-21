import axios from 'axios'
import { identity } from 'svelte/internal'
import { stores_TOKEN } from './stores.js'
    
const BASEURL = import.meta.env.VITE_API_URL+"api/"
// const token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VybmFtZSI6Im5veWUxIiwiaWQiOjE0NzI2NDgzfQ.YHU6KxEIE1ndzBNdbP4-j7Rt4Uzf1QWgMZnDrwdvhtA"
const token = function() {
    return localStorage.getItem("token")
}

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
            // console.log(res.data.content)
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
    return safe_return(axios.get(`${BASEURL}book/detail/${idx}`,{ headers: { TOKEN: token(),}, withCredentials: true}))
}

const bookSearch = async (keyword, page) => {
    return safe_return(axios.get(`${BASEURL}book/search/${encodeURI(keyword)}/${page}`))
}

const bookSearchKeywords = async (keywords, page) => {
    return safe_return(axios.get(`${BASEURL}book/search_keyword/${encodeURI(keywords)}/${page}`))
}

const myReviews = async () => {
    return safe_return(axios.get(`${BASEURL}user/reviews`, { headers: { TOKEN: token()}, withCredentials: true}))
}

const mainpage = async (recom_type) => {
    return safe_return(axios.get(`${BASEURL}book/recommend/${recom_type}`, { headers: { TOKEN: token()}, withCredentials: true}))
}

const writeReview = async (book_id, state, score, content) => {
    return safe_return(axios.post(`${BASEURL}book/review/`, 
    {
        book_id : book_id,
        state : state,
        score : score,
        content: content,
    },
    { 
        headers: { TOKEN: token()},
        withCredentials: true,
    }
    ))
}

const getReviewPage = async (book_id, page) => {
    return safe_return(axios.get(`${BASEURL}book/review_pages/${book_id}/${page}`, 
    { 
        headers: { TOKEN: token()},
        withCredentials: true,
    }
    ))
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
    return safe_return(axios.post(`${BASEURL}book/firstpage`, 
    {
        selected_books : selected_books,
        TOKEN : token(),
     },
     { headers: { TOKEN: token(),}, withCredentials: true}))
}

const getBanners = async () => {
    return safe_return(axios.get(`${BASEURL}book/banners`, 
     { headers: { TOKEN: token(),}, withCredentials: true}))
}


const mainBannerMockup = async () => {
    const banners = [
        {
            id: 204346,
            image: 'https://bookthumb-phinf.pstatic.net/cover/164/054/16405427.jpg',
            title: '불편한 편의점',
            author: '김호연',
            publisher: '나무옆의자',
            intro: '설명 별로 안긴거',
            desc: '어젯밤 어떤 꿈을 꾸셨나요?<br> 오늘 밤 꿈은<br>달러구트 꿈 백화점에서<br>골라보세요.',
            keywords: ['장편소설', '즐거움', '기쁨'],
            bgColor: '#213355',
            pointColor:'#37DBFF',
            textColor:'#FFFFFF',
        },
        {
            id: 826,
            image: 'https://bookthumb-phinf.pstatic.net/cover/072/622/07262295.jpg',
            title: '살인자의 기억법',
            author: '김호연',
            publisher: '나무옆의자',
            intro: '설명 별로 안긴거',
            desc: '치매에 걸린 연쇄살인범의 이야기<br>네 기억은 믿지 마라<br>그 놈은 살인자다!',
            keywords: ['살인', '치매', '살인자',],
            bgColor: '#26282B',
            pointColor:'#DD2200',
            textColor:'#FFFFFF',
        },
        {
            id: 826,
            image: 'http://bookthumb.phinf.naver.net/cover/090/537/09053751.jpg',
            title: '오베라는 남자',
            author: '김호연',
            publisher: '나무옆의자',
            intro: '설명 별로 안긴거',
            desc: '인생 최악의 순간<br>최고의<br>이웃을 만났다!<br>',
            keywords: ['블로거', '아이슬란드', '빈자리','자전거'],
            bgColor: '#E9EBED',
            pointColor:'#FF68CC',
            textColor:'#1B1D1F',
        },
        {
            id: 204346,
            image: 'https://bookthumb-phinf.pstatic.net/cover/164/054/16405427.jpg',
            title: '불편한 편의점',
            author: '김호연',
            publisher: '나무옆의자',
            intro: '설명 별로 안긴거',
            desc: '어젯밤 어떤 꿈을 꾸셨나요?<br> 오늘 밤 꿈은<br>달러구트 꿈 백화점에서<br>골라보세요.',
            keywords: ['장편소설', '즐거움', '기쁨'],
            bgColor: '#213355',
            pointColor:'#37DBFF',
            textColor:'#FFFFFF',
        },
        {
            id: 826,
            image: 'https://bookthumb-phinf.pstatic.net/cover/072/622/07262295.jpg',
            title: '살인자의 기억법',
            author: '김호연',
            publisher: '나무옆의자',
            intro: '설명 별로 안긴거',
            desc: '치매에 걸린 연쇄살인범의 이야기<br>네 기억은 믿지 마라<br>그 놈은 살인자다!',
            keywords: ['살인', '치매', '살인자',],
            bgColor: '#26282B',
            pointColor:'#DD2200',
            textColor:'#FFFFFF',
        },
        {
            id: 826,
            image: 'http://bookthumb.phinf.naver.net/cover/090/537/09053751.jpg',
            title: '오베라는 남자',
            author: '김호연',
            publisher: '나무옆의자',
            intro: '설명 별로 안긴거',
            desc: '인생 최악의 순간<br>최고의<br>이웃을 만났다!<br>',
            keywords: ['블로거', '아이슬란드', '빈자리','자전거'],
            bgColor: '#E9EBED',
            pointColor:'#FF68CC',
            textColor:'#1B1D1F',
        },
    ]
    return banners
}

const profileMockup = async () => {
    const profile = {
        userId:0,
        profileImg:"https://cdn-icons.flaticon.com/png/512/3177/premium/3177440.png?token()=exp=1648532054~hmac=e1e0e0aa4e891febcd2cf65054766972",
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
    writeReview,getReviewPage,getBanners,
    myReviews
}