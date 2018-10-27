from marshmallow import fields, Schema
from backend.categories.serializers import CategorySchema


class ArticleSchema(Schema):
    """Serializer for scientific articles"""
    id = fields.Int()
    category_id = fields.Integer()
    abstract = fields.String()
    title = fields.String()
    category = fields.Nested(CategorySchema)
