from Flashcard import Flashcard
import random
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
                self.flashcards.append(Flashcard(self, card[0], card[1]))
    
    def getShuffledFlashcards(self):
        flashcards = self.flashcards.copy()
        random.shuffle(flashcards)
        return flashcards
    
    def remove(self, flashcard):
        for f in self.flashcards:
            if f.equals(flashcard.term, flashcard.definition):
                self.flashcards.remove(f)
                f.delete()
    
    def update(self, tuples):
        for i in range(len(tuples)):
            for j in range(i+1, len(tuples)):
                if tuples[i][0] == tuples[j][0] and tuples[i][1] == tuples[j][1]:
                    raise Exception("Cannot add duplicate card '" + tuples[i][0] + "', '" + tuples[i][1] +"'")
        for i in range(len(tuples)):
            try:
                if not self.flashcards[i].equals(tuples[i][0], tuples[i][1]):
                    self.flashcards[i].update(tuples[i][0], tuples[i][1])
            except IndexError:
                if tuples[i][0] != '' and tuples[i][1] != '':
                    newFlashcard = Flashcard(self, tuples[i][0], tuples[i][1])
                    self.flashcards.append(newFlashcard)
                    newFlashcard.insert()