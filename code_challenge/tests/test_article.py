import pytest
from lib.models.article import Article
from lib.models.author import Author
from lib.models.magazine import Magazine
from lib.db.connection import get_connection

def setup_module(module):
    conn = get_connection()
    conn.execute("DELETE FROM articles")
    conn.execute("DELETE FROM authors")
    conn.execute("DELETE FROM magazines")
    conn.commit()
    

def test_article_save_and_find():
    author = Author(name="Test Author")
    author.save()

    mag = Magazine(name="Test Magazine", category="General")
    mag.save()

    article = Article(title="Test Article", author_id=author.id, magazine_id=mag.id)
    article.save()

    found = Article.find_by_id(article.id)
    assert found.title == "Test Article"
    assert found.author_id == author.id
    assert found.magazine_id == mag.id
