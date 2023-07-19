from datetime import datetime
from flaskblog import db
from flask_login import UserMixin




class Student(db.Model , UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    Year = db.Column(db.Integer , nullable = False ,default =2022 )
    SBD = db.Column(db.Integer, nullable = False)
    Toán = db.Column(db.Float ,nullable = True)
    Van = db.Column(db.Float ,nullable = True)
    Su = db.Column(db.Float ,nullable = True)
    Dia = db.Column(db.Float ,nullable = True)
    Li = db.Column(db.Float ,nullable = True)
    Hoa = db.Column(db.Float ,nullable = True)
    Sinh = db.Column(db.Float ,nullable = True)
    NN = db.Column(db.Float ,nullable = True)
    GDCD = db.Column(db.Float ,nullable = True)
    
    def items(self):
        item ={'SBD':self.SBD, 'Toán' : self.Toán , 'Văn':self.Van , 'Ngoại ngữ' : self.NN,
               'Lí' : self.Li , 'Hóa' : self.Hoa , 'Sinh':self.Sinh,
               'Địa': self.Dia , 'Sử' : self.Su , 'GDCD' : self.GDCD}
        return item
    
    def __repr__(self):
        return f"Student('{self.Toán}', '{self.Van}', '{self.Su}')"


class Rank(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    Year = db.Column(db.Integer , nullable = False ,default =2022 )
    SBD = db.Column(db.Integer, nullable = False)
    A00 = db.Column(db.Float,nullable = True )
    AO1 = db.Column(db.Float,nullable = True )
    B00 = db.Column(db.Float,nullable = True )
    C00 = db.Column(db.Float,nullable = True )
    
    