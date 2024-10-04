import sqlite3


class Database:
    def __init__(self):
        self.db = sqlite3.connect("database2.db")
        self.cursor = self.db.cursor()

    def create_table(self):
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS jokes(
            joke1 VARCHAR(255)
        )
        """)
        self.db.commit()

    def insert(self, joke1):
        self.cursor.execute("""
            INSERT OR IGNORE INTO jokes (joke1)
            VALUES (?)
        """, (f"{joke1}",))
        self.db.commit()

    def select(self):
        data = self.cursor.execute("""
        SELECT * FROM jokes
        """)
        return data.fetchall()

    def delete(self):
        self.cursor.execute("""
        DELETE FROM jokes
        WHERE joke = 'Поймал старик золотую рыбку. — Отпусти меня, старче, три желания исполню! — Зашибись! — сказал старик. И зашиблась бедная рыбка, так и не исполнив два другие желания.'
        """)
        self.db.commit()

    def drop(self):
        self.cursor.execute("""
        DROP TABLE jokes
        """)
        self.db.commit()

    def project_close(self):
        self.db.close()
