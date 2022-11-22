from flask_sqlalchemy import SQLAlchemy


db= SQLAlchemy()

class User(db.Model):


    __tablename__= "users"
    
    username = db.column(dbtext , nullable = False, unique = True, primary_key = True) 
    password = db.column (db.Text , nullable = False)
    email = db.column(db.String(50), nullable = False)
    first_name = db.column(db.String(30), nullable = False)
    last_name = db.column(db.String(30), nullable = False)
    
    
    
