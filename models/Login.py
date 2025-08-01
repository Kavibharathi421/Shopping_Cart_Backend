from models import db
from werkzeug.security import generate_password_hash, check_password_hash

class Login(db.Model):
    __tablename__ = 'login'

    login_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)
    phone_number = db.Column(db.String(20))
    role = db.Column(db.String(20), default='customer')

    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)
    
 