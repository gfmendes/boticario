import unittest
import json
from cashback.app import app
import cashback.data.mongo_collections as mongo_collections

#Integration/automated tests 
class ResellerIntegrationTest(unittest.TestCase) :

  def setUp(self):
    self.app = app.test_client()
    mongo_collections.database = mongo_collections.client.boticario_tests

  def test_add_new_reseller(self):
    #Given
    payload1 = json.dumps({"cpf":"15138291498","name":"John","surname":"Galt","email":"snow@email.com","password":"12345678"})
    #When
    response = self.app.post('/cashback/reseller/', headers={'Content-Type': 'application/json'}, data=payload1)
    #Then
    self.assertEqual(201, response.status_code)
    self.assertEqual("15138291498", response.json['cpf'])

  def test_add_existent_email_reseller(self):
    #Given
    payload1 = json.dumps({"cpf":"15138291477","name":"John","surname":"Galt","email":"snow@email.com","password":"12345678"})
    payload2 = json.dumps({"cpf":"15138291498","name":"John","surname":"Snow","email":"snow@email.com","password":"12345678"})
    #When
    self.app.post('/cashback/reseller/', headers={'Content-Type': 'application/json'}, data=payload1) #adding first time
    response = self.app.post('/cashback/reseller/', headers={'Content-Type': 'application/json'}, data=payload2) #adding second time

    self.assertEqual(400, response.status_code)
    self.assertEqual("email exists", response.json['error'])

  def test_add_existent_cpf_reseller(self):
    #Given
    payload1 = json.dumps({"cpf":"15138291498","name":"John","surname":"Galt","email":"galt@email.com","password":"12345678"})
    payload2 = json.dumps({"cpf":"15138291498","name":"John","surname":"Snow","email":"snow@email.com","password":"12345678"})
    #When
    self.app.post('/cashback/reseller/', headers={'Content-Type': 'application/json'}, data=payload1) #adding first time
    response = self.app.post('/cashback/reseller/', headers={'Content-Type': 'application/json'}, data=payload2) #adding second time
    #Then
    self.assertEqual(400, response.status_code)
    self.assertEqual("cpf exists", response.json['error'])
  
  def tearDown(self):
    for collection in mongo_collections.database.list_collection_names():
      mongo_collections.database.drop_collection(collection)