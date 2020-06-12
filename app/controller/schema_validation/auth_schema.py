from marshmallow import Schema, fields
from marshmallow.validate import Length

class AuthInputSchema(Schema):
    email = fields.Str(required=True, validate=Length(min=1)) #email validation can be improved using regex
    password = fields.Str(required=True, validate=Length(min=8))