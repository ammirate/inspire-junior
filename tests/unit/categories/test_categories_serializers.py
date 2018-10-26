from backend.categories.serializers import CategorySchema
from backend.categories.models import Category


def test_cat_schema():
    cat = Category(name='hep-th')
    expected_json = {
        'name': 'hep-th',
        'id': 0,
    }
    serialized_data = CategorySchema().dump(cat).data
    assert serialized_data == expected_json
