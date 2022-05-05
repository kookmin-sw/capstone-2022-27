import pickle as pkl
from time import time
import numpy as np

class LatentFactor:
    users = []
    books = []
    
    @classmethod
    def init(cls):
        t1 = time()
        t2 = time()
        t = t2 - t1
        print(f'Latent factor computated in {t} seconds.')
    
    @classmethod
    def update(cls):
        pass

    @classmethod
    def user_to_books(used_idx, book_idx, rating):
        pass