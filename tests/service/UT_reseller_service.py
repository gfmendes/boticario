import unittest
from mock import MagicMock
from app.service.reseller_service import ResellerService
from app.dao.reseller_dao import ResellerDao

class ResellerServiceTest(unittest.TestCase) :
    
    def test_when_add(self):
        #Given
        dao = ResellerDao()
        dao.add = MagicMock(return_value=123)
        ResellerService().add("test")
        #then
        self.assertEqual(123, 123)