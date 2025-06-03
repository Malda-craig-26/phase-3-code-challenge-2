import pytest
from lib.models.author import Author
from lib.models.magazine import Magazine
from lib.models.article import Article
from lib.db.connection import get_connection

def setup_module(module):
    # Clear all tables before running these tests
    conn = get_connection()
    conn.execute("DELETE FROM articles")
    conn.execute("DELETE FROM authors")
    conn.execute("DELETE FROM magazines")
    conn.commit()
    

def test_author_save_and_find():
    author = Author(name="Jane Doe")
    author.save()
    assert author.id is not None

    found = Author.find_by_id(author.id)
    assert found.name == "Jane Doe"

def test_author_articles():
    author = Author(name="John Writer")
    author.save()

    mag = Magazine(name="Science Monthly", category="Science")
    mag.save()

    article1 = Article(title="The Big Bang", author_id=author.id, magazine_id=mag.id)
    article1.save()
    article2 = Article(title="Quantum Realms", author_id=author.id, magazine_id=mag.id)
    article2.save()

    articles = author.articles()
    assert len(articles) == 2
    titles = [article.title for article in articles]
    assert "The Big Bang" in titles
    assert "Quantum Realms" in titles

def test_author_magazines():
    author = Author(name="Multi-Mag Author")
    author.save()

    mag1 = Magazine(name="Tech Daily", category="Technology")
    mag2 = Magazine(name="Health Weekly", category="Health")
    mag1.save()
    mag2.save()

    article1 = Article(title="AI Revolution", author_id=author.id, magazine_id=mag1.id)
    article2 = Article(title="Healthy Living", author_id=author.id, magazine_id=mag2.id)
    article1.save()
    article2.save()

    magazines = author.magazines()
    assert len(magazines) == 2
    names = [mag.name for mag in magazines]
    assert "Tech Daily" in names
    assert "Health Weekly" in names
