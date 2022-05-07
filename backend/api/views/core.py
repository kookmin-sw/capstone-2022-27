import requests
import ast

def get_data(url):
    res = requests.get(f'http://127.0.0.1:3009/{url}')
    if len(res.text) == 0 or res.status_code != 200:
        return None
    return ast.literal_eval(res.text)

def post_data(url, data):
    res = requests.post(f'http://127.0.0.1:3009/{url}', json=data)
    if len(res.text) == 0 or res.status_code != 200:
        return None
    return ast.literal_eval(res.text)

if __name__ == '__main__':
    print(post_data('cossim/make_as_a/12345', [123, 456]))