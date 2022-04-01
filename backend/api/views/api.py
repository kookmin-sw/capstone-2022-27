from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from rest_framework.decorators import api_view, parser_classes
from rest_framework.parsers import FormParser, JSONParser, MultiPartParser, FileUploadParser
from django.views.decorators.csrf import csrf_exempt
import json

from rest_framework.response import Response

class P:
    name: str
    desc: str
    t: str
    required: bool
    def __init__(self, name='', t='string', desc='', required=True):
        self.name=name
        self.desc=desc
        self.t=t
        self.required=required

def api(name='', desc='', method='GET', params=[], response=None, errors=dict()):
    '''
    문서화 + 파라미터 자동 파싱
    '''
    params_real = []
    for p in params:
        if type(p) is str:
            p = P(p)
        params_real.append(openapi.Parameter(
            p.name,
            openapi.IN_PATH if method == 'GET' else openapi.IN_FORM,
            type=p.t,
            description=p.desc,
            required=p.required,
        ))
    responses_real = {
        k: v for k, v in errors.items() 
    }
    responses_real[0] = openapi.Response('정상', response)
    def decorated(func):
        @swagger_auto_schema(
            operation_summary=name,
            operation_description=desc,
            method=method,
            manual_parameters=params_real,
            responses=responses_real,
        )
        @api_view([method])
        @parser_classes((FormParser,))
        @csrf_exempt
        def wrapper(req, *args, **kwargs):
            try:
                body = json.loads(req.body)
            except:
                body = dict()
            for param in params_real:
                if param.in_ == openapi.IN_QUERY:
                    kwargs[param.name] = req.query_params.get(param.name, None)
                elif param.in_ == openapi.IN_PATH:
                    pass # kwargs[param.name] = req.path_params.get(param.name, None)
                elif param.in_ == openapi.IN_BODY or param.in_ == openapi.IN_FORM:
                    param.in_ = openapi.IN_FORM
                    kwargs[param.name] = body[param.name] if param.name in body else req.POST[param.name]
                elif param.in_ == openapi.IN_HEADER:
                    kwargs[param.name] = req.headers.get(param.name, None)
            return func(req, *args, **kwargs)
        return wrapper
    return decorated

def res(data=None, code=0, msg='알 수 없는 에러', to_json=False):
    if code == 0:
        msg = '성공'
    
    res = {
        'status': {
            'code': code,
            'msg': msg,
        },
        'content': data
    }
    return json.dumps(res, ensure_ascii=False) if to_json else Response(res)