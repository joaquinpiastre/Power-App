from marshmallow import Schema, fields

class GymClassSchema(Schema):
    id = fields.Int(dump_only=True)
    gym_name = fields.Str(required=True)
    instructors = fields.Nested('InstructorSchema', many=True, exclude=('gym_classes',))
    type_class = fields.Str(required=True)
