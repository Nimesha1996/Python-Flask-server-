import os
import sys
import json

sys.path.append(os.getcwd() + '/..')
#from openapi_server.app import db  
from openapi_server.appConfig import db , ma 
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
#from flask_sqlalchemy import relationship
from sqlalchemy.orm import sessionmaker, relationship

#Order_Pet = db.Table('Order_Pet', db.metadata,
#    db.Column('order_id', db.Integer, db.ForeignKey('Order.id')),
#    db.Column('pet_id', db.Integer, db.ForeignKey('Pet.id'))
#)

Pet_Order = db.Table('Pet_Order', db.metadata,
    db.Column('pet_id', db.Integer, db.ForeignKey('Pet.id')),
    db.Column('order_id', db.Integer, db.ForeignKey('Order.id')),
    extend_existing=True
)

Pet_Category = db.Table('Pet_Category', db.metadata,
    db.Column('pet_id', db.Integer, db.ForeignKey('Pet.id')),
    db.Column('category_id', db.Integer, db.ForeignKey('Category.id')),
    extend_existing=True
)

Pet_Tag = db.Table('Pet_Tag', db.metadata,
    db.Column('pet_id', db.Integer, db.ForeignKey('Pet.id')),
    db.Column('tag_id', db.Integer, db.ForeignKey('Tag.id')),
    extend_existing=True
)


class Tag(db.Model):
    __tablename__ = 'Tag'
    __table_args__ = {'extend_existing': True}
    id = db.Column(db.Integer(), primary_key=True)
    name= db.Column(db.String(120), nullable=False)



class Category(db.Model):
    __tablename__ = 'Category'
    __table_args__ = {'extend_existing': True}
    id = db.Column(db.Integer(), primary_key=True)
    name= db.Column(db.String(120), nullable=False)
#    pet = relationship('Pet', back_populates="category" , secondary=Pet_Category,  lazy=True)
#    pet = db.relationship('Pet', backref='Category',secondary=Pet_Category, lazy=True)



class Order(db.Model):
    __tablename__ = 'Order'
    __table_args__ = {'extend_existing': True}
    id = db.Column(db.Integer(), primary_key=True)
    petId =  db.Column(db.Integer, db.ForeignKey('Pet.id'), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    shipDate = db.Column(db.String(120), nullable=False)
    status = db.Column(db.String(120), nullable=False)
    complete = db.Column(db.Boolean, nullable=False)
  #  pet = db.relationship("Pet", back_populates="Order")
#    pet = db.relationship('Pet', backref="Order",secondary=Pet_Order,  lazy=True )
  #  pet = relationship("Pet", back_populates="order") 
   
#    Pet = db.relationship("Pet", back_populates="Order")
#   pet = db.relationship('Pet', secondary=Order_Pet, backref=db.backref('Order', lazy='dynamic'), lazy='dynamic')
   

    def __init__(self, id, pet_id, quantity, shipDate, status, complete):
        self.id = id
        self.petId = petId
        self.quantity = quantity
        self.shipDate = shipDate
        self.status = status
        self.complete = complete

class OrderSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Order

order_schema = OrderSchema()

"""
Pet_Category = db.Table('Pet_Category', db.metadata,
    db.Column('pet_id', db.Integer, db.ForeignKey('Pet.id')),
    db.Column('category_id', db.Integer, db.ForeignKey('Category.id')),
    extend_existing=True
)

Pet_Tag = db.Table('Pet_Tag', db.metadata,
    db.Column('pet_id', db.Integer, db.ForeignKey('Pet.id')),
    db.Column('tag_id', db.Integer, db.ForeignKey('Tag.id')),
    extend_existing=True
)
"""
class Pet(db.Model):
    __tablename__ = 'Pet'
    __table_args__ = {'extend_existing': True}
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    category = relationship('Category', backref="pet",secondary=Pet_Category,  lazy=True )
    photoUrls = db.Column(db.PickleType, nullable=True)
    tags = db.relationship('Tag', backref='Pet',secondary=Pet_Tag, lazy=True)
    status = db.Column(db.String(120), nullable=False)
  #  Order = db.relationship('Order', back_populates='Pet', lazy=True)    
  #  order = db.relationship("Order", back_populates="pet" ,lazy='dynamic', primaryjoin="Pet.id == Order.petId")
    order = db.relationship('Order', backref='Pet',secondary=Pet_Order, lazy=True)     
#    order = relationship("Order", back_populates="pet" ,lazy='dynamic', primaryjoin="Pet.id == Order.pet_id")

    def __init__(self, id, name,category, photoUrls,tags, status):
        self.id = id
        self.name = name
        self.category = category
        self.photoUrls = photoUrls
        self.tags = tags
        self.status = status

class PetSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Pet
        include_relationships = True
        

pet_schema = PetSchema()


"""
class Category(db.Model):
    __tablename__ = 'Category'
    __table_args__ = {'extend_existing': True}
    id = db.Column(db.Integer(), primary_key=True)
    name= db.Column(db.String(120), nullable=False)
#    Pet = relationship("Pet", back_populates="Category" , secondary=Pet_Category,  lazy=True)
#    pet = db.relationship('Pet', backref='Category',secondary=Pet_Category, lazy=True)

"""

"""
class Tag(db.Model):
    __tablename__ = 'Tag'
    __table_args__ = {'extend_existing': True}
    id = db.Column(db.Integer(), primary_key=True)
    name= db.Column(db.String(120), nullable=False)

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
	
    def __init__(self, id, username, firstName, lastName, password, email, phone, userStatus):
        self.id = id
        self.username = username
        self.firstName = firstName
        self.lastName = lastName
        self.password = password
        self.email = email
        self.phone = phone
        self.userStatus = userStatus

class UserSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = User

user_schema = UserSchema()
	

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
