from .api import res, api, P
from .core import get_data, post_data
from django.db.models import F, Count, Q, Value, IntegerField
from django.forms.models import model_to_dict
from ..models import Book, User, Review, Keyword, Banner
from ..serializer import BookSerializer, BookSimpleSerializer, BookDetailSerializer, ReviewSerializer, SimpleSerializer, MainSerializer, BookLineSerializer, SearchSerializer, BannerSerializer
from .rand_nick import gen
import random
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
    
    try:
        user = User.objects.get(id=token['id'])
    except:
        return res(code=2, msg='토큰 에러')
    
    core_res = get_data(f'gnn/booktobooks/{book.id}')[:10]
    similar_books = [Book.objects.get(id=book_id) for book_id, score in core_res]
            
    reviews = []
    all_reviews = Review.objects.filter(book=book, content__isnull=False).exclude(content__exact='')
    for review in all_reviews.order_by('-created_at')[:3]:
        reviews.append({
            'user_name': review.user.nickname if review.user.booka else gen(review.user.id),
            'read_state': review.read_state,
            'score': review.score,
            'created_at': review.created_at,
            'content': review.content,
        })
    
    try:
        my_review = Review.objects.filter(book=book, user=user).order_by('-created_at')[0]
        my_review = ReviewSerializer({
                'user_name': review.user.nickname if review.user.booka else gen(review.user.id),
                'read_state': my_review.read_state,
                'score': my_review.score,
                'created_at': my_review.created_at,
                'content': my_review.content,
            }).data
    except Exception as e:
        print(e)
        my_review = None
    data = {
        'book': BookSerializer(book).data,
        'similar': BookSimpleSerializer(similar_books, many=True).data,
        'reviews': ReviewSerializer(reviews, many=True).data,
        'my_review': my_review,
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
            'user_name': review.user.username if review.user.booka else gen(review.user.id),
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
    books = [book for book in books_queryset.order_by('-num_review')[page*10:(page+1)*10]]
    
    data = SearchSerializer({
        'books': BookSimpleSerializer(books, many=True).data,
        'count': books_queryset.count(),
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
    books_queryset = Book.objects.filter(Q(title__icontains=keyword)).annotate(type=Value(0, output_field=IntegerField())) | Book.objects.filter(Q(author__icontains=keyword)).annotate(type=Value(1, output_field=IntegerField()))
    books = [book for book in books_queryset.order_by('type', '-num_review')[page*10:(page+1)*10]]
    
    data = SearchSerializer({
        'books': BookSimpleSerializer(books, many=True).data,
        'count': books_queryset.count(),
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
        if len(selected_books) == 0:
            as_a = 61367
        else:
            as_a = post_data(f'cossim/makeasa/{token["id"]}', selected_books)
        user.as_a = as_a
        user.save()
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
        data = BookSimpleSerializer(Book.objects.order_by('-num_review')[:100], many=True).data
        return res(data)
    except:
        return res(code=1, msg='알 수 없는 에러')

@api(
    name="추천 책",
    method='GET',
    params=[
        P('recom_type', t='integer', desc='추천 종류')
    ],
    response=BookSimpleSerializer(many=True),
    errors={
        1: '알 수 없는 에러'
    },
    auth=True
)
def recommend(req, recom_type, token):
    try:
        user = User.objects.get(id=token['id'])
        core_id = user.as_a if user.as_a else user.id
    except:
        return res(code=2, msg='토큰 에러')
    try:
        read_books = set(Review.objects.filter(user=user, read_state='읽었어요').prefetch_related('book').values_list('book', flat=True))
        def read_id_filter(books):
            return list(filter(lambda x: x[0] not in read_books, books))
        def read_filter(books):
            return list(filter(lambda x: x['id'] not in read_books, books))
        
        if recom_type == 0:
            books = [BookSimpleSerializer(Book.objects.get(id=book_id)).data for book_id, score in read_id_filter(get_data(f'gnn/usertobooks/{core_id}/0.0'))[:30]]
            random.shuffle(books)
            line = BookLineSerializer({
                'title': 'BOOKA BEST 추천',
                'books': books[:20]
            }).data
            return res(line)
        elif recom_type == 1:
            line_similar_users = get_data(f'gnn/usertousers/{core_id}')
            users_set = set(map(lambda x: x[0], line_similar_users))
            books = list(set([book.book for book in Review.objects.filter(Q(user__in=users_set)).select_related('book').order_by('-book__num_review')[:30]]))
            random.shuffle(books)
            books = books[:20]
            line = BookLineSerializer({
                'title': '비슷한 사람이 읽은 책',
                'books': read_filter(BookSimpleSerializer(books, many=True).data)
            }).data
            return res(line)
        elif recom_type == 2:
            book = Review.objects.filter(user=user).order_by('?')[:1].select_related('book').get().book
            books = get_data(f'gnn/booktobooks/{book.id}')[:30]
            random.shuffle(books)
            books = [Book.objects.get(id=book_id) for book_id, score in books]
            line = BookLineSerializer({
                'title': f'{book.title}: 이 책과 비슷한 책',
                'books': read_filter(BookSimpleSerializer(books[:20], many=True).data)
            }).data
            return res(line)
        elif recom_type == 3:
            books = [BookSimpleSerializer(Book.objects.get(id=book_id)).data for book_id, score in read_id_filter(get_data(f'gnn/usertobooks/{core_id}/1.0'))[:40]]
            # random.shuffle(books)
            line = BookLineSerializer({
                'title': '당신만을 위한 추천 도서',
                'books': books[:40]
            }).data
            return res(line)
        elif recom_type == 4:
            book = Review.objects.filter(user=user).order_by('?')[:1].select_related('book').get().book
            keyword = book.keywords.all()[0]
            
            line = BookLineSerializer({
                'title': f' #{keyword}',
                'books': read_filter(BookSimpleSerializer(Book.objects.filter(keywords__keyword=keyword).order_by('-num_review')[:30], many=True).data)
            }).data
            return res(line)
        elif recom_type == 5: # 키워드 붙는 애들
            # 장르: 장르 설명
            mapping = {
                '판타지': '상상 속 세상',
                '스타트업': '이제 막 창업하려는 당신에게',
                '추리소설': '진실은 언제나 하나',
                '여행': '떠나볼까요?',
                '로맨스': '두근거림이 필요할 때',
                '문학상': '믿고 읽는',
                '소프트웨어': '세상을 바꾸는',
            }
            keyword = random.choice(list(mapping.keys()))
            msg = mapping[keyword]
            print(keyword, msg)
            line = BookLineSerializer({
                'title': f'{msg} #{keyword}',
                'books': read_filter(BookSimpleSerializer(Book.objects.filter(keywords__keyword=keyword).order_by('-num_review')[:30], many=True).data)
            }).data
            return res(line)
        elif recom_type == 6: # 키워드 안붙는 애들
            # 장르: 장르 설명
            mapping = {
                '장편소설': '밤에 읽기 좋은 소설',
                '고양이': '이것도 읽어보라냥!',
                '과학': '세상을 밝히는 힘, 과학',
                '애니메이션': '영상의 감동을 글로 느껴보세요',
                '실리콘밸리': '실리콘밸리에 가고 싶은 당신에게',
                '우울': '나를 돌보는 법을 잊어버린 당신에게',
            }
            keyword = random.choice(list(mapping.keys()))
            msg = mapping[keyword]
            print(keyword, msg)
            line = BookLineSerializer({
                'title': f'{msg}',
                'books': read_filter(BookSimpleSerializer(Book.objects.filter(keywords__keyword=keyword).order_by('-num_review')[:30], many=True).data)
            }).data
            return res(line)
        return res(code=4, msg='알 수 없는 추천 종류')
    except Exception as e:
        print(e)
        return res(BookLineSerializer({
                'title': '',
                'books': []
            }).data)

@api(
    name="리뷰 작성",
    method='POST',
    params=[
        P('book_id', t='integer', desc='책 id'),
        P('state', t='string', desc='읽은 상태'),
        P('score', t='integer', desc='별점(1~10)'),
        P('content', t='string', desc='리뷰 내용'),
    ],
    response=BookSimpleSerializer(many=True),
    errors={
        1: '알 수 없는 에러'
    },
    auth=True
)
def review(req, book_id, state, content, score, token):
    print(book_id, state, content, score, token)
    try:
        user = User.objects.get(id=token['id'])
    except:
        return res(code=2, msg='토큰 에러')
    try:
        book = Book.objects.get(id=book_id)
        try:
            my_review = Review.objects.get(book=book, user=user)
        except:
            my_review = None
        if my_review:
            if state == '':
                my_review.delete()
            else: 
                my_review.read_state = state
                my_review.content = content if state == '읽었어요' else ''
                my_review.score = score if state == '읽었어요' else 0
                my_review.save()
        else:
            if len(content):
                Review(book=book, user=user, read_state=state, score=score, content=content).save()
            else:
                Review(book=book, user=user, read_state=state, score=score).save()
        return res()
    except Exception as e:
        print(e)
        return res(code=1, msg='알 수 없는 에러')
    
@api(
    name="배너",
    method='GET',
    params=[],
    response=BookSimpleSerializer(many=True),
    errors={
        1: '알 수 없는 에러'
    }
)
def banners(req):
    try:
        banners = [{
            'keywords': [banner.keywords.split()],
            'color1': banner.color1,
            'color2': banner.color2,
            'content': banner.content,
            'order': banner.order,
            'book': BookSimpleSerializer(banner.book).data
        } for banner in Banner.objects.all()]
        banners.sort(key=lambda x: x['order'])
        return res(banners)
    except Exception as e:
        print(e)
        return res(code=1, msg='알 수 없는 에러')