import connexion
import six
from flask import Flask, request, jsonify
#from openapi_server.models.user import User  # noqa: E501
from openapi_server.classes.db_model import *
from openapi_server import util
from openapi_server.appConfig import db 

def create_user():  # noqa: E501
       
    id = request.json.get('id' , '')
    username = request.json.get('username', '')
    firstName= request.json.get('firstName', '')
    lastName = request.json.get('lastName', '')
    password = request.json.get('password', '')
    email = request.json.get('email', '')
    phone = request.json.get('phone','')
    userStatus = request.json.get('userStatus', '')

    new_user = User(id=id,username=username,firstName=firstName,lastName=lastName,password=password,email=email,phone=phone,userStatus=userStatus)

    db.session.add(new_user)
    db.session.commit()

    return user_schema.jsonify(new_user)

def create_users_with_list_input(user=None):  # noqa: E501

    id = request.json.get('id' , '')
    username = request.json.get('username', '')
    firstName= request.json.get('firstName', '')
    lastName = request.json.get('lastName', '')
    password = request.json.get('password', '')
    email = request.json.get('email', '')
    phone = request.json.get('phone','')
    userStatus = request.json.get('userStatus', '')

    new_user = User(id=id,username=username,firstName=firstName,lastName=lastName,password=password,email=email,phone=phone,userStatus=userStatus)

    db.session.add(new_user)
    db.session.commit()

    return user_schema.jsonify(new_user)

    


def delete_user(username):  # noqa: E501
    """Delete user

    This can only be done by the logged in user. # noqa: E501

    """
    
    user = User.query.filter_by(username=username).first_or_404()
  
    print(username)

    db.session.delete(user)
    db.session.commit()
     
    return user_schema.jsonify(user)

def get_user_by_name(username):  # noqa: E501
    """Get user by user name

     # noqa: E501

    :param username: The name that needs to be fetched. Use user1 for testing. 
    :type username: str

    :rtype: User
    """
   
    print(User.query.all())

    UserbyName = User.query.filter_by(username=username).first_or_404() 
 
    print(UserbyName)
    print(UserbyName.email)
    return user_schema.jsonify(UserbyName)

def login_user(username=None, password=None):  # noqa: E501
    """Logs user into the system

     # noqa: E501

    :param username: The user name for login
    :type username: str
    :param password: The password for login in clear text
    :type password: str

    :rtype: str
    """
    return 'do some magic!'


def logout_user():  # noqa: E501
    """Logs out current logged in user session

     # noqa: E501


    :rtype: None
    """
    return 'do some magic!'


def update_user(username):  # noqa: E501
    """Update user

    This can only be done by the logged in user. # noqa: E501

    :param username: name that need to be deleted
    :type username: str
    :param user: Update an existent user in the store
    :type user: dict | bytes

    :rtype: None
    """

    update_user = User.query.filter_by(username=username).first_or_404()

    print(update_user)

    id = request.json.get('id' , '')
    username = request.json.get('username', '')
    firstName= request.json.get('firstName', '')
    lastName = request.json.get('lastName', '')
    password = request.json.get('password', '')
    email = request.json.get('email', '')
    phone = request.json.get('phone','')
    userStatus = request.json.get('userStatus', '')
    

    update_user.id = id
    update_user.username = username
    update_user.firstName = firstName
    update_user.lastName = lastName
    update_user.password = password
    update_user.email = email
    update_user.phone = phone
    update_user.userStatus = userStatus

    db.session.add(update_user)
    db.session.commit()

    return user_schema.jsonify(update_user)
    
