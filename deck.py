import card 
import random

# a deck object that contains all the cards in a deck with associate methods
class Deck():

    def __init__(self):
        self.cards = []


    def newDeck(self):
        self.cards = []
        faces = ["Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"]

        suits = ["Clubs", "Spades", "Hearts", "Diamonds"]

        for suit in suits:

            for face in faces:

                c = card.Card(face, suit)

                self.cards.append(c)

    def shuffle(self):
        random.shuffle(self.cards)

    def deal(self):

        return self.cards.pop()