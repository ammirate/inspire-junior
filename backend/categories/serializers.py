from marshmallow import fields, Schema


class CategorySchema(Schema):
    """Serializer for scientific articles"""
    id = fields.Int()
    name = fields.String()
