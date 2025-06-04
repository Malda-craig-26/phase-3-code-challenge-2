from lib.db.connection import get_connection



class Article:
    def __init__(self, id=None, title=None, author_id=None, magazine_id=None, content=""):
        self.id = id
        self.title = title
        self.author_id = author_id
        self.magazine_id = magazine_id
        self.content = content

    def save(self):
        conn = get_connection()
        cursor = conn.cursor()
        if self.id is None:
            cursor.execute(
                "INSERT INTO articles (title, author_id, magazine_id, content) VALUES (?, ?, ?, ?)",
                (self.title, self.author_id, self.magazine_id, self.content),
            )
            self.id = cursor.lastrowid
        else:
            cursor.execute(
                "UPDATE articles SET title = ?, author_id = ?, magazine_id = ?, content = ? WHERE id = ?",
                (self.title, self.author_id, self.magazine_id, self.content, self.id),
            )
        conn.commit()
        


    @classmethod
    def find_by_id(cls, id):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM articles WHERE id = ?", (id,))
        row = cursor.fetchone()
        if row:
            return cls(
                id=row["id"],
                title=row["title"],
                author_id=row["author_id"],
                magazine_id=row["magazine_id"]
            )
        return None
    @classmethod
    def find_by_title(cls,title):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM articles WHERE title = ?", (title,))
        row = cursor.fetchone()
        if row:
            return cls(
                title=row["title"],
                author_id=row["author_id"],
                magazine_id=row["magazine_id"]
            )
        return None
    


       

        
