from flask_restful import Resource, request
from flask_jwt_extended import (create_access_token, create_refresh_token, jwt_required, jwt_refresh_token_required, get_jwt_identity, get_raw_jwt)
from cashback.controller.schema_validation import (AuthInputSchema,CashBackInputSchema,PurchaseInputSchema,ResellerInputSchema)
from cashback.services.purchase import PurchaseService
from cashback.services.reseller import ResellerService


class AuthResource(Resource):
  def post(self):
    #data input validations
    errors = AuthInputSchema().validate(request.get_json())
    if errors: return errors, 400

    login_data = request.get_json()
    if ResellerService().validate_reseller_password(login_data):
      access_token = create_access_token(identity=login_data['email'])          
      refresh_token = create_refresh_token(identity=login_data['email'])
      return {'access_token' : access_token, 'refresh_token' : refresh_token}, 200
    else :
      return {'error':'incorrect email or password'}, 400

class ResellerResource(Resource):
  def post(self):
    #data input validations
    errors = ResellerInputSchema().validate(request.get_json())
    if errors: return str(errors), 400

    result = ResellerService().add_reseller(request.get_json())
    return (result, 400) if 'error' in result.keys() else (result, 201)

class CashbackResource(Resource):
  @jwt_required
  def get(self, cpf):
    return ResellerService().get_cashback_amount(cpf), 200

class PurchaseResource(Resource):
  @jwt_required
  def post(self):
    #data input validations
    errors = PurchaseInputSchema().validate(request.get_json())
    if errors:
        return str(errors), 400

    result = PurchaseService().add_purchase(request.get_json())
    return (result, 400) if 'error' in result.keys() else (result, 201)

class PurchaseListResource(Resource):
  @jwt_required
  def get(self, cpf):
    return PurchaseService().list_current_month_purchases(cpf), 200