from app.models.user import User
from marshmallow import validate, fields, Schema, post_load

class UserSchema(Schema):
    id = fields.Integer(dump_only=True)
    name = fields.String(required=True, validate=validate.Length(min=5, max=120))
    email = fields.Email(required=True, validate=validate.Length(min=5, max=120))
    password = fields.String(required=True, validate=validate.Length(min=8, max=120), load_only=True)
    data = fields.Nested('UserDataSchema')
    
    @post_load
    def make_user(self, data, **kwargs):
        return User(**data)
