Phase-3-code-challenge:Articles and Magazines.
Project Overview
The application demonstrates:

Object-oriented programming (OOP)

One-to-many and many-to-many relationships

Raw SQL for persistence

Model methods for querying and data manipulation

🗂️ Models
🖊️ Author
name: Name of the author

id: primary key

Methods:
save()

articles() – returns all articles by this author

magazines() – returns all magazines this author has written for

add_article(magazine, title) – creates and saves an article

📰 Article
title: Title of the article

author_id: Foreign key to Author

magazine_id: Foreign key to Magazine

Class Methods:
Article.find_by_title(title)

🗞️ Magazine
name: Name of the magazine

category: Category of the magazine

Methods:
save()

contributors() – returns all authors who have written for this magazine

article_titles() – returns all article titles for this magazine

contributing_authors() – returns authors with more than 2 articles in this magazine

✅ Features
Create and manage authors, articles, and magazines

Raw SQL backend for direct database manipulation

Methods for complex relationships

Test suite using pytest

