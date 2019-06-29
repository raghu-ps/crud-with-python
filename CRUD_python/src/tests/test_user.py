import unittest
import os
import json
from ..app import create_app, db

class UsersTest(unittest.TestCase):
  """
  Users Test Case
  """
  def setUp(self):
    """
    Test Setup
    """
    self.app = create_app("testing")
    self.client = self.app.test_client
    self.user = {
                 "id":12,
                 "name":"Game of Thrones",
                 "isbn": "456-987-0071",
                 "authors":"Raghu",
                 "country":"USA",
                 "pages":"128",
                 "publisher":"TATA",
                 "release_date":"12/06/2011"
                }

    with self.app.app_context():
      # create all tables
      db.create_all()
  
  def test_book_creation(self):
    """ test user creation with valid credentials """
    res = self.client().post('/api/v1/books/', headers={'Content-Type': 'application/json'}, data=json.dumps(self.user))
    json_data = json.loads(res.data)
    self.assertEqual(res.status_code, 201)

  def test_book_creation_with_existing_email(self):
    """ test book creation with already existing id"""
    res = self.client().post('/api/v1/books/', headers={'Content-Type': 'application/json'}, data=json.dumps(self.user))
    self.assertEqual(res.status_code, 400)
    res = self.client().post('/api/v1/books/', headers={'Content-Type': 'application/json'}, data=json.dumps(self.user))
    json_data = json.loads(res.data)
    self.assertEqual(res.status_code, 400)
    self.assertTrue(json_data.get('error'))

  def test_book_creation_with_no_id(self):
    """ test book creation with no id"""
    user = {
                 "name":"Game of Thrones",
                 "isbn": "456-987-0071",
                 "authors":"Raghu",
                 "country":"USA",
                 "pages":"128",
                 "publisher":"TATA",
                 "release_date":"12/06/2011"
                }
    res = self.client().post('/api/v1/books/', headers={'Content-Type': 'application/json'}, data=json.dumps(user1))
    json_data = json.loads(res.data)
    self.assertEqual(res.status_code, 400)

  def test_book_creation_with_no_book_name(self):
    """ test user creation with no email """
    user1 = {
                 "id":12,
                 "isbn": "456-987-0071",
                 "authors":"Raghu",
                 "country":"USA",
                 "pages":"128",
                 "publisher":"TATA",
                 "release_date":"12/06/2011"
    }
    res = self.client().post('/api/v1/books/', headers={'Content-Type': 'application/json'}, data=json.dumps(user1))
    json_data = json.loads(res.data)
    self.assertEqual(res.status_code, 400)
    self.assertTrue(json_data.get('email'))

  def test_book_creation_with_empty_request(self):
    """ test user creation with empty request """
    user1 = {}
    res = self.client().post('/api/v1/books/', headers={'Content-Type': 'application/json'}, data=json.dumps(user1))
    json_data = json.loads(res.data)
    self.assertEqual(res.status_code, 400)
  
 

  def test_book_get_book(self):
    """ Test User Get Me """
    res = self.client().get('/api/v1/books/12', headers={'Content-Type': 'application/json'})
    json_data = json.loads(res.data)
    self.assertEqual(res.status_code, 200)

  def test_user_update_book(self):
    """ Test User Update Me """
    user1 = {
                 "id":12,
                 "name":"Game of Thrones",
                 "isbn": "456-987-8451",
                 "authors":"Sandeep",
                 "country":"USA",
                 "pages":"128",
                 "publisher":"TATA",
                 "release_date":"12/06/2011"
                }
    res = self.client().put('/api/v1/books/12', headers={'Content-Type': 'application/json'}, data=json.dumps(user1))
    json_data = json.loads(res.data)
    self.assertEqual(res.status_code, 200)

  def test_delete_book(self):
    """ Test User Delete """
    api_token = json.loads(res.data).get('jwt_token')
    res = self.client().delete('/api/v1/books/12', headers={'Content-Type': 'application/json'})
    self.assertEqual(res.status_code, 204)
    
  def tearDown(self):
    """
    Tear Down
    """
    with self.app.app_context():
      db.session.remove()
      db.drop_all()

if __name__ == "__main__":
  unittest.main()