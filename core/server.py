from flask import Flask, abort, request

from models.embeddings import Embeddings
from models.latent_factor import LatentFactor

app = Flask(__name__)

Embeddings.init()
LatentFactor.init()

@app.before_request
def whitelist():
    if request.remote_addr not in ['127.0.0.1']:
        abort(403)

@app.route('/embeddings/usertobooks/<int:user_idx>')
def embedding_user_to_books(user_idx):
    return Embeddings.user_to_books(user_idx)

@app.route('/embeddings/booktobooks/<int:book_idx>')
def embedding_book_to_books(book_idx):
    return Embeddings.book_to_books(book_idx)

@app.route('/embeddings/reload')
def embedding_reload():
    Embeddings.init()

@app.route('/latent_factor/usertobooks/<int:user_idx>')
def latent_factor_user_to_books(user_idx):
    return LatentFactor.user_to_books(user_idx)

@app.route('/latent_factor/update/<int:user_idx>/<int:book_idx>/<float:rating>')
def latent_factor_update(user_idx, book_idx, rating):
    LatentFactor.update(user_idx, book_idx, rating)