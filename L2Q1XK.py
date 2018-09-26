'''
Xavier Kidston
3063475
Computer Science 200 - XO2L
Lab 2 - Classes
'''



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
    Purpose: Switching the nominator with the new input
    Parameters: Self - the inside object
                other - outside integer
    Throws: TypeError - input must be an integer
    Pre: user is trying to switch with integer
    Post: the nominator becomes other
    '''
    def set_nom(self, other):
        if isinstance(other, int): self._Frac[0] = other
        else: raise TypeError("Nominator must be an integer.")
        
    
    '''
    Purpose: Switching the denominator with the new input
    Parameters: Self - the inside object
                other - outside integer
    Throws: TypeError - input must be an integer
    Pre: user is trying to switch with integer
    Post: the denominator becomes other
    '''
    def set_den(self, other):
        if isinstance(other, int) and other != 0: self._Frac[1] = other
        else: raise TypeError("Nominator must be an integer.")



