import player

class Board():

    def __init__(self, dealer, player):
        self.dealer = dealer
        self.player = player

    
    def display(self):

        dHand = ""
        pHand = ""

        for card in self.dealer.hand:
            dHand += "| "
            dHand += str(card)
            dHand += " |"

        for card in self.player.hand:
            pHand += "| "
            pHand += str(card)    
            pHand += " |"

        print("Dealer: " + dHand + "\n\n\n" + "Player: " + pHand)