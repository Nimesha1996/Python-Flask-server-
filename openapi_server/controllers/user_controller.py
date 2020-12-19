import connexion
import six
from flask import Flask, request, jsonify
#from openapi_server.models.user import User  # noqa: E501
from openapi_server.classes.db_model import *
from openapi_server import util
from openapi_server.appConfig import db 

def create_user():  # noqa: E501
    """Create user

    This can only be done by the logged in user. # noqa: E501

    :param user: Created user object
    :type user: dict | bytes

    :rtype: User
    
    if connexion.request.is_json:
        user = User.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
    """

    id = request.json['id']
    username = request.json['username']
    firstName= request.json['firstName']
    lastName = request.json['lastName']
    email = request.json['email']
    phone = request.json['phone']
    userStatus = request.json['userStatus']

    new_user = User(id,username,firstName,lastName,email,phone,userStatus)

    db.session.add(new_user)
    db.session.commit()

    return user_schema.jsonify(new_user)

def create_users_with_list_input(user=None):  # noqa: E501
    """Creates list of users with given input array

    Creates list of users with given input array # noqa: E501

    :param user: 
    :type user: list | bytes

    :rtype: User
    """
    if connexion.request.is_json:
        user = [User.from_dict(d) for d in connexion.request.get_json()]  # noqa: E501
    return 'do some magic!'


def delete_user(username):  # noqa: E501
    """Delete user

    This can only be done by the logged in user. # noqa: E501

    :param username: The name that needs to be deleted
    :type username: str

    :rtype: None
    
    return 'do some magic!'
    """

    user = User.query.get(username)
    print(user)
    username.session.delete(user)
    username.session.commit()

    return username.jsonify(user)

def get_user_by_name(username):  # noqa: E501
    """Get user by user name

     # noqa: E501

    :param username: The name that needs to be fetched. Use user1 for testing. 
    :type username: str

    :rtype: User
    """
 
#    userbyname = User.query.filter(User.username == username)
#    result = user_schema.dump(userbyname)
#    return jsonify(result)
   
    print(User.query.all())
 #   UserbyName= User.query.filter_by(request.json['username']).first()
    UserbyName = User.query.filter_by(username=username).first_or_404() 
 #   print(UserbyName.username)
 #   print(UserbyName.firstName)
#   userByName = User.query.get(username)
#    result = user_schema.dump(UserbyName)
#    return UserbyName
#    return 'hello'
 #   UserbyName = User.query.get(username)
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


def update_user(username, user=None):  # noqa: E501
    """Update user

    This can only be done by the logged in user. # noqa: E501

    :param username: name that need to be deleted
    :type username: str
    :param user: Update an existent user in the store
    :type user: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        user = User.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'

