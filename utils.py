

"""
This class is a calculator that performs arithmatic oparation on two numbers.

complete methods below and add missing methods according to the tests.

"""
class Calculator():
    """rounding_digits is a default value by which 
    the calculator rounds off numbers 10/3 = 3.3333333333...
    if rounding_digits = 2 the answer for this expression is 3.33  
    """
    rounding_digits = 0
    
    def __init__(self,round_digits):
        self.rounding_digits = round_digits
       
        
    def addtion(self,a,b):
        sum = round(a + b, self.rounding_digits)
        return sum

    def subtraction(self,a,b):
        subtract = round(a - b,  self.rounding_digits)
        return subtract

    def multiplication(self,a,b):
        multiply = round(a * b, self.rounding_digits)
        return multiply
    
    def division(self,a,b):
        divide = round(a / b,self.rounding_digits)
        return divide
    

    @property
    def round_digits(self):
        return self.rounding_digits

    def set_ound_digits(self,digits):
        self.rounding_digits = digits

calc0 = Calculator(0)  
calc2 = Calculator(2)
print(calc0.addtion(5, 3))
print(calc2.subtraction(5.555, 2.222),)
print(calc2.multiplication(2.345, 3.456))
print(calc2.division(10, 3))
        
    
class History():
    filepath_ = "History.txt"
    
    def __init__(self, filepath):
        self.filepath_ = filepath
        
    
    def save(self,expression:str):
        with open(self.filepath_, "a") as f:
            f.write(expression + "\n")

    
    def restore(self)->list[str]:
        list_1 = []
        with open(self.filepath_, "r") as f:

            for line in f:
                lines = line.strip()
                list_1.append(lines)
            return list_1


    def clear(self):
        with open(self.filepath_, "w") as f:
            pass 
           