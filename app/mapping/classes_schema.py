from marshmallow import Schema, fields

class ClassesSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True)
    instructor = fields.Str(required=True)
    type = fields.Str(required=True)
    capacity = fields.Int(required=True)