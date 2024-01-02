import sqlite3

class Flashcard:
    
    set_ = None
    term = ''
    definition = ''
    
    def __init__(self, set_, term, definition):
        self.set_ = set_
        self.term = term
        self.definition = definition
        
    def delete(self):
        self.set_.cursor.execute("DELETE FROM flashcards WHERE term = '" + self.term + "' AND definition = '" + self.definition + "'")
        rows_deleted = self.set_.cursor.rowcount
        self.set_.conn.commit()
        print(rows_deleted)
        
    def equals(self, term, definition):
        if self.term == term and self.definition == definition:
            return True
        return False
    
    def insert(self):
        self.set_.cursor.execute("INSERT INTO flashcards VALUES ('" + self.term + "', '" + self.definition + "')")
        self.set_.conn.commit()
    
    def update(self, term, definition):
        self.set_.cursor.execute("UPDATE flashcards SET term = '" + term + "', definition = '" + definition + "' WHERE term = '" + self.term + "' AND definition = '" + self.definition + "'")
        self.set_.conn.commit()