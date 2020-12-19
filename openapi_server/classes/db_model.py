import os
import sys
import json

sys.path.append(os.getcwd() + '/..')
#from openapi_server.app import db  
from openapi_server.appConfig import db , ma 

# from sqlalchemy.orm import sessionmaker, relationship

#Order_Pet = db.Table('Order_Pet', db.metadata,
#    db.Column('order_id', db.Integer, db.ForeignKey('Order.id')),
#    db.Column('pet_id', db.Integer, db.ForeignKey('Pet.id'))
#)

class Order(db.Model):
    __tablename__ = 'Order'
    __table_args__ = {'extend_existing': True}
    id = db.Column(db.Integer(), primary_key=True)
    petId =  db.Column(db.Integer, db.ForeignKey('Pet.id'), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    shipDate = db.Column(db.String(120), nullable=False)
    status = db.Column(db.String(120), nullable=False)
    complete = db.Column(db.Boolean, nullable=False)
    pet = db.relationship("Pet", back_populates="order")

#    Pet = db.relationship("Pet", back_populates="Order")
#   pet = db.relationship('Pet', secondary=Order_Pet, backref=db.backref('Order', lazy='dynamic'), lazy='dynamic')

Pet_Order = db.Table('Pet_Order', db.metadata,
    db.Column('pet_id', db.Integer, db.ForeignKey('Pet.id')),
    db.Column('category_id', db.Integer, db.ForeignKey('Category.id')),
    extend_existing=True
)

Pet_Tag = db.Table('Pet_Tag', db.metadata,
    db.Column('pet_id', db.Integer, db.ForeignKey('Pet.id')),
    db.Column('tag_id', db.Integer, db.ForeignKey('Tag.id')),
    extend_existing=True
)


class Pet(db.Model):
    __tablename__ = 'Pet'
    __table_args__ = {'extend_existing': True}
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    category = db.relationship('Category', backref="Pet",secondary=Pet_Order,  lazy=True )
    photoUrls = db.Column(db.String(120), nullable=False)
    tags = db.relationship('Tag', backref='Pet',secondary=Pet_Tag, lazy=True)
    status = db.Column(db.String(120), nullable=False)
  #  Order = db.relationship('Order', back_populates='Pet', lazy=True)    
    order = db.relationship("Order", back_populates="pet" ,lazy='dynamic', primaryjoin="Pet.id == Order.petId")
    

class Category(db.Model):
    __tablename__ = 'Category'
    __table_args__ = {'extend_existing': True}
    id = db.Column(db.Integer(), primary_key=True)
    name= db.Column(db.String(120), nullable=False)
   # pet = relationship("Pet", back_populates="category" , primaryjoin="Pet.category == Category.id ")




class Tag(db.Model):
    __tablename__ = 'Tag'
    __table_args__ = {'extend_existing': True}
    id = db.Column(db.Integer(), primary_key=True)
    name= db.Column(db.String(120), nullable=False)

"""
class Serializer(object):
    @staticmethod
    def serialize_list(l):
        return [m.serialize() for m in l]
"""

class User(db.Model):
    __tablename__ = 'User'
    __table_args__ = {'extend_existing': True}
    id = db.Column(db.Integer(), primary_key=True)
    username = db.Column(db.String(120), nullable=False)
    firstName = db.Column(db.String(120), nullable=False)
    lastName = db.Column(db.String(120), nullable=False)
    email = db.Column(db.String(120), nullable=False)
    password = db.Column(db.String(120), nullable=False)
    phone = db.Column(db.String(120), nullable=False)
    userStatus = db.Column(db.Integer, nullable=False)
	
    def __init__(self, id, username, firstName, lastName, email, phone, userStatus):
        self.id = id
        self.username = username
        self.firstName = firstName
        self.lastName = lastName
        self.email = email
        self.phone = phone
        self.userStatus = userStatus

class UserSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = User


    
"""    
# User Schema
    
class UserSchema(ma.Schema):
    class MetaUser:
        fields = ('id', 'username', 'firstName', 'lastName', 'email', 'phone', 'userStaus')

"""
user_schema = UserSchema()
   
""" 
def serialize(self):
    user_serialized = {
        'id': self.id ,
        'username': self.username,
        'firstName': self.firstName ,
        'lastName': self.lastName  ,
        'email': self.email,
        'phone': self.phone  ,
        'userStatus': self.userStatus 
    }

    return json.loads(json.dumps(user_serialized)
"""	

Customer_Address = db.Table('Customer_Address', db.metadata,
   
    db.Column('customer_id', db.Integer, db.ForeignKey('Customer.id')),
    db.Column('address_id', db.Integer, db.ForeignKey('Address.id')),
    extend_existing=True
)


class Customer(db.Model):
    __tablename__ = 'Customer'
    __table_args__ = {'extend_existing': True}
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(120), nullable=False)
    address = db.relationship('Address', backref='Customer',secondary=Customer_Address, lazy=True)

class Address(db.Model):
    __tablename__ = 'Address'
    __table_args__ = {'extend_existing': True}
    id= db.Column(db.Integer, primary_key=True)
    street = db.Column(db.String(120), nullable=False)
    city = db.Column(db.String(120), nullable=False)
    state = db.Column(db.String(120), nullable=False)
    zip = db.Column(db.String(120), nullable=False)
