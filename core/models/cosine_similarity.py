import pickle as pkl
from time import time
import numpy as np

def make_record(records):
    res = dict()
    for rec in records:
        res[rec] = 5
    return res

def cosine_distance_sparse(record1, record2):
    score = 0
    norm1 = 0
    norm2 = 0
    for book, s in record1.items():
        norm1 += s*s
    for book, s in record2.items():
        norm2 += s*s
    for book, s1 in record1.items():
        if book in record2:
            s2 = record2[book]
            score += s1*s2
    if norm1 == 0 or norm2 == 0: return 0
    norm1 = norm1**.5
    norm2 = norm2**.5
    return score / (norm1 * norm2)

class CosineSimilarity:
    all_user = set()
    records = dict()
    
    @classmethod
    def init(cls):
        t1 = time()
        cls.all_user = pkl.load(open('data/user_1.pkl', 'rb'))
        cls.records:dict = pkl.load(open('data/user_3_records.pkl', 'rb'))
        t2 = time()
        t = t2 - t1
        print(f'Cossim ready in {t} seconds.')
    
    @classmethod
    def make_as_a(cls, user_idx, records):
        if user_idx in cls.records:
            return user_idx
        
        user_rec = make_record(records)
        
        max_similar = (-1, 0)
        for other_idx, other_rec in cls.records.items():
            sim = cosine_distance_sparse(user_rec, other_rec)
            if sim >= max_similar[1]:
                max_similar = (other_idx, sim)
        
        return max_similar[0]
    
    @classmethod
    def is_inner_user(cls, user_idx):
        return user_idx in cls.records

if __name__ == "__main__":
    pass