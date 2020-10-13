import card

class Player():

    def __init__(self, name):
        self.name = name
        self.hand = []
        self.chips = 10
   
    
    def hit(self, item):
        self.hand.append(item)

    def valueCalc(self):

        li = [0] * len(self.hand)
        

        

        return li        

    def count(self):

        # if the hand is empty then value is 0
        if not self.hand:
            return 0

        count = 0
        aces = 0

        royal = ['jack', 'queen', 'king']
        
        # calculate the value of the hand in for loop
        for index in range(len(self.hand)):    
            face = self.hand[index].face
            
            # value of royal card is 10
            if face.lower() in royal:
                count += 10

            # value of ace is initally 11
            elif face.lower() == "ace":
                count += 11
                aces += 1

            # else convert value to integer
            else:
                count += int(face)

        # if the count is more than 21 and there is an ace then adjust
        if count > 21 and aces > 0:
            counter = aces
         
            # loop for number of aces there are
            for _ in range(counter):
                count -= 10
                aces -= 1

                if count <= 21:
                    break
                 
        return count       

           
    def bet(self, number):

        self.chips = self.chips - number

    def win(self, number):
        self.chips += number    