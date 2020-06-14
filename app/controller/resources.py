from app.controller.schema_validation import (AuthInputSchema,
                                              CashBackInputSchema,
                                              PurchaseInputSchema,
                                              ResellerInputSchema)
from app.services.purchase import PurchaseService
from app.services.reseller import ResellerService
from flask_restful import Resource, request


class AuthResource(Resource):
  def post(self):
    #data input validations
    errors = AuthInputSchema().validate(request.get_json())
    if errors:
      return str(errors), 400

    login_data = request.get_json()
    return ResellerService().validate_reseller_password(login_data), 200

class CashbackResource(Resource):
  def get(self, cpf):
    return ResellerService().get_cashback_amount(cpf), 200

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

    return PurchaseService().add_purchase(request.get_json()), 201

class PurchaseListResource(Resource):
  def get(self, cpf):
    return PurchaseService().list_current_month_purchases(cpf), 200

class ResellerResource(Resource):
  def post(self):
    #data input validations
    errors = ResellerInputSchema().validate(request.get_json())
    if errors:
        return str(errors), 400

    result = ResellerService().add_reseller(request.get_json())
    
    if 'error' in result:
      return result, 400
    else:
      return result, 201