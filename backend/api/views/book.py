from .api import res, api, P
from .core import get_data
from django.db.models import F, Count, Q
from ..models import Book, User, Review, Keyword
from ..serializer import BookSerializer, BookSimpleSerializer, BookDetailSerializer, ReviewSerializer

@api(
    name="책 상세",
    method='GET',
    params=[
        P('id', t='integer', desc='책의 id'),
    ],
    response=BookDetailSerializer,
    errors={
        1: '알 수 없는 에러',
    },
    auth=True
)
def detail(req, id:int, token):
    book = Book.objects.get(id=id)

    similar_books = []
    core_res = get_data(f'gnn/booktobooks/{book.id}')[:10]
    for book_id, score in core_res:
        similar_books.append(Book.objects.get(id=book_id))
    
    hope = False # 유저가 읽고싶은지 여부
    if token:
        user = User.objects.get(id=token['id'])
        if len(Review.objects.filter(user=user, book=book, read_state='읽고싶어요')) > 0:
            hope = True
            
    reviews = []
    for review in book.reviews.order_by('-created_at')[:15]:
        reviews.append({
            'user_name': review.user.username if review.user.booka else 'test',
            'read_state': review.read_state,
            'score': review.score,
            'created_at': review.created_at,
        })
    
    data = {
        'book': BookSerializer(book).data,
        'similar': BookSimpleSerializer(similar_books, many=True).data,
        'reviews': ReviewSerializer(reviews, many=True).data,
        'keywords': ['인기', '누구나'],
        'hope': hope,
    }
    data_s = BookDetailSerializer(data=data)
    data_s.book = book
    if not data_s.is_valid():
        print(data_s.errors)
        return res(code=2)
    return res(data_s.data)

@api(
    name="책 키워드 검색",
    method='GET',
    params=[
        P('keywords', t='string', desc='검색할 키워드, 쉼표로 구분'),
        P('page', t='integer', desc='검색 조회 페이지'),
    ],
    response=BookSimpleSerializer,
    errors={
        1: '알 수 없는 에러',
    },
)
def search_keyword(req, keywords:str, page:int):
    books = list(Book.objects.filter(tags__keyword__in=keywords.split(',')).annotate(num_reviews=Count('reviews')).order_by('-num_reviews')[page*10:(page+1)*10].values('id', 'image', 'title', 'isbn', 'author', 'publisher', 'pubdate'))
        
    data_s = BookSimpleSerializer(data=books, many=True)
    
    if not data_s.is_valid():
        print(data_s.errors)
        return res(code=2)
    return res(data_s.data)

@api(
    name="책 검색",
    method='GET',
    params=[
        P('keyword', t='string', desc='검색할 내용'),
        P('page', t='integer', desc='검색 조회 페이지'),
    ],
    response=BookSimpleSerializer,
    errors={
        1: '알 수 없는 에러',
    },
)
def search(req, keyword:str, page:int):
    books = list(Book.objects.filter(Q(title__icontains=keyword) | Q(author__icontains=keyword) | Q(desc__icontains=keyword)).annotate(num_reviews=Count('reviews')).order_by('-num_reviews')[page*10:(page+1)*10].values('id', 'image', 'title', 'isbn', 'author', 'publisher', 'pubdate'))
        
    data_s = BookSimpleSerializer(data=books, many=True)
    
    if not data_s.is_valid():
        print(data_s.errors)
        return res(code=2)
    return res(data_s.data)