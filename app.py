from flask import Flask
from flask_cors import CORS
from models import db, Login
from routes._init_ import register_route
import os
from flask_session import Session

app = Flask(__name__, static_folder='static')

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:Kavi%40123@localhost:3306/shop'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

app.secret_key = 'IVAKA'  

db.init_app(app)
register_route(app)
os.makedirs(os.path.join(app.root_path, 'static', 'uploads'), exist_ok=True)

CORS(app, supports_credentials=True, origins=["http://localhost:5173"])

app.config['SESSION_TYPE'] = 'filesystem'   
app.config['SESSION_PERMANENT'] = False
app.config['SESSION_USE_SIGNER'] = True
Session(app)

with app.app_context():
 db.create_all()
 if __name__ == '__main__':
    app.run(debug=True)
