from __future__ import absolute_import, division, print_function

from marshmallow import fields, Schema


class CategorySchema(Schema):
    """Serializer for scientific articles"""
    id = fields.Int()
    name = fields.String()
