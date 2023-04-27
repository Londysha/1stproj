#import the flask and sqlalchemy modules
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask import request, render_template


#create an app instance and configure the database URI
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mydb.sqlite'

#create a database instance and bind it to the app
db = SQLAlchemy(app)

#define a model class for your database table
class User(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  username = db.Column(db.String(80), unique=True)
  password = db.Column(db.String(120))

  def __init__(self, username, password):
    self.username = username
    self.password = password

#create the database and tables
with app.app_context():
  db.create_all()

@app.route('/')
def index():
    return render_template('index.html')

#set a api route to get all users from the database
@app.route('/users')
def get_users():
  users = User.query.all()
  return { 'users': list(map(lambda user: { 'username': user.username, 'password': user.password }, users)) }

#set a api route to add a new user to the database
@app.route('/users', methods=['POST'])
def add_user():
  user = User(request.json['username'], request.json['password'])
  db.session.add(user)
  db.session.commit()
  return { 'user': { 'username': user.username, 'password': user.password } }

#

if __name__ == '__main__':
  app.run(debug=True)