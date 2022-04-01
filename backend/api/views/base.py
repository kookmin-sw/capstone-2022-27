from .api import res, api, P

@api(
    name="테스트 API",
    method='GET',
    params=[
        P('name', t='string'),
    ],
    errors={
        0: "Hello, {name}",
        1: '알 수 없는 에러',
    }
)
def test(req, name:str):
    return res(f'Hello, {name}!')
