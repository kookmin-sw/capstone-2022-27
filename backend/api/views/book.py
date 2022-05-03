from .api import res, api, P
from django.db.models import F, Count
from ..models import Book, User, Review
from ..serializer import BookSerializer, BookSimpleSerializer, BookDetailSerializer

@api(
    name="책 상세",
    method='GET',
    params=[
        P('id', t='integer', desc='책의 id'),
    ],
    response=BookDetailSerializer,
    errors={
        1: '알 수 없는 에러',
    }
)
def detail(req, id:int):
    book = Book.objects.get(id=id)

    data = {
        'book': BookSerializer(book).data,
        'similar': BookSimpleSerializer(random_books(), many=True).data,
        'keywords': ['인기', '누구나']
    }
    data_s = BookDetailSerializer(data=data)
    data_s.book = book
    if not data_s.is_valid():
        print(data_s.errors)
        return res(code=2)
    return res(data_s.data)
