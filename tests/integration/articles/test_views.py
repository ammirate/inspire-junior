import json


def test_get_articles_empty_db(test_client):
    resp = test_client.get('/api/articles/')
    resp_data = json.loads(resp.data)

    assert resp.status_code == 200
    assert resp_data == []


def test_get_articles_non_empty_db(test_client, db_article):
    resp = test_client.get('/api/articles/')
    resp_data = json.loads(resp.data)

    expected_data = [
        db_article.dump()
    ]

    assert resp.status_code == 200
    assert resp_data == expected_data


def test_get_article(test_client, db_article):
    article_id = db_article.id

    resp = test_client.get('/api/articles/%d' % article_id)
    resp_data = json.loads(resp.data)

    expected_data = db_article.dump()

    assert resp.status_code == 200
    assert resp_data == expected_data


def test_get_article_404(test_client):
    resp = test_client.get('/api/articles/123456789')
    assert resp.status_code == 404


def test_post_article(test_client, article):
    metadata = article.dump()
    expected_data = {
        'category': 'hep-th',
        'abstract': 'lorem ipsum',
        'id': 1,
        'title': 'A Model of Leptons'
    }

    resp = test_client.post(
        '/api/articles/',
        data=json.dumps(metadata),
        content_type='application/json',
    )
    resp_data = json.loads(resp.data)

    assert resp.status_code == 200
    assert resp_data == expected_data


def test_post_article_bad_request(test_client, ):
    metadata = {'title': 'FooBar'}  # missing category

    resp = test_client.post(
        '/api/articles/',
        data=json.dumps(metadata),
        content_type='application/json',
    )
    assert resp.status_code == 400
