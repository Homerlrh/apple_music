from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = 'password'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///sqlalchemydemo.db'

db = SQLAlchemy(app)

#each class will be its own table in the database

#user model
class User(db.Model):
    #columns for table:
    id = db.Column(db.Integer, primary_key=True) #data type of integer, set it to be the primary key

                    #max length of 20 characters
    username = db.Column(db.String(20), unique=True, nullable=False) #make them unique, and cannot be false
                    
                    #max length of 120 characters
    email = db.Column(db.String(120), unique=True, nullable=False)

                    #hashed password of length 60 characters
    password = db.Column(db.String(60), nullable=False)

    #instructs how to print out objects
    def __repr__(self):
        #print out the username every thing you print out the user object
        return f"User('{self.username}', '{self.email}')"




db.session.add(User(name="Flask", email="example@example.com"))
db.session.commit()

users = User.query.all()
print(users)