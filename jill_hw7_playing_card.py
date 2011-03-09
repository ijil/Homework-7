#Jill Lee
#March 6, 2011
#This program randomly generates playing cards for the number of
#times designated by the user.

from random import *

#I used the list and the dictionary to simplify the code by
#eliminating numerous if statements. I call rank names by
#indexing and suit names by calling values to corresponding keys.
ranks=[0,"Ace","Two","Three","Four","Five","Six","Seven",
       "Eight","Nine","Ten","Jack","Queen","King"]
suits={"d":"Diamonds","c":"Clubs","h":"Hearts","s":"Spades"}

class Card:
    
    def __init__(self, rank, suit):
        self.rank=ranks[rank] #indexing; rank is assigned in the
                              #for loop at the bottom.  
        self.suit=suits[suit] #getting values from dictionary
                              #with key 'suit.' suit is assigned
                              #in the for loop at the bottom.        
    def getRank(self):
        return self.rank

    def getSuit(self):
        return self.suit

    def BJValue(self):
        return bj_val  #This variable is assigned in the for loop
                       #at the bottom. 
    def __str__(self):
        return self.rank+" of "+self.suit

n=int(input("How many cards would you like to see? "))

#generating the identity of the cards that will get translated
#into names with class Card
for i in range(n):
    rank=randrange(1,13)        
    suit=choice(["d","c","h","s"])
    if rank<10:
        bj_val=rank
    else:
        bj_val=10

    card=Card(rank,suit)
    print(str(card)+":","Blackjack value is",str(card.BJValue())+".")
