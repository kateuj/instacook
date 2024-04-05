from recipes import db

class User(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(25), unique=True, nullable=False)
    password = db.Column(db.String, nullable=False)
    cookbook = db.relationship('#', backref='user', cascade="all, delete", lazy=True)

    def __repr__(self):
        return self.username