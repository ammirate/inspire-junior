from scraper.parser import ArticleParser


def test_parse_articles_one_article():
    html = """
          <div class="post mb-3">
            <h2 class="post-title">CP Violation in the Renormalizable Theory of Weak Interaction</h2>
            <p class="post-description">In a framework of the renormalizable theory of weak interaction, problems of CP-violation are studied. It is concluded that no realistic models of CP-violation exist in the quartet scheme without introducing any other new fields. Some possible models of CP-violation are also discussed.</p>
            <div class="post-categories">
                <span class="post-category badge badge-pill badge-primary">hep-ph</span>
            </div>
          </div>
    """
    expected = [{
        'title': 'CP Violation in the Renormalizable Theory of Weak Interaction',
        'abstract': 'In a framework of the renormalizable theory of weak interaction, problems of CP-violation are studied. It is concluded that no realistic models of CP-violation exist in the quartet scheme without introducing any other new fields. Some possible models of CP-violation are also discussed.',
        'category': 'hep-ph'
    }]
    parser = ArticleParser()
    result = parser.parse_articles(html)
    assert result == expected


def test_parse_articles_two_articles():
    html = """
          <div class="post mb-3">
            <h2 class="post-title">CP Violation in the Renormalizable Theory of Weak Interaction</h2>
            <p class="post-description">In a framework of the renormalizable theory of weak interaction, problems of CP-violation are studied. It is concluded that no realistic models of CP-violation exist in the quartet scheme without introducing any other new fields. Some possible models of CP-violation are also discussed.</p>
            <div class="post-categories">
                <span class="post-category badge badge-pill badge-primary">hep-ph</span>
            </div>
          </div>
          
          <div class="post mb-3">
            <h2 class="post-title">Review of Particle Physics</h2>
            <p class="post-description">TheReviewsummarizes much of particle physics and cosmology</p>
            <div class="post-categories">
                <span class="post-category badge badge-pill badge-primary">hep</span>
            </div>
          </div>
    """
    expected = [
        {
            'title': 'CP Violation in the Renormalizable Theory of Weak Interaction',
            'abstract': 'In a framework of the renormalizable theory of weak interaction, problems of CP-violation are studied. It is concluded that no realistic models of CP-violation exist in the quartet scheme without introducing any other new fields. Some possible models of CP-violation are also discussed.',
            'category': 'hep-ph'
        },
        {
            'title': 'Review of Particle Physics',
            'abstract': 'TheReviewsummarizes much of particle physics and cosmology',
            'category': 'hep'
        }
    ]
    parser = ArticleParser()
    result = parser.parse_articles(html)
    assert result == expected


def test_parse_articles_no_articles():
    html = """"""
    expected = []

    parser = ArticleParser()
    result = parser.parse_articles(html)

    assert result == expected
