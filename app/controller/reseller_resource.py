import json
from flask_restful import Resource, request, abort
from app.service.reseller_service import ResellerService
from app.controller.schema_validation.reseller_schema import ResellerInputSchema

class ResellerResource(Resource):
    def post(self):
        #data input validations
        errors = ResellerInputSchema().validate(request.get_json())
        if errors:
            return str(errors), 400
        
        #business checks
        errors = ResellerService().check_reseller_exists(request.get_json())
        if errors:
            return str(errors), 400

        return ResellerService().add(request.get_json()), 201
