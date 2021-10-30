from . import db

class ListofUsers(db.Model):
    id = db.Column(db.Integer, primary_key = True)

    Username = db.Column(db.Text, nullable = False)
    Password = db.Column(db.Text, nullable = False)
    Email = db.Column(db.Text, nullable = False)
    Active = db.Column(db.Boolean, nullable = False, default = False)
    Admin = db.Column(db.Boolean, nullable = False, default = False)
    
    def __str__(self):
        return {
            self.Username:{
                "Password": self.Password,
                "Email": self.Email
            }
        }