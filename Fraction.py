class Fraction:
    __numerator = 0 # private data member
    __denominator = 0 # private data member

    def __lcm(self, other): #private
        # This method will calculate and return LCM(least common multiple) of two numbers
        return (other.__denominator * self.__denominator) / self.__gcd(other.__denominator)

    def __simple(self): #private
        # This method simplifies or reduces the fraction numerator and denominator to least possible values
        x = self.__gcd(self.__numerator)
        self.__numerator = int(self.__numerator / x)
        self.__denominator = int(self.__denominator / x)
        return self

    def __gcd(self, y): #private
        # This method will calculate and return GCD(greatest common divisor) of two numbers
        x = self.__denominator
        if x < y:
            x, y = y, x
        while y:
            x, y = y, (x % y)
        return x

    def __init__(self, numerator=1, denominator=1): #constructor
        # This is a constructor to assign values of numerator and denominator of a fraction object
        if denominator == 0:
            raise TypeError("Denominator can't by zero")
        self.__numerator = numerator
        self.__denominator = denominator

    def __str__(self): #executed with print statement
        # This method will define how to print an object of this class
        return f"({self.__numerator}/{self.__denominator})"

    def __add__(self, other): #executed with '+' operator
        # This method has definition to add two objects of this class
        x = self.__lcm(other)
        return Fraction((self.__numerator * x) / self.__denominator + (other.__numerator * x) / other.__denominator,
                        x).__simple()

    def __sub__(self, other): #executed with '-' operator
        # This method has definition to subtract two objects of this class
        x = self.__lcm(other)
        return Fraction((self.__numerator * x) / self.__denominator - (other.__numerator * x) / other.__denominator,
                        x).__simple()

    def __mul__(self, other): #executed with '*' operator
        # This method has definition to multiply two objects of this class
        return Fraction(self.__numerator * other.__numerator, self.__denominator * other.__denominator).__simple()

    def __truediv__(self, other): #executed with '/' operator
        # This method has definition to divide two objects of this class
        return Fraction(self.__numerator * other.__denominator, self.__denominator * other.__numerator).__simple()

    def __eq__(self, other): #executed with '==' operator
        # This method has definition to check whether two objects of this class are same
        if (self.__numerator / self.__denominator) == (other.__numerator / other.__denominator):
            return True
        else:
            return False

    def __ge__(self, other): #executed with '>=' operator
        # This method has definition to check whether first object is greater than or equal to second object of this class
        if (self.__numerator / self.__denominator) >= (other.__numerator / other.__denominator):
            return True
        else:
            return False

    def __gt__(self, other): #executed with '>' operator
        # This method has definition to check whether first object is greater than second object of this class
        if (self.__numerator / self.__denominator) > (other.__numerator / other.__denominator):
            return True
        else:
            return False

    def __le__(self, other): #executed with '<=' operator
        # This method has definition to check whether first object is lesser than or equal to second object of this class
        if (self.__numerator / self.__denominator) <= (other.__numerator / other.__denominator):
            return True
        else:
            return False

    def __lt__(self, other): #executed with '<' operator
        # This method has definition to check whether first object is lesser than second object of this class
        if (self.__numerator / self.__denominator) < (other.__numerator / other.__denominator):
            return True
        else:
            return False
