import json


def test_get_categories_empty_db(test_client):
    resp = test_client.get('/api/categories/')
    resp_data = json.loads(resp.data)

    assert resp.status_code == 200
    assert resp_data == []


def test_get_categories_non_empty_db(test_client, db_category):
    resp = test_client.get('/api/categories/')
    resp_data = json.loads(resp.data)

    expected_data = [
        db_category.dump()
    ]

    assert resp.status_code == 200
    assert resp_data == expected_data


def test_get_category(test_client, db_category):
    category_id = db_category.id

    resp = test_client.get('/api/categories/%d' % category_id)
    resp_data = json.loads(resp.data)

    expected_data = db_category.dump()

    assert resp.status_code == 200
    assert resp_data == expected_data


def test_get_category_404(test_client):
    resp = test_client.get('/api/categories/123456789')
    assert resp.status_code == 404


def test_post_category(test_client):
    expected_data = {
        'name': 'it-se',
        'id': 1,
    }

    resp = test_client.post(
        '/api/categories/',
        data=json.dumps({"name": "it-se"}),
        content_type='application/json',
    )
    resp_data = json.loads(resp.data)

    assert resp.status_code == 200
    assert resp_data == expected_data


def test_post_category_bad_request(test_client):
    metadata = {"name": None}

    resp = test_client.post(
        '/api/categories/',
        data=json.dumps(metadata),
        content_type='application/json',
    )
    assert resp.status_code == 400
