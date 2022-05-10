from .api import res, api, P
from .core import get_data, post_data
from django.db.models import F, Count, Q, Value, IntegerField
from django.forms.models import model_to_dict
from ..models import Book, User, Review, Keyword
from ..serializer import BookSerializer, BookSimpleSerializer, BookDetailSerializer, ReviewSerializer, SimpleSerializer, MainSerializer, BookLineSerializer, SearchSerializer
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
    
    core_res = get_data(f'gnn/booktobooks/{book.id}')[:10]
    similar_books = [Book.objects.get(id=book_id) for book_id, score in core_res]
    
    hope = False # 유저가 읽고싶은지 여부
    if token:
        user = User.objects.get(id=token['id'])
        if len(Review.objects.filter(user=user, book=book, read_state='읽고싶어요')) > 0:
            hope = True
            
    reviews = []
    all_reviews = Review.objects.filter(book=book, content__isnull=False).exclude(content__exact='')
    for review in all_reviews.order_by('-created_at')[:3]:
        reviews.append({
            'user_name': review.user.username if review.user.booka else 'test',
            'read_state': review.read_state,
            'score': review.score,
            'created_at': review.created_at,
            'content': review.content,
        })
    
    data = {
        'book': BookSerializer(book).data,
        'similar': BookSimpleSerializer(similar_books, many=True).data,
        'reviews': ReviewSerializer(reviews, many=True).data,
        'num_reviews': all_reviews.count(),
        'hope': hope,
    }
    
    return res(data)

@api(
    name="리뷰 페이지",
    method='GET',
    params=[
        P('id', t='integer', desc='책의 id'),
        P('page', t='integer', desc='페이지 번호'),
    ],
    response=ReviewSerializer(many=True),
    errors={
        1: '알 수 없는 에러',
    }
)
def review_pages(req, id:int, page):
    book = Book.objects.get(id=id)            
    reviews = []
    all_reviews = Review.objects.filter(book=book, content__isnull=False).exclude(content__exact='')
    for review in all_reviews.order_by('-created_at')[page*3:(page+1)*3]:
        reviews.append({
            'user_name': review.user.username if review.user.booka else 'test',
            'read_state': review.read_state,
            'score': review.score,
            'created_at': review.created_at,
            'content': review.content,
        })

    return res(ReviewSerializer(reviews, many=True).data)

@api(
    name="책 키워드 검색",
    method='GET',
    params=[
        P('keyword', t='string', desc='검색할 키워드'),
        P('page', t='integer', desc='검색 조회 페이지'),
    ],
    response=SearchSerializer,
    errors={
        1: '알 수 없는 에러',
    },
)
def search_keyword(req, keyword:str, page:int):
    books_queryset = Book.objects.filter(keywords__keyword=keyword)
    books = [book for book in books_queryset.annotate(num_reviews=Count('reviews')).order_by('-num_reviews')[page*10:(page+1)*10]]
    
    data = SearchSerializer({
        'books': BookSimpleSerializer(books, many=True).data,
        'count': len(books_queryset),
    }).data
    
    return res(data)

@api(
    name="책 검색",
    method='GET',
    params=[
        P('keyword', t='string', desc='검색할 내용'),
        P('page', t='integer', desc='검색 조회 페이지'),
    ],
    response=SearchSerializer,
    errors={
        1: '알 수 없는 에러',
    },
)
def search(req, keyword:str, page:int):
    books_queryset = Book.objects.filter(Q(title__icontains=keyword)).annotate(type=Value(0, output_field=IntegerField())) | Book.objects.filter(Q(author__icontains=keyword)).annotate(type=Value(1, output_field=IntegerField()))| Book.objects.filter(Q(publisher__icontains=keyword)).annotate(type=Value(2, output_field=IntegerField()))
    books = [book for book in books_queryset.annotate(num_reviews=Count('reviews')).order_by('type', '-num_reviews')[page*10:(page+1)*10]]
    
    data = SearchSerializer({
        'books': BookSimpleSerializer(books, many=True).data,
        'count': len(books_queryset),
    }).data
    
    return res(data)

@api(
    name="첫 페이지 (취향 찾기)",
    method='POST',
    params=[
        P('selected_books', t='string', desc='선택한 책의 목록'),
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
        
        return res()
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
        data = BookSimpleSerializer(Book.objects.annotate(num_reviews=Count('reviews')).order_by('-num_reviews')[:50], many=True).data
        return res(data)
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
        
        line_general = BookLineSerializer({
            'title': '그냥 젤 많이 읽을만한 거',
            'desc': '에이 이거는 추천 잘 되겠지',
            'books': [BookSerializer(Book.objects.get(id=book_id)).data for book_id, score in get_data(f'gnn/usertobooks/{token["id"]}')[:30]]
        })
        
        line_similar_users = get_data(f'gnn/usertousers/{token["id"]}')
        users_set = set(map(lambda x: x[0], line_similar_users))
        books = Review.objects.filter(user__in=users_set).values('book').distinct().annotate(num_reviews=Count('book')).order_by('-num_reviews')[:30]
        line_similar_read = BookLineSerializer({
            'title': '비슷한 사람이 읽은 책',
            'desc': '그렇습니다',
            'books': [BookSerializer(Book.objects.get(id=book['book'])).data for book in books]
        })
        
        data = MainSerializer({
            'banner': [],
            'lines': [line_general.data, line_similar_read.data]
        }).data
        
        return res(data)
    except Exception as e:
        print(e)
        return res(code=1)