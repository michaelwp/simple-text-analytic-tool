from apis.controllers.controller_corpus import (
    Register_new_corpus
    , Get_all_corpus_list
    , Delete_corpus
    , Load_current_corpus
)
from app import app
from middlewares.middleware_authentication import Token_authentication


@app.route('/corpuses/register', methods=['POST'])
@Token_authentication
def Corpus_register(user_id):
    return Register_new_corpus(user_id)


@app.route('/corpuses', methods=['GET'])
@Token_authentication
def Corpus_list(user_id):
    return Get_all_corpus_list(user_id)


@app.route('/corpuses/delete', methods=['DELETE'])
@Token_authentication
def Corpus_delete(user_id):
    return Delete_corpus(user_id)


@app.route('/corpuses/<corpus_id>', methods=['GET'])
@Token_authentication
def Corpus_load(user_id, corpus_id):
    return Load_current_corpus(user_id, corpus_id)
