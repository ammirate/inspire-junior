from marshmallow import fields, Schema


class ArticleSchema(Schema):
    """Serializer for scientific articles"""
    id = fields.Int()
    category_id = fields.Integer()
    abstract = fields.String()
    title = fields.String()
