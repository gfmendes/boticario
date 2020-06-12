from flask_restful import Resource, reqparse
from app.service.cashback_service import CashbackService

class CashbackResource(Resource):

    def get(self, cpf):
        return CashbackService().get_reseller_cashback(cpf), 200
        
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument("codigo")
        parser.add_argument("valor")
        parser.add_argument("data")
        parser.add_argument("cpf")
        args = parser.parse_args()
        return (args["codigo"]), 201
