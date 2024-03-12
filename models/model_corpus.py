import sqlalchemy

from app import db
from sqlalchemy.sql import func


class Corpuses(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100), nullable=False, unique=True)
    corpus = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    created_at = db.Column(db.DateTime(timezone=True), nullable=False, server_default=func.now())
    updated_at = db.Column(db.DateTime(timezone=True), onupdate=func.now())


def Add_new_corpus(new_corpus):
    err_msg = f'error add new token:'
    try:
        corpus = Corpuses(
            name=new_corpus['name']
            , corpus=new_corpus['corpus']
            , user_id=new_corpus['user_id']

        )

        db.session.add(corpus)
        db.session.commit()
    except sqlalchemy.exc.OperationalError as err:
        return f'{err_msg} {err}'
    except sqlalchemy.exc.IntegrityError as err:
        return f'{err_msg} corpus name already registered'
    except:
        return 'unknown error add new corpus'

    return None


def View_all_corpus(**filters):
    err_msg = f'error view all tokens:'
    corpuses = []

    try:
        corpus_list =Corpuses.query.filter_by(**filters).order_by(Corpuses.created_at).all()

        for corpus in corpus_list:
            corpuses.append({
                "id": corpus.id
                , "name": corpus.name
                , "created_at": corpus.created_at
            })
    except sqlalchemy.exc.OperationalError as err:
        return None, f'{err_msg} {err}'
    except sqlalchemy.exc.IntegrityError as err:
        return None,f'{err_msg} {err}'
    except:
        return None, 'unknown error view all corpus'

    return corpuses, None


def Delete_current_corpus(current_corpus):
    err_msg = f'error delete current corpus:'

    try:
        db.session.delete(current_corpus)
        db.session.commit()
    except sqlalchemy.exc.OperationalError as err:
        return f'{err_msg} {err}'
    except sqlalchemy.exc.IntegrityError as err:
        return f'{err_msg} {err}'
    except:
        return 'unknown error delete current corpus'

    return None


def Find_corpus_by_id(corpus_id):
    try:
        curr_corpus = Corpuses.query.get(corpus_id)
        if curr_corpus is None:
            return None, "corpus not found"

        return curr_corpus, None
    except:
        return None, "error find corpus by id"


def Find_corpus_by_custom_filter(**filters):
    try:
        curr_corpus = Corpuses.query.filter_by(**filters).first()
        if curr_corpus is None:
            return None, "corpus not found"

        return curr_corpus, None
    except:
        return None, "error find corpus by id"
