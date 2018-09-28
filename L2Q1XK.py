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
    def __init__(self, num = None, den = None):
        Frac = [] #Sets up frac for later use
        Sign = '+'
        if isinstance(num, str): #If the user tryna enter a str
            num = num.replace(" ", "") #Replaces all spaces with empty
            if num[0] == '-': #Checks if num is negative 
                Sign = num[0] #Adds the sign
                num = num[1:] #Creates the new string
            if num[0].isdigit() and num[-1].isdigit(): # Makes sure it's a frac
                num = num.split("/") #Allows for the user to input the fraction as str
                den = int(num[1]) #Makes denominator
                num = int(num[0]) #Makes numerator
        if num == None or den == None: raise Exception("Must be two inputs") #input == 2
        if den == 0: raise Exception("Denominator must not be 0") #Den == 0
        Frac.append(num) #Appends numerator to the object list
        Frac.append(den) #Appends denominator to the object list
        if Sign == '-': value = -(num / den) #Gets value for negative
        elif Sign == '+': value = num / den #Gets value for positive
        self._value = value #Creates the value in the object
        self._frac = Frac #Creates the fraction in the object
    
    
    '''
    Purpose: overloads __str__, so that it can be called to be printed
    Parameters: Self
    Returns: the fraction in a string in the form of x/y
    '''
    def __str__(self): 
        if self._value < 0.0: #If the value is negative, just displays it as such
            return "-" + str(self._frac[0]) + "/" + str(self._frac[1])
        if self._value >= 0.0: return str(self._frac[0]) + "/" + str(self._frac[1])
    
    
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
        #Makes sure the user switch is an int or str
        if isinstance(other, int): self._Frac[0] = other
        if isinstance(other, str) and other.isdigit(): self._Frac[0] = other
        else: raise TypeError("Nominator must be an integer or str of digits.")
        
    
    '''
    Purpose: Switching the denominator with the new input
    Parameters: Self - the inside object
                other - outside integer
    Throws: TypeError - input must be an integer
    Pre: user is trying to switch with integer
    Post: the denominator becomes other
    '''
    def set_den(self, other):
        #Makes sure the user switch is an int or str
        if isinstance(other, str) and other.isdigit() and int(other) != 0: self._Frac[1]=other
        if isinstance(other, int) and other != 0: self._Frac[1] = other
        else: raise TypeError("denominator must be an integer or str of digits.")
    
    
'''
Purpose: To test my Fraction class
'''
def test_frac():
    frac1 = Fraction(1, 2) #Shows it works with int inputs
    #I just did this one to show the robust nature of my constructor
    frac2 = Fraction("   4   /  2          ")
    frac3 = Fraction("6 / 3") # Shows it works under normal conditions
    print("Here are our three fractions:")
    print(frac1)
    print(frac2)
    print(frac3)
    