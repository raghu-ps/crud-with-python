from flask import Flask,json,Response,request
import requests
from .config import app_config
from .models import db
from .views.UserView import user_api as user_blueprint

def create_app(env_name):
  """
  Create app
  """
  
  # app initiliazation
  app = Flask(__name__)

  app.config.from_object(app_config[env_name])

  db.init_app(app)
  app.register_blueprint(user_blueprint, url_prefix='/api/v1/books')

  @app.route('/external-books', methods=['GET'])
  def index():
    print("Inside the app")
    try:
      print("request args", request.args.get('name'))
      final_json = {}
      if 'name' in request.args:
        name = str(request.args.get('name'))
        print("name from args", name)
        # api-endpoint 
        URL = "https://www.anapioficeandfire.com/api/books"
        PARAMS = {'name':name}
        # sending get request and saving the response as response object 
        r = requests.get(url = URL, params = PARAMS)
        # extracting data in json format 
        data = r.json()
        #print("data", data)
        books_list = []
        for book in data:
            book_json = {}
            print("Inside the data")
            #print("BOOK", book)
            print("name of book", book['name'])
            book_json['name'] = book['name']
            book_json['isbn'] = book['isbn']
            book_json['authors'] = book['authors']
            book_json['number_of_pages'] = book['numberOfPages']
            book_json['publisher'] = book['publisher']
            book_json['country'] = book['country']
            book_json['release_date'] = book['released']
            books_list.append(book_json)
            
        final_json['status_code'] = 200
        final_json['status'] = 'Success'
        final_json['data'] = books_list
      return Response(
           mimetype="application/json",
           response=json.dumps(final_json),
           status=200
           )
    except:
       data = []
       except_json  = {}
       except_json['status_code'] = 200
       except_json['status'] = 'success'
       except_json = data
       return Response(mimetype="application/json",
                       response=json.dumps(except_json),
                       status=200)
  return app