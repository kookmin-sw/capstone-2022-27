import pickle as pkl
from time import time
import numpy as np

class Embeddings:
    users = []
    books = []
    pre_book_to_books = {}
    pre_book_to_books = {}
    
    @classmethod
    def precomputation(cls):
        user_to_books = {}
        for user_idx, user_ebd in cls.users:
            user_books = []
            for book_idx, book_ebd in cls.books:
                user_books.append((book_idx, np.dot(user_ebd, book_ebd)))
            user_to_books[user_idx] = sorted(user_books, key=lambda x: x[1], reverse=True)
        cls.pre_user_to_books = user_to_books
        
        book_to_books = {}
        for book1_idx, book1_ebd in cls.books:
            book_books = []
            for book2_idx, book2_ebd in cls.books:
                if book1_idx == book2_idx:
                    continue
                book_books.append((book2_idx, np.dot(book1_ebd, book2_ebd)))
            book_to_books[book1_ebd] = sorted(book_books, key=lambda x: x[1], reverse=True)
        cls.pre_book_to_books = book_to_books
    
    # 처음에만 호출할 필요 없음
    @classmethod
    def init(cls):
        t1 = time()
        cls.users = pkl.load(open('data/user_embeddings.pkl', 'rb'))
        cls.books = pkl.load(open('data/book_embeddings.pkl', 'rb'))
        t2 = time()
        t = t2 - t1
        print(f'Embeddings loaded in {t} seconds.')
        cls.precomputation()()
        t3 = time()
        t = t3 - t2
        print(f'Precomputation done in {t} seconds.')
        
    @classmethod
    def user_to_books(user_idx):
        return cls.user_to_books[user_idx]

    @classmethod
    def book_to_books(book_id):
        return cls.book_to_books[used_idx]