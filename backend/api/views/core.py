import requests
import ast

def get_data(url):
    res = requests.get(f'http://127.0.0.1:3009/{url}')
    if len(res.text) == 0 or res.status_code != 200:
        return None
    return ast.literal_eval(res.text)