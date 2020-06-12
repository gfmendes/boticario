from flask_restful import Resource, request
from app.controller.schema_validation import AuthInputSchema, PurchaseInputSchema, ResellerInputSchema, CashBackInputSchema
from app.services.cashback import CashBackService
from app.services.purchase import PurchaseService
from app.services.reseller import ResellerService

class AuthResource(Resource):
  def post(self):
    errors = AuthInputSchema().validate(request.get_json())
    if errors:
      return str(errors), 400

    login_data = request.get_json()
    return ResellerService().validate_password(login_data), 200

class CashbackResource(Resource):
  def get(self, cpf):
    return CashBackService().get_reseller_cashback(cpf), 200
      
  def post(self):
    return "", 201

class PurchaseResource(Resource):
  def post(self):
    #data input validations
    errors = PurchaseInputSchema().validate(request.get_json())
    if errors:
        return str(errors), 400

    #business checks
    errors = PurchaseService().validate_purchase(request.get_json())
    if errors:
        return str(errors), 400

    return PurchaseService().add(request.get_json()), 201

class PurchaseListResource(Resource):
  def get(self, cpf):
    return PurchaseService().list(cpf), 200

class ResellerResource(Resource):
  def post(self):
    #data input validations
    errors = ResellerInputSchema().validate(request.get_json())
    if errors:
        return str(errors), 400
    return ResellerService().add(request.get_json()), 201