
#/src/views/UserView

from flask import request, json, Response, Blueprint
from ..models.UserModel import UserModel, UserSchema

user_api = Blueprint('books', __name__)
user_schema = UserSchema()

# add this new method
@user_api.route('/', methods=['GET'])
def get_all():
  try:
     users = UserModel.get_all_users()
     ser_users = user_schema.dump(users, many=True).data
     return custom_response(ser_users, 200)
  except:
    fin_json={}
    fin_json['status_code'] = 200
    fin_json['status'] = 'Success'
    fin_json['data'] = []
    return custom_response(fin_json, 201)


@user_api.route('/', methods=['POST'])
def create():
  """
  Create User Function
  """
  req_data = request.get_json()
  print("req_data", req_data)
  data, error = user_schema.load(req_data)

  print("Data",data)

  if error:
    return custom_response(error, 400)
  
  # check if user already exist in the db
  user_in_db = UserModel.get_one_user(data.get('id'))
  if user_in_db:
    message = {'error': 'Book already exist, please supply another ID'}
    return custom_response(message, 400)
  
  user = UserModel(data)
  user.save()

  ser_data = user_schema.dump(user).data

  return response_on_success(ser_data, 201)

@user_api.route('/<int:user_id>', methods=['PUT'])
def update(user_id):
  """
  Update me
  """
  req_data = request.get_json()
  data, error = user_schema.load(req_data, partial=True)
  if error:
    return custom_response(error, 400)

  user = UserModel.get_one_user(user_id)
  user.update(data)
  ser_user = user_schema.dump(user).data
  return custom_response(ser_user, 200)

@user_api.route('/<int:user_id>', methods=['DELETE'])
def delete(user_id):
  """
  Delete a user
  """
  user = UserModel.get_one_user(user_id)
  user.delete()
  return response_on_success({'message': 'deleted'}, 201)

 
@user_api.route('/<int:user_id>', methods=['GET'])
def get_a_user(user_id):
  """
  Get a single user
  """
  user = UserModel.get_one_user(user_id)
  if not user:
    return custom_response({'error': 'Book not found'}, 404)
  
  ser_user = user_schema.dump(user).data

  return response_on_success(ser_user, 201)
  

def custom_response(res, status_code):
  """
  Custom Response Function
  """
  return Response(
    mimetype="application/json",
    response=json.dumps(res),
    status=status_code
  )

def response_on_success(res, status_code):
  fin_json = {}
  fin_json['status_code'] = status_code
  fin_json['status'] = 'Success'
  fin_json['data'] = res
  return Response(
    mimetype="application/json",
    response=json.dumps(fin_json),
    status=status_code
  )
