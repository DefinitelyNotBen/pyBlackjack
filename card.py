# Class for cards that contain attributes for value, face, and suit
class Card():

    def __init__(self, face, suit):

        self.face = face
        self.suit = suit

    def __repr__(self):

        return self.face + " of " + self.suit

    def __str__(self):

        return self.face + " of " + self.suit

  

     