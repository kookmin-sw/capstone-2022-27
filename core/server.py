from flask import Flask, abort, request

import json

from models.gnn import GNN
from models.latent_factor import LatentFactor

app = Flask(__name__)

N_BOOK = 5000
N_USER = 5000

if __name__ == "__main__":
    GNN.init()
    LatentFactor.init()

@app.before_request
def whitelist():
    if request.remote_addr not in ['127.0.0.1']:
        abort(403)

@app.route('/gnn/usertobooks/<int:user_idx>')
def gnn_user_to_books(user_idx):
    return json.dumps(GNN.user_to_books(user_idx))

@app.route('/gnn/booktobooks/<int:book_idx>')
def gnn_book_to_books(book_idx):
    return json.dumps(GNN.book_to_books(book_idx)[:N_BOOK])

@app.route('/gnn/reload')
def gnn_reload():
    GNN.init()

@app.route('/latent_factor/usertobooks/<int:user_idx>')
def latent_factor_user_to_books(user_idx):
    return json.dumps(LatentFactor.user_to_books(user_idx)[:N_USER])

@app.route('/latent_factor/update/<int:user_idx>/<int:book_idx>/<float:rating>')
def latent_factor_update(user_idx, book_idx, rating):
    LatentFactor.update(user_idx, book_idx, rating)
    
@app.route('/latent_factor/recompute/<int:user_idx>')
def latent_factor_recompute(user_idx, book_idx, rating):
    LatentFactor.compute()

app.run(host='127.0.0.1', port=3009, debug=True)