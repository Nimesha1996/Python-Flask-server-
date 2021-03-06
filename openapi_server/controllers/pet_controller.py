import connexion
import six
from flask import Flask, request, jsonify
#from openapi_server.models.user import User  # noqa: E501
from openapi_server.classes.db_model import *
from openapi_server import util
from openapi_server.appConfig import db


def add_pet(pet=None):  # noqa: E501
    """Add a new pet to the store

    Add a new pet to the store # noqa: E501

    :param pet: Create a new pet in the store
    :type pet: dict | bytes

    :rtype: Pet
    """        
    

    id = request.json.get('id' , '')
    name = request.json.get('name', '')
    category= request.json.get('category', [])
    photoUrls = request.json.get('photoUrls', [])
    tags = request.json.get('tags', [])
    status = request.json.get('status', '')
 

    new_pet = Pet(id=id,name=name , category=category,photoUrls=photoUrls,tags=tags,status=status)

    db.session.add(new_pet)
    db.session.commit()

    return pet_schema.jsonify(new_pet)
    
    

def delete_pet(pet_id, api_key=None):  # noqa: E501
    """Deletes a pet

     # noqa: E501

    :param pet_id: Pet id to delete
    :type pet_id: int
    :param api_key: 
    :type api_key: str

    :rtype: None
    """
    


def find_pets_by_status(status=None):  # noqa: E501
    """Finds Pets by status

    Multiple status values can be provided with comma separated strings # noqa: E501

    :param status: Status values that need to be considered for filter
    :type status: str

    :rtype: List[Pet]
    """
 #   companies = [{"id": 1, "name": "Company One"}, {"id": 2, "name": "Company Two"}]
 #    return json.dumps(companies) 
   


def find_pets_by_tags(tags=None):  # noqa: E501
    """Finds Pets by tags

    Multiple tags can be provided with comma separated strings. Use tag1, tag2, tag3 for testing. # noqa: E501

    :param tags: Tags to filter by
    :type tags: List[str]

    :rtype: List[Pet]
    """
    return 'do some magic!'


def get_pet_by_id(pet_id):  # noqa: E501
    """Find pet by ID

    Returns a single pet # noqa: E501

    :param pet_id: ID of pet to return
    :type pet_id: int

    :rtype: Pet

    """
#    print(Pet.query.all())
#    pet = Pet.query.filter_by(id = pet_id).first_or_404() 
#    PetbyId = Pet.query.get(id)
#    PetbyId = Pet.query.filter_by(id=pet_id).first()
#    print(parent) 
     
#    pet = Pet.query.all()
#    print(pet)
#    print(PetbyId.name)
#    return pet_schema.jsonify(PetbyId)
    return 'do some magic!'

def update_pet(pet=None):  # noqa: E501
    """Update an existing pet

    Update an existing pet by Id # noqa: E501

    :param pet: Update an existent pet in the store
    :type pet: dict | bytes

    :rtype: Pet
    """
    if connexion.request.is_json:
        pet = Pet.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def update_pet_with_form(pet_id, name=None, status=None):  # noqa: E501
    """Updates a pet in the store with form data

     # noqa: E501

    :param pet_id: ID of pet that needs to be updated
    :type pet_id: int
    :param name: Name of pet that needs to be updated
    :type name: str
    :param status: Status of pet that needs to be updated
    :type status: str

    :rtype: None
    """
    return 'do some magic!'


def upload_file(pet_id, additional_metadata=None, body=None):  # noqa: E501
    """uploads an image

     # noqa: E501

    :param pet_id: ID of pet to update
    :type pet_id: int
    :param additional_metadata: Additional Metadata
    :type additional_metadata: str
    :param body: 
    :type body: str

    :rtype: ApiResponse
    """
    return 'do some magic!'
