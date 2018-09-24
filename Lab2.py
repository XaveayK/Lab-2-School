'''
Xavier Kidston
3063475
Computer Science 200 - XO2L
Lab 2 - Classes
'''
from random import *



'''
This is a basic fraction object, it'll store information in a list [num][den]
and then when the object is called to __str__ it'll display "num / den"
'''
class Fraction:
    
    
    '''
    Purpose: Constructor
    Parameters: Self, frac
    Throws: Letter Exception
            denominator exception
    Pre: num and den are numbers
    Post: Objects created
    '''
    def __init__(self, num, den):
        Frac = []
        value = float
        if num == None or den == None: raise Exception("Must be two inputs") #input == 2
        if den == 0: raise Exception("Denominator must not be 0")
        Frac.append(num) #Appends numerator to the object list
        Frac.append(den) #Appends denominator to the object list
        value = num / den #Gets the value for the fraction
        self._value = value #Creates the value in the object
        self._frac = Frac #Creates the fraction in the object
    
    
    '''
    Purpose: overloads __str__, so that it can be called to be printed
    Parameters: Self
    Returns: the fraction in a string in the form of x/y
    '''
    def __str__(self): return str(self._frac[0]) + "/" + str(self._frac[1])
    
    
    '''
    Purpose: Overloads __add__ to allow for fraction addition, and returns
             a new fraction object
    Parameters: self - local fraction object
                Other - fraction object
    Throws: TypeError if other object isnt fraction
    Pre: Two fraction objects
    Post: A fraction adding to another fraction
    Returns: A new fraction object
    '''
    def __add__(self, other):
        
        #Ensures other is a fraction object
        if isinstance(other, Fraction) == False:
            raise TypeError("Object you add must be type Fraction")
        
        #Adds the fraction if denominators are equal
        if self._frac[1] == other._frac[1]: 
            return Fraction((self._frac[0] + other._frac[0]), self._frac[1])
        
        #Adds the fraction if denominators are unequal
        else: return Fraction((self._frac[0] * other._frac[1]) + (other._frac[0]\
                * self._frac[1]), (self._frac[1] * other._frac[1]))
    
    
    '''
    Purpose: Overloads __sub__ to allow for fraction subtraction, and returns 
             a new fraction object
    Parameters: self - local fraction object
                other - fraction object
    Throws: TypeError if other object isnt fraction
    Pre: Two fraction objects
    Post: A fraction minus another fraction
    Returns: A new fraction object
    '''
    def __sub__(self, other):
        
        #Ensures other is a Fraction object
        if isinstance(other, Fraction) == False:
            raise TypeError("Object you subtract must be type Fraction")
        
        #subtracts the fraction if denominators are equal
        if self._frac[1] == other._frac[1]: 
            return Fraction(self._frac[0] - other._frac[0], self._frac[1])
        
        #Subtracts the fractions if denominators are unequal
        else: return Fraction((self._frac[0] * other._frac[1])-(other._frac[0]\
                * self._frac[1]), (self._frac[1] * other._frac[1]))
    
    
    '''
    Purpose: Overloads __mul__ (*) to allow for fraction division, and returns
             a new fraction object
    Parameters: self - local fraction object
                other - fraction object
    Throws: TypeError if other object isnt fraction
    Pre: Two fraction objects
    Post: A fraction multiplied by another fraction
    Returns: A new fraction object
    '''
    def __mul__(self, other): 
        
        #checks to make sure other is Fraction
        if isinstance(other, Fraction) == False:
            raise TypeError("Object you multiply must be type Fraction")
        
        return Fraction(self._frac[0] * other._frac[0],\
                    self._frac[1] * other._frac[1]) # Multiplies the fraction
    
    
    '''
    Purpose: Overloads __truediv__ (/) to allow for fraction division and
             returns a new fraction object
    Parameters: self - local fraction object
                other - fraction object
    Throws: TypeError if other object isnt fraction
    Pre: Two fraction objects
    Post: A fraction divided by another fraction
    Returns: A new fraction object
    '''
    def __truediv__(self, other): 
        
        #Checks to make sure other is Fraction 
        if isinstance(other, Fraction) == False:
            raise TypeError("Object you divide by must be type Fraction")
        
        return Fraction(self._frac[0] * other._frac[1],\
                    self._frac[1] * other._frac[0]) #Divides the fraction
    
    
    '''
    Purpose: To check if the two fractions are equal to eachother
    Parameters: self - local fraction object
                other - fraction object
    Throws: TypeError if other object isnt fraction
    Pre: Two fraction objects
    Post: Compared fractions
    Returns: True or False dependant on the condition being met
    '''
    def __eq__(self, other):
        
        #Checks to make sure other is Fraction 
        if isinstance(other, Fraction) == False:
            raise TypeError("Object you divide by must be type Fraction")     
        
        #Checks to see if local object is equal to other object
        if self._value == other._value:
            return True
        else:
            return False        
    
    
    '''
    Purpose: To check if the fraction is less than the local object
    Parameters: self - local fraction object
                other - fraction object
    Throws: TypeError if other object isnt fraction
    Pre: Two fraction objects
    Post: Compared fractions
    Returns: True or False dependant on the condition being met
    '''
    def __lt__(self, other):
        
        #Checks to make sure other is Fraction 
        if isinstance(other, Fraction) == False:
            raise TypeError("Object you divide by must be type Fraction")    
        
        #checks to see if local object is less than other object
        if self._value < other._value:
            return True
        else:
            return False        
    
    
    '''
    Purpose: To check if the two fractions are unequal
    Parameters: self - local fraction object
                other - fraction object
    Throws: TypeError if other object isnt fraction
    Pre: Two fraction objects
    Post: Compared fractions
    Returns: True or False dependant on the condition being met
    '''
    def __ne__(self, other):
        
        #Checks to make sure other is Fraction 
        if isinstance(other, Fraction) == False:
            raise TypeError("Object you divide by must be type Fraction")  
        
        #checks to see if local object is not equal to other object
        if self._value != other._value:
            return True
        else:
            return False        
    
    
    '''
    Purpose: To check if the object is less than or equal to local object
    Parameters: self - local fraction object
                other - fraction object
    Throws: TypeError if other object isnt fraction
    Pre: Two fraction objects
    Post: Compared fractions
    Returns: True or false dependant on the condition being met
    '''
    def __le__(self, other):
        
        #Checks to make sure other is Fraction 
        if isinstance(other, Fraction) == False:
            raise TypeError("Object you divide by must be type Fraction")    
        
        #Checks to see if local object is less than or equal to other object
        if self._value <= other._value:
            return True
        else:
            return False        
    
    
    '''
    Purpose: To check if the object is greater than the local object
    Parameters: self - local fraction object
                other - fraction object
    Throws: TypeError if other object isnt fraction
    Pre: Two fraction objects
    Post: Compared fractions
    Returns: True or false dependant on the condition being met
    '''
    def __gt__(self, other):
        
        #Checks to make sure other is Fraction 
        if isinstance(other, Fraction) == False:
            raise TypeError("Object you divide by must be type Fraction")   
        
        #Checks to see if local object is greater than other object
        if self._value > other._value:
            return True
        else:
            return False
    
    
    '''
    Purpose: To check if the object is greater than or equal to the local object
    Parameters: self - local fraction object
                other - fraction object
    Throws: TypeError if other object isnt fraction
    Pre: Two fraction objects
    Post: Compared fractions
    Returns: True or False dependant on the condition being met
    '''
    def __ge__(self, other):
        
        #Checks to make sure other is Fraction 
        if isinstance(other, Fraction) == False:
            raise TypeError("Object you divide by must be type Fraction")
        
        #checks to see if local object is greater than or equal to other object
        if self._value >= other._value:
            return True
        else:
            return False



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
        Value = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']):
        Dek = []
        for face in Face:
            for value in Value:
                Dek.append(card(face, value))
        shuffle(Dek)
        self._Deck = Dek
        self._Face = face
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
         that looks like a card
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
                other = card(other[0], other[1])
                self._Deck.append(other)
                
        
        elif isinstance(other, list): #If what you're entering is a list
            for cards in range(len(other)): #For the range of the list
                
                #if the item is a str and only has 2 values
                if isinstance(other[cards], str) and len(other[cards]) == 2: 
                    
                    #makes the item that isnt a card object, a card object
                    if other[cards][0] in self._Face or other[cards][1] \
        in self._Value: other[cards] = card(other[cards][0], other[cards][1])
                    
                    #If it doesn't fit these parameters, raises exception
                    else: raise Exception("Face and Value must be in the decks range")
                
                elif isinstance(cards, card): pass #If the type is card, does nothing
            self._Deck += other
            other.clear()            
                
        #Raises type error if the list items arent cards or string
        else: raise TypeError("Adding to a deck must be a card object, string or\
a list with strings and card objects in it.")            

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
        hand = []
        for han in range(cards): hand.append(str(self._Deck.pop()))
        return hand
   
   
            
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
        if Value in 'A2345678910JQK':
            self._Face = Face
            self._Value = Value
        else: raise Exception("Needs to be in the norm for card values (A-K)")
    
    
    '''
    Purpose: To create a string representation of a card
    Parameters: self - object
    Throws: None
    Pre: self._Face and self._Value
    Post: str representation of self._Face and self._Value
    Returns: the str representation of self._Face and self._Value
    '''
    def __str__(self): return str(self._Face + self._Value) #The string value
    
    
    '''
    Purpose: Checks if the cards values are equal
    Parameters: self - the inside object 
                other - the outside object
    Throws: TypeError - must be a card type
    Pre: Two different cards
    Post: if they are equal
    Returns: True if the values are equal
    '''
    def __eq__(self, other): 
        if isinstance(other, card): return self._Value != other._Value
        else: raise TypeError("A card must be compared to another card")
        
    
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
        if isinstance(other, card): return self._Value != other._Value
        else: raise TypeError("A card must be compared to another card")
        
        
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
        if isinstance(other, card): return self._Value > other._Value 
        else: raise TypeError("A card must be compared to another card")
    
    
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
        if isinstance(other, card): return self._Value >= other._Value
        else: raise TypeError("A card must be compared to another card")
    
    
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
        if isinstance(other, card): return self._Value < other._Value
        else: raise TypeError("A card must be compared to another card")
    
    
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
        List = 'A_________JQK' 
        if self._Value == 'A': x = 1
        if other._Value == 'A': y = 1
        if isinstance(other, card): return self._Value <= other._Value
        else: raise TypeError("A card must be compared to another card")
        


def test_decks():
    
    #Sets up the decks for testing
    a = deck()
    b = deck()
    c = deck()
    
    #Runs through checks for the deck and 
    print("This is the current deck:")
    print(a)
    hand1 = a.deal(5)
    hand2 = a.deal(5)
    print("Dealing two 5 card hands.....")
    print()
    print("Hand 1 is:", hand1)        
    hand1.append('C6')
    hand1.append('S8')    
    print("Hand 2 is:", hand2)
    print("Manually added two strings to hand1:", hand1)
    print()
    print("Now adding hand 1 to the deck.....")
    a + hand1
    print("Hand 1 after adding it to the deck:", hand1)
    print("Deck after adding hand1 to it and shuffling:\n")
    print(a)
    print("Creating a second deck.....")
    print(b)
    print("Adding hand2 to the second deck...")
    b + hand2
    print("This is now deck b:")
    print()
    print(b)
    b + 'C8'
    print()
    print("Adding C8 directly to deck b:")
    print()
    print(b)
    