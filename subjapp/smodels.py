from datetime import datetime
from subjapp import db


class User(db.Model):
    id = db.Column(db.String(9), primary_key = True, nullable=False)
    username = db.Column(db.String(9), unique = True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    #image_file = db.Column(db.String(20), nullable=False, default='default.jpg')
    password = db.Column(db.String(100), nullable=False)
    posts = db.relationship('Post', backref='author', lazy=True)
    
    def __repr__(self):
        return f"User('{self.id}', '{self.username}', '{self.email}')"


#return f"User('{self.rollno}', '{self.email}','{self.image_file}', '(self.email)')"

class Post(db.Model):    
    id = db.Column(db.String(9), primary_key = True)
    title = db.Column(db.String(100), nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    content = db.Column(db.Text, nullable=False)
    users_rollnumber = db.Column(db.String(9), db.ForeignKey('user.username'), nullable=False)

    def __repr__(self):
        return f"Post('{self.title}', '{self.date_posted}')"
        

"""
if __name__ == '__main__':
    init_db() 
"""    