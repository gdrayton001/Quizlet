from Flashcard import Flashcard
import sqlite3

class Set:
    
    conn = None
    cursor = None
    flashcards = []
    
    def __init__(self, name):
        self.conn = sqlite3.connect(name + '.db')
        self.cursor = self.conn.cursor()
        self.flashcards = []
        try:
            self.cursor.execute("CREATE TABLE flashcards (term text, definition text)")
        except sqlite3.OperationalError:
            self.cursor.execute("SELECT * FROM flashcards;")
            cards = self.cursor.fetchall()
            for card in cards:
                self.flashcards.append(Flashcard(card[0], card[1]))