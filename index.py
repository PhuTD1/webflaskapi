from flaskblog import app, db
from flaskblog.models import Student
with app.app_context():
    db.create_all() 
    