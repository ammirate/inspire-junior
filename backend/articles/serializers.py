from marshmallow import fields, Schema


class ArticleSchema(Schema):
    """Serializer for scientific articles"""
    id = fields.Int()
    category = fields.String()
    abstract = fields.String()
    title = fields.String()
