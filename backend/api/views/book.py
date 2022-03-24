from .api import res, api, P
from ..models import Book

@api(
    name="책 테스트 API",
    method='GET',
    params=[
        P('test', t='string', desc='아무 의미 없는 인자'),
    ],
    responses={
        0: "[Book, Book, Book...]",
        1: '알 수 없는 에러',
    }
)
def test(req, name:str):
    book = {
        
    }
    return res(f'Hello, {name}!')
