from flask import Flask, abort, request

import json

from models.gnn import GNN
from models.cosine_similarity import CosineSimilarity

app = Flask(__name__)

# 결과에 주어질 최대 개수
N_BOOK = 200
N_USER = 200

if __name__ == "__main__":
    GNN.init()
    CosineSimilarity().init()

@app.before_request
def whitelist():
    if request.remote_addr not in ['127.0.0.1']:
        abort(403)

@app.route('/gnn/usertobooks/<int:user_idx>')
def gnn_user_to_books(user_idx):
    return json.dumps(GNN.user_to_books(user_idx)[:N_BOOK])

@app.route('/gnn/booktobooks/<int:book_idx>')
def gnn_book_to_books(book_idx):
    return json.dumps(GNN.book_to_books(book_idx)[:N_BOOK])

@app.route('/gnn/usertousers/<int:user_idx>')
def gnn_user_to_users(user_idx):
    return json.dumps(GNN.user_to_users(user_idx)[:20])

@app.route('/gnn/reload')
def gnn_reload():
    GNN.init()

@app.route('/cossim/makeasa/<int:user_idx>', methods=['POST'])
def cossim_make_as_a(user_idx):
    records = request.json
    return str(CosineSimilarity.make_as_a(user_idx, records))

@app.route('/is_inner_user/<int:user_idx>', methods=['GET'])
def is_inner_user(user_idx):
    return str(CosineSimilarity.is_inner_user(user_idx))

app.run(host='127.0.0.1', port=3009, debug=True)