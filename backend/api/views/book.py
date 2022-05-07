from .api import res, api, P
from .core import get_data, post_data
from django.db.models import F, Count, Q
from ..models import Book, User, Review, Keyword
from ..serializer import BookSerializer, BookSimpleSerializer, BookDetailSerializer, ReviewSerializer, SimpleSerializer, MainSerializer, BookLineSerializer
import json

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
    response=BookSimpleSerializer(many=True),
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
    response=BookSimpleSerializer(many=True),
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

@api(
    name="첫 페이지 (취향 찾기)",
    method='POST',
    params=[
        P('selected_books', t='list', desc='선택한 책의 목록'),
    ],
    response=SimpleSerializer,
    errors={
        1: '알 수 없는 에러',
        2: '계정 관련 에러'
    },
    auth=True
)
def firstpage(req, selected_books, token):
    try:
        user = User.objects.get(id=token['id'])
    except:
        return res(code=2, msg='토큰 에러')
    try:   
        selected_books = json.loads(selected_books)
        post_data(f'cossim/makeasa/{token["id"]}', selected_books)
        for book_id in selected_books:
            Review(user=user, book=Book.objects.get(id=book_id), read_state='읽었어요', score=10).save()
        
        return res(msg='성공')
    except:
        return res(code=1, msg='알 수 없는 에러')

@api(
    name="첫 페이지 (취향 찾기) 책 목록",
    method='GET',
    params=[],
    response=BookSimpleSerializer(many=True),
    errors={
        1: '알 수 없는 에러'
    }
)
def firstpage_list(req):
    try:
        books = [BookSimpleSerializer(book).data for book in Book.objects.annotate(num_reviews=Count('reviews')).order_by('-num_reviews')[:50].values('id', 'image', 'title', 'isbn', 'author', 'publisher', 'pubdate')]
        return res(books)
    except:
        return res(code=1, msg='알 수 없는 에러')


@api(
    name="메인페이지",
    method='GET',
    params=[],
    response=MainSerializer,
    errors={
        1: '알 수 없는 에러',
        2: '계정 관련 에러'
    },
    auth=True
)
def mainpage(req, token):
    try:
        user = User.objects.get(id=token['id'])
    except:
        return res(code=2, msg='토큰 에러')
    try:
        
        line_general = {
            'title': '그냥 젤 많이 읽을만한 거',
            'desc': '에이 이거는 추천 잘 되겠지',
            'books': [BookSerializer(Book.objects.get(id=book_id)).data for book_id, score in get_data(f'gnn/usertobooks/{token["id"]}')[:30]]
        }
        line_general_s = BookLineSerializer(data=line_general)
        if not line_general_s.is_valid():
            print(line_general_s.errors)
            return res(code=3)
        
        line_similar_users = get_data(f'gnn/usertousers/{token["id"]}')
        users_set = set(map(lambda x: x[0], line_similar_users))
        print(users_set)
        books = Review.objects.filter(user__in=users_set).values('book').distinct().annotate(num_reviews=Count('book')).order_by('-num_reviews')[:30]
        books = [BookSerializer(Book.objects.get(id=book['book'])).data for book in books]
        line_similar_read = {
            'title': '비슷한 사람이 읽은 책',
            'desc': '그렇습니다',
            'books': books
        }
        line_similar_read_s = BookLineSerializer(data=line_similar_read)
        if not line_similar_read_s.is_valid():
            print(line_similar_read_s.errors)
            return res(code=3)
        
        data_s = MainSerializer(data={
            'banner': [],
            'lines': [line_general_s.data, line_similar_read_s.data]
        })
        
        if not data_s.is_valid():
            print(data_s.errors)
            return res(code=3)
        
        return res(data_s.data)
    except Exception as e:
        print(e)
        return res(code=1)