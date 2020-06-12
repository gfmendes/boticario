from flask_restful import Resource, request
from app.service.purchase_service import PurchaseService
from app.controller.schema_validation.purchase_schema import PurchaseInputSchema

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