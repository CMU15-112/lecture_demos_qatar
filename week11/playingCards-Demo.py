import random

class PlayingCard(object):
    
    numNames=[None, "Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"]
    suitNames=["clubs", "diamonds", "hearts", "spades"]
    DIAMONDS= 1
    
    @staticmethod
    def getDeck():   
        deck=[]
        
        for s in range(4): #clubs, diamonds, hearts, spades
            for n in range(1, 14): #Ace, 2, 3, ..., 10, Jack, Queen, King
                c= PlayingCard(n, s)
                deck.append(c)
                
        random.shuffle(deck)    
        return deck


    def __init__(self, num, suit):
        self.num= num
        self.suit= suit
        
    def __repr__(self):
        number= PlayingCard.numNames[self.num]
        suit= PlayingCard.suitNames[self.suit]
        return f"{number} of {suit}"
        
        
    def __eq__(self, other):
        return (type(self)== type(other)) and (self.num == other.num) and (self.suit==other.suit)
    
    def __hash__(self):
        return hash( (self.num, self.suit) )
    

############################## FULL DEMO

print()
print("Demo of PlayingCard will keep creating new shuffled decks, and")
print("drawing the first card, until we see the same card twice.")
print()

# Cards:
# number is 1 for Ace, 2...10,
#           11 for Jack, 12 for Queen, 13 for King
# suit is 0 for Clubs, 1 for Diamonds,
#         2 for Hearts, 3 for Spades
  
  
# Now keep drawing cards until we get a duplicate
cardsSeen = set()
diamondsCount = 0

while True:
    deck = PlayingCard.getDeck()
    drawnCard = deck[0]
    if (drawnCard.suit == PlayingCard.DIAMONDS):
        diamondsCount += 1
    print("  drawnCard:", drawnCard) # names of numbers
    if (drawnCard in cardsSeen): break
    cardsSeen.add(drawnCard)

# And then report how many cards we drew
print("Total cards drawn:", 1+len(cardsSeen))
print("Total diamonds drawn:", diamondsCount)


