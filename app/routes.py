from flask import Flask
from flask_restful import Api
from app.controller.reseller_resource import ResellerResource
from app.controller.auth_resource import AuthResource
from app.controller.purchase_resource import PurchaseResource
from app.controller.purchase_resource import PurchaseListResource
from app.controller.cashback_resource import CashbackResource

def init_routes(api):
    api.add_resource(ResellerResource, '/reseller/')
    api.add_resource(AuthResource, '/auth/')
    api.add_resource(PurchaseResource, '/purchase/')
    api.add_resource(PurchaseListResource, '/purchase/<cpf>')
    api.add_resource(CashbackResource, '/cashback/<cpf>')

