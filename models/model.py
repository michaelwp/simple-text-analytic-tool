from app import app, db
import models.model_user
import models.model_corpus

with app.app_context():
    db.create_all()
