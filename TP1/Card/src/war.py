import card
import sys

class War(object):
    """
    """

    def __init__(self, turns):
        


    def turn(self):
        c1=
        c2=
        print("--------------------- \nfirst play\n")
        print(c1)
        print("second plays")
        print(c2)
        comp = c1.compare(c2)
        if comp < 0 :
            print("second player wins the round")
        elif comp > 0 :
            print("first player wins the round")
        else :
            print("**** war !")

class Player(object)

    def __init__(self, number_card):
        self.cards = []
        for i in range(number_card):
            self.cards.append(Card.random())

    def play_card(self):
        card_to_play = self.cards[0]
        self.cards.remove(0)
        return card_to_play

    def take_card(self, card):
        self.cards.append(card)
        
if __name__ == '__main__':
    War(sys.argv[1])
