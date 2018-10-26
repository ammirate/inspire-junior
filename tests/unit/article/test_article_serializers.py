from backend.articles.serializers import ArticleSchema
from backend.articles.models import Article


def test_article_schema():
    article = Article(
        title='Partial Symmetries of Weak Interactions',
        category_id=1,
    )
    expected_json = {
        'category_id': 1,
        'abstract': '',
        'id': 0,
        'title': 'Partial Symmetries of Weak Interactions'
    }
    serialized_data = ArticleSchema().dump(article).data
    assert serialized_data == expected_json
