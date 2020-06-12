from flask_restful import Resource, request
from app.service.reseller_service import ResellerService
from app.controller.schema_validation.auth_schema import AuthInputSchema

class AuthResource(Resource):
    
  def post(self):
    errors = AuthInputSchema().validate(request.get_json())
    if errors:
      return str(errors), 400
    login_data = request.get_json()
    return ResellerService().validate_password(login_data), 200