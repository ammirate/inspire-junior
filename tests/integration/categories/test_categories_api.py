import json
import pytest
import pkg_resources

from backend.categories.api import (
    get_categories,
    read_category,
    create_category,
    update_category,
    delete_category,
)
from backend.categories.errors import CategoryValueError


def test_get_categories_empty_db(test_app):
    assert get_categories() == []


def test_get_categories_non_empty_db(test_app, db_category):
    assert len(get_categories()) == 1


def test_read_category(test_app, db_category):
    category = read_category(db_category.id)
    assert category
    assert category.name == 'hep-th'


def test_read_category_not_in_db(test_app):
    read_category(98877554)


def test_create_category(test_app):
    model = create_category(name='hep')
    model_id = model.id

    db_model = read_category(model_id)
    assert db_model.name == 'hep'


def test_create_category_no_name(test_app):
    with pytest.raises(CategoryValueError):
        create_category(name=None)


def test_update_category(test_app, db_category):
    with pytest.raises(NotImplementedError):
        update_category(db_category.id, name='astro-ph')


def test_delete_category(test_app, db_category):
    category_id = db_category.id
    delete_category(category_id)
    assert read_category(category_id) is None
