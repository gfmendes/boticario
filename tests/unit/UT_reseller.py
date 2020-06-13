import unittest
from mock import MagicMock
from app.services.reseller import ResellerService
from app.database.data_access import ResellerDao

class ResellerServiceTest(unittest.TestCase) :
    
    def test_when_add(self):
        #Given
        reseller = {}
        reseller['password'] = '123456'
        dao = ResellerDao()
        dao.add = MagicMock(return_value='123456')
        ResellerService().add_reseller(reseller)
        #then
        self.assertEqual(123, 123)