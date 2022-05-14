import pickle as pkl
from time import time
import numpy as np
from tqdm import tqdm

def normalize(lst):
    res = []
    lst = list(lst)
    mean = np.mean(lst)
    std = np.std(lst)
    
    return [(item - mean) / std for item in lst]

class GNN:
    books_to_use = set()
    users_to_use = set()
    book_baseline = dict()
    all_users = []
    all_books = []
    users = []
    books = []
    pre_user_to_books = {}
    pre_book_to_books = {}
    pre_user_to_users = {}
    
    @classmethod
    def precomputation(cls):
        # user_to_books = {}
        # for user_idx, user_ebd in tqdm(cls.users):
        #     user_books = [0] * len(cls.books)
        #     for i, (book_idx, book_ebd) in enumerate(cls.books):
        #         user_books[i] = ((book_idx, np.dot(user_ebd, book_ebd)))
        #     user_to_books[user_idx] = user_books
        # cls.pre_user_to_books = user_to_books
        
        # book_to_books = {}
        # for book1_idx, book1_ebd in tqdm(cls.books):
        #     book_books = []
        #     for book2_idx, book2_ebd in cls.books:
        #         if book1_idx == book2_idx:
        #             continue
        #         book_books.append((book2_idx, np.dot(book1_ebd, book2_ebd)))
        #     book_to_books[book1_idx] = book_books
        # cls.pre_book_to_books = book_to_books
        pass
    
    # 처음에만 호출할 필요 없음
    @classmethod
    def init(cls):
        t1 = time()
        cls.users_to_use = list(pkl.load(open('data/user_1.pkl', 'rb')))
        cls.books_to_use = list(pkl.load(open('data/book_3.pkl', 'rb')))
        cls.book_baseline = pkl.load(open('data/baseline.pkl', 'rb'))
        
        # normalize book baseline
        cls.book_baseline = dict(zip(cls.book_baseline.keys(), normalize(cls.book_baseline.values())))
        
        cls.all_users = pkl.load(open('data/gnn_user.pkl', 'rb'))
        cls.all_books = pkl.load(open('data/gnn_book.pkl', 'rb'))
        cls.users = list(filter(lambda x: x[0] in cls.users_to_use, cls.all_users.items()))
        cls.books = list(filter(lambda x: x[0] in cls.books_to_use, cls.all_books.items()))
        t2 = time()
        t = t2 - t1
        print(f'Embeddings loaded in {t} seconds.')
        cls.precomputation()
        t3 = time()
        t = t3 - t2
        print(f'Precomputation done in {t} seconds.')
        
    @classmethod
    def user_to_books(cls, user_idx, alpha=0):
        if user_idx not in cls.all_users:
            return []
        if user_idx not in cls.pre_user_to_books:
            t1 = time()
            user_ebd = cls.all_users[user_idx]
            user_books = []
            for book_idx, book_ebd in cls.books:
                if user_idx == book_idx:
                    continue
                user_books.append((book_idx, np.dot(user_ebd, book_ebd)))
            cls.pre_user_to_books[user_idx] = sorted(user_books, key=lambda x: x[1], reverse=True)
            print(f'User {user_idx} computed in {time() - t1} seconds.')
        books = cls.pre_user_to_books[user_idx]
        
        # normalize books
        books = zip([book[0] for book in books], normalize([book[1] for book in books]))
        
        books = list(map(lambda x: (x[0], x[1] - (cls.book_baseline[x[0]] * alpha)), filter(lambda x: x[0] in cls.book_baseline, books)))
        return sorted(books, key=lambda x: x[1], reverse=True)

    @classmethod
    def book_to_books(cls, book_idx):
        if book_idx not in cls.all_books:
            return []
        if book_idx not in cls.pre_book_to_books:
            t1 = time()
            book_ebd = cls.all_books[book_idx]
            book_books = []
            for book2_idx, book2_ebd in cls.books:
                if book_idx == book2_idx:
                    continue
                book_books.append((book2_idx, np.dot(book_ebd, book2_ebd)))
            cls.pre_book_to_books[book_idx] = sorted(book_books, key=lambda x: x[1], reverse=True)
            print(f'Book {book_idx} computed in {time() - t1} seconds.')
        return cls.pre_book_to_books[book_idx]
    
    @classmethod
    def user_to_users(cls, user_idx):
        if user_idx not in cls.all_users:
            return []
        if user_idx not in cls.pre_user_to_users:
            t1 = time()
            user_ebd = cls.all_users[user_idx]
            user_users = []
            for user2_idx, user2_ebd in cls.users:
                if user_idx == user2_idx:
                    continue
                user_users.append((user2_idx, np.dot(user_ebd, user2_ebd)))
            cls.pre_user_to_users[user_idx] = sorted(user_users)
            print(f'UserToUser {user_idx} computed in {time() - t1} seconds.')
        return cls.pre_user_to_users[user_idx]