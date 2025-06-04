from lib.models.author import Author
from lib.models.magazine import Magazine
from lib.models.article import Article

def seed_data():
    author1 = Author(name="Alice Writer")
    author1.save()
    author2 = Author(name="Bob Reporter")
    author2.save()

    mag1 = Magazine(name="Tech Times", category="Technology")
    mag1.save()
    mag2 = Magazine(name="Health Weekly", category="Health")
    mag2.save()

    a1 = Article(title="AI in 2025", author_id=author1.id, magazine_id=mag1.id)
    a1.save()
    a2 = Article(title="Mental Wellness", author_id=author2.id, magazine_id=mag2.id)
    a2.save()
    a3 = Article(title="Smart Gadgets", author_id=author1.id, magazine_id=mag1.id)
    a3.save()

    print("Seed data inserted successfully.")

if __name__ == "__main__":
    seed_data()
