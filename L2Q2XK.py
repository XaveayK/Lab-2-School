'''
Xavier Kidston
3063475
Computer Science 200 - XO2L
Lab 2 - Classes
'''
from random import *



'''
This class creates a deck object with 52 card objects
'''
class deck:
    
    
    '''
    Purpose: Constructor
    Parameters: self - object
                Face - the faces of the cards you want
                Value - the values of the cards you want
    Throws: None
    Pre: That deck object is being created
    Post: Deck object created
    Returns: None
    '''
    def __init__(self, Face = ['C', 'S', 'D', 'H'], \
        Value = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13']):
        Dek = []
        for face in Face:
            for value in Value:
                Dek.append(card(face, value))
        shuffle(Dek)
        self._Deck = Dek
        self._Face = Face
        self._Value = Value
        
        
    '''
    Purpose: To allow for a string representation of the deck with lines of the 
             the length / 4
    Parameters: self - object
    Throws: exception - deck empty
    Pre: the deck is a list of cards
    Post: printed out each individual card left in the deck
    Returns: None
    '''
    def __str__(self):
        count = 0
        strang = ''
        for cards in self._Deck: 
            strang += str(cards) + " "
            count += 1
            if count == (len(self._Deck) // 4):
                if len(self._Deck) / 4 != len(self._Deck) // 4:
                    count = -1
                else:
                    count = 0
                strang += "\n"
        count = 0
        return strang
    
    
    '''
    Purpose: To add to a dictionary from outside of itself
    Parameters: self - inside object
                other - outside object, list, or string
    Throws: Exception - adding to the deck as a string must in form 'C6'
            TypeError - adding to the deck has to be a card object or somethign 
            that looks like a card
    Pre: That the thing you're trying to add to the deck is a card or something 
         that looks like a card, or a list with cards in it
    Post: The added to deck
    Returns: None
    '''
    def __add__(self, other):
        
        
        if isinstance(other, deck): #If the item is a object Deck
            self._Deck += other._Deck #Adds the outside deck to this deck
            other._Deck.clear() #Clears the other deck
        
        
        elif isinstance(other, str): #if the item is a string
            #creates a card object and replaces the string with that object
            if other[0] in self._Face or other[1] in self._Value:
                other = card(other[0], other[1]) #Makes the card object
                self._Deck.append(other) #Adds it to the deck
                
        
        elif isinstance(other, list): #If what you're entering is a list
            x = 0
            while x < len(other): #For the range of the list
                x += 1
                #if the item is a str and only has 2 values
                if isinstance(other[x-1], str) and (len(other[x-1]) >= 2\
                   or len(others[x-1] < 4)): 
                    
                    #makes the item that isnt a card object, a card object
                    if len(other[x-1]) == 2:
                        if other[x-1][0] in self._Face and other[x-1][1] in \
                           self._Value: other[x-1] = card(other[x-1][0], other[x-1][1])
                    elif len(other[x-1]) == 3:
                        if other[x-1][0] in self._Face and other[x-1][1:] in \
                           self._Value: other[x-1] = card(other[x-1][0], other[x-1][1:])
                
                #If the type is card, does nothing
                elif isinstance(other[x-1], card): other[x-1] = other[x-1]
                
                #If it doesn't fit these parameters, raises exception
                else: raise TypeError("Each item in the list must be a card or str for a card")
                
            self._Deck += other #adds other to the deck
            other.clear() #clears the origin if its a list
                
        #Raises type error if the items arent cards or string or list
        else: raise TypeError("Adding to a deck must be a card object, string or" +\
                              " a list with strings and card objects in it.")            

        shuffle(self._Deck)    
                
    
    '''
    Purpose: To create a hand to give to someone
    Parameters: self - object
                cards = the amount of cards you want in your hand
    Throws: exception - deck is empty
    Pre: the deck has cards
    Post: the hand is created
    Returns: The created hand of cards
    '''
    def deal(self, cards = 1):
        hand = [] #Sets hand variable
        for han in range(cards): hand.append(str(self._Deck.pop())) # adds card variable
        return hand #returns the created card variables as a list
   
   
            
'''
This class creates a card object with its face, and the value of the card
'''
class card:
    
    
    '''
    Purpose: Constructor
    Parameters: Face - The face value (Clubs, Spades, Hearts, Diamonds)
                Value - The numerical value assigned to the card (1 through 13)
    Throws: Exception if card isnt in values and preset faces
    Pre: That face and value are both proper
    Post: The card is created
    Returns: None
    '''
    def __init__(self, Face, Value):
        
        VAM = ['1','2','3','4','5','6','7','8','9','10','11','12','13']
        
        if Value.upper() == 'A': Value = '1' #Changes an Ace to 1
        elif Value.upper() == 'J': Value = '11' #changes J to 11
        elif Value.upper() == 'Q': Value = '12' #Changes Q to 12
        elif Value.upper() == 'K': Value = '13' #Changes K to 13
        
        if Value in VAM: #Makes sure value exists
            self._Face = Face #Stores the face of the card for the object
            self._Value = Value #Stores the value of the object
        
        else: raise Exception("Needs to be in the norm for card values (1-13)")
    
    
    '''
    Purpose: To create a string representation of a card
    Parameters: self - object
    Throws: None
    Pre: self._Face and self._Value
    Post: str representation of self._Face and self._Value
    Returns: the str representation of self._Face and self._Value
    '''
    def __str__(self): 
        if self._Value == '1': return str(self._Face + 'A') #Returns FA
        elif self._Value == '11': return str(self._Face + 'J') #Returns FJ
        elif self._Value == '12': return str(self._Face + "Q") #Returns FQ
        elif self._Value == '13': return str(self._Face + 'K') #Returns FK
        else: return str(self._Face + self._Value) #Returns the face with number
    
    
    '''
    Purpose: Checks if the cards values are equal
    Parameters: self - the inside object 
                other - the outside object
    Throws: TypeError - must be a card type or int type
    Pre: Two different cards
    Post: if they are equal
    Returns: True if the values are equal
    '''
    def __eq__(self, other): 
        #Returns true if the values are equal, also allows for compare to int
        if isinstance(other, card): return self._Value == other._Value #checks card
        elif isinstance(other, int): return self._Value == other #checks int
        else: raise TypeError("A card must be compared to another card or int")
        
    
    '''
    Purpose: Checks if the two cards are not equal
    Parameters: self - the inside object
                other - the outside object
    Throws: TypeError
    Pre: two different cards
    Post: if they are unequal
    Returns: True - if the values are unequal
    '''
    def __ne__(self, other): 
        #Returns true if the values arent equal
        if isinstance(other, card): return self._Value != other._Value #checks card
        elif isinstance(other, int): return self._Value != other #checks int
        else: raise TypeError("A card must be compared to another card or int")
        
        
    '''
    Purpose: Checks if self card is greater than other
    Parameters: self - the inside object
                other - the outside object
    Throws: TypeError
    Pre: two different cards
    Post: if self is greater than other
    Returns: True - if the self value greater than other
    '''
    def __gt__(self, other): 
        #Returns true if the value is greater than the outside value
        if isinstance(other, card): return self._Value > other._Value #Checks card
        elif isinstance(other, int): return self._Value > other #checks int
        else: raise TypeError("A card must be compared to another card or int")
    
    
    '''
    Purpose: Checks if self card is greater than or equal to other
    Parameters: self - the inside object
                other - the outside object
    Throws: TypeError
    Pre: two different cards
    Post: if self is greater/equal than other
    Returns: True - if the self value greater/equal than other
    '''
    def __ge__(self, other): 
        #Returns true if the value is greater/equal tghan the outside value
        if isinstance(other, card): return self._Value >= other._Value #checks card
        elif isinstance(other, int): return self._Value >= other #checks int
        else: raise TypeError("A card must be compared to another card or int")
    
    
    '''
    Purpose: Checks if self card is less than other
    Parameters: self - the inside object
                other - the outside object
    Throws: TypeError
    Pre: two different cards
    Post: if self is less than other
    Returns: True - if the self value less than other
    '''
    def __lt__(self, other): 
        #Returns true if the value is less than the outside value
        if isinstance(other, card): return self._Value < other._Value #checks card
        elif isinstance(other, int): return self._Value < other #checks int
        else: raise TypeError("A card must be compared to another card or int")
    
    
    '''
    Purpose: Checks if self card is less than or equal to other
    Parameters: self - the inside object
                other - the outside object
    Throws: TypeError
    Pre: two different cards
    Post: if self is less than or equal to other
    Returns: True - if the self value less than/equal to other
    '''
    def __le__(self, other): 
        #Returns true if the value is less/equal than the outside value
        if isinstance(other, card): return self._Value <= other._Value #checks card
        elif isinstance(other, int): return self._Value <= other #checks int
        else: raise TypeError("A card must be compared to another card or int")
        


def test_decks():
    
    a = deck()
    print("This is the deck of cards with shuffle:")
    print(a)
    x = a.deal(1)
    y = a.deal(1)
    print(x, y, "are our two cards.\nIs x == y?", x == y, "\nAre they unequal?", x != y)
    print()
    print("Both of those cards were dealt into two separate hands. Here is the\
deck now:")
    print(a)
    print()
    print("I'll deal 30 more cards into a single hand so it's easier to notice\
 the reduction in deck number.")
    z = a.deal(30)
    print(a)
    print("Here is the hand they were dealt into:", z)
    print()
    print("I will now add all the hands back to the deck, and display it:")
    a + x
    a + y
    a + z
    print(a)