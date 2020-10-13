import deck
import player
import card
import board
import time

    
# the time package has been imported into this program and used to create short time delays
# these delays help to stop avoid disorientating the player by running through steps faster than they can process them
def main():
    # first there is the greating message 
    print("Hello and welcome to Blackjack")

    # create variable for deck
    play_deck = deck.Deck()

    # user and dealer are declared then added to the gameBoard
    user = player.Player("User")
    dealer = player.Player("Dealer")
    gameBoard = board.Board(dealer, user)

    # create loop to start game
    while True:
        start = input("Would you like to play? Y / N\n")
            
           

        if start.lower() == "y":
            game_on = True
            break
            
        elif start.lower() == "n":
            game_on = False
            break

        else:
            print("Sorry, I didn't catch that\n")
            
    # this is the game loop that will keep going until the user wants to stop playing
    while game_on:
        
        # create cards for play_deck and then shuffle them, this is done every game
        play_deck.newDeck()
        play_deck.shuffle()

        # reset hands of players on the gameboad
        gameBoard.player.hand = []
        gameBoard.dealer.hand = []
        

        
        # deal the cards
        gameBoard.dealer.hit(play_deck.deal())
        gameBoard.dealer.hit(play_deck.deal())
        gameBoard.player.hit(play_deck.deal())
        gameBoard.player.hit(play_deck.deal())

        # creating variable to store dealer card for later
        hidden_card = gameBoard.dealer.hand[1]
        gameBoard.dealer.hand[1] = "X"


        

        print("\nYour current chips balance is " + str(gameBoard.player.chips))

        print("\nUser will go first!\n")
        betting_turn = True
        
        # loop for user to bet chips on the game
        while betting_turn:
            try: 
                
                bet = input("\nWhat would you like to bet? (Type 0 to exit)\n")
                        
                bet_num = int(bet)

                if bet_num == 0 :
                    break

                elif bet_num > gameBoard.player.chips:
                    print("\nYou do not have enough chips to make this bet!\n")
                    
                    
                else:
                    gameBoard.player.bet(bet_num)
                    print("Your bet of " + str(bet_num) + " has been placed")
                    betting_turn = False

            except:

                print("Oops! Something went wrong, please be sure to input a number!")      

        # had to create exit for loop otherwise would never let you not play
        if bet_num == 0:
            
            break
        
        # booleans to keep track of blackjack status and player turn 
        player_blackjack = False
        player_turn = True

        # loop that will continue until the player is bust or ends their turn
        while player_turn:

            gameBoard.display()

            if len(gameBoard.player.hand) == 2 and gameBoard.player.count() == 21:
                print("Player has blackjack!")
                player_turn = False
                player_blackjack = True
                break

            print("\nCurrent hand value is " + str(gameBoard.player.count()))

            move = input("\nWhat would you like to do? Hit / Stick \n")

            # if player hits
            if move.lower() == "hit":

                print("\nPlayer hits\n")
                # declare card variable to print and add to hand
                draw = play_deck.deal()

                print("You drew a " + str(draw))
                gameBoard.player.hit(draw)
                
                print("\nCurrent hand value is " + str(gameBoard.player.count()))

                # check if player is bust
                if gameBoard.player.count() > 21:
                    print("\nPlayer is bust\n")
                    print("Game over! Dealer wins!")
                    player_turn = False
            
            # if player sticks then end turn
            elif move.lower() == "stick":
                print("\nPlayer sticks, end turn!\n")
                player_turn = False

            else:
                print("\nSorry, I didn't catch that\n")

        player_hand = gameBoard.player.count()
    
        dealer_turn = False

        
        
        
        # reveal hidden card of dealer
        gameBoard.dealer.hand[1] = hidden_card

        gameBoard.display()

        time.sleep(1.0)
        # if player has blackjack
        if player_blackjack:

            # if both player and dealer have blackjak then its a draw and bet is returned
            if len(gameBoard.dealer.hand) == 2 and gameBoard.dealer.count() == 21:
                print("\nBoth dealer and player have blackjack!\nPlayer bet is returned\n")

                gameBoard.player.chips += bet_num                

            else:
                # player wins so return winnings based on bet
                gameBoard.player.chips = bet_num * 2 + gameBoard.player.chips
                print("\nYou have won +" + str(bet_num) + " chips!")

        # if only dealer has blackjack then dealer wins 
        elif len(gameBoard.dealer.hand) == 2 and gameBoard.dealer.count() == 21 and player_hand <= 21:
            print("\nDealer has blackjack!\nDealer wins!")

        # if nobody has blackjack and player is not bust then game continues
        elif player_hand <= 21:
            
            dealer_turn = True
            print("\nIt is now the dealers turn")

            
            print("\nDealer's hand value is " + str(gameBoard.dealer.count()) + "\n")
        
        # loop dealers turn until game is resolved
        while dealer_turn:
            time.sleep(2.0)

            

            # first check to see if dealer has gone bust
            if(gameBoard.dealer.count() > 21):
                print("\nDealer has gone bust, player wins!")
                
                # player wins so return winnings based on bet
                gameBoard.player.chips = bet_num * 2 + gameBoard.player.chips
                print("\nYou have won +" + str(bet_num) + " chips!")
                dealer_turn = False
                break
            
            # if dealers hand is same or more than player then dealer wins
            elif player_hand <= gameBoard.dealer.count():
                print("Dealer wins this round!")
                dealer_turn = False
                break
            
            draw = play_deck.deal()

            print("\nDealer deals a " + str(draw))
            gameBoard.dealer.hit(draw)

            # display game board
            gameBoard.display()
            print("\nDealer's hand value is " + str(gameBoard.dealer.count()) + "\n")
           

        # final loop to see if player wants to play again    
        while True:

            if gameBoard.player.chips == 0:
                print("\nYou have run out of chips to bet with!\n")
                game_on = False
                break

            replay = input("\nWould you like to play again? Y / N\n")

            
            if replay.lower() == "y":
                game_on = True
                break
                
            elif replay.lower() == "n":
                game_on = False
                break

            else:
                print("Sorry, I didn't catch that\n")

        
    print("Thank you for playing!")

if __name__ == "__main__":
    main()


