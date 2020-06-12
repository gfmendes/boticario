from flask import Flask
from flask_restful import Api
from app.controller.resources import ResellerResource, AuthResource, PurchaseResource, PurchaseListResource, CashbackResource

def init_routes(api):
    api.add_resource(ResellerResource, '/reseller/')
    api.add_resource(AuthResource, '/auth/')
    api.add_resource(PurchaseResource, '/purchase/')
    api.add_resource(PurchaseListResource, '/purchase/<cpf>')
    api.add_resource(CashbackResource, '/cashback/<cpf>')

