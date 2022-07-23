from app import db

class User(db.Model):
    """
    User model
    """
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    lastname = db.Column(db.String(150), nullable=False)
    email = db.Column(db.String(200), unique=True, nullable=False)
    address = db.Column(db.Text)
    reference_address = db.Column(db.Text)
    phone_number = db.Column(db.String(20))
    
    def __repr__(self):
        return '<User %r>' % self.username


    def save(self):
        if not self.id :
            db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

  