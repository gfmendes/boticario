from marshmallow import Schema, fields
from marshmallow.validate import Length

class PurchaseInputSchema(Schema):
    code = fields.Int(required=True)
    value = fields.Float(required=True)
    cpf = fields.Str(required=True, validate=Length(equal=11))
    date = fields.Str(required=True) 