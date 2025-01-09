#!python3
"""
Compound Interest Calculator
Create a class object that accepts paramters for Principal, Annual Interest Rate, Number of compounding periods.  
Create a class method that calculates the amount of compound interest for a given length of time.

Extension: accept time given in different measurements, but convert them to years for use in your class template.
    length = 0
    width = 0
    height = 0

    def __init__(self,l=0,w=0,h=0):
        # note you will need to specify more input parameters
            self.length = l
            self.height = w
            self.width = h
            self.volume()
            self.surfaceArea()


    def volume(self):
        V = self.length * self.width * self.height
        if V == 0:
            V = None
        return V
    
    def surfaceArea(self):
        SA = self.length * self.width * 2 + self.width * self.height * 2 + self.length * self.height * 2
        if self.length == 0 or self.width == 0 or self.height == 0:
            SA = None
        return SA

"""


class Calc:
    principal = 0
    rate = 0
    nPeriods = 0

    def __init__(self,P=0,r=0,n=0,t=0):
        self.principal = P
        self.rate = r / 100
        self.nPeriods = n
        self.interest(t)
        self.amount(t)
        #more input parameters needed
        return

    def interest(self,t):
        self.Amt = self.principal * (1 + self.rate / self.nPeriods) ** (self.nPeriods * t)
        self.Int = self.Amt - self.principal
        self.Int = round(self.Int,2)
        return self.Int
    
    def amount(self,t):
        self.Amt = self.principal * (1 + self.rate / self.nPeriods) ** (self.nPeriods * t)
        self.Amt = round(self.Amt,2)
        return self.Amt

a = Calc(P=1000,r=4,n=2)
assert a.interest(3) == 126.16
assert a.amount(5) == 1218.99

b = Calc(P=5000,r=5.25,n=12)
assert b.interest(10) == 3442.62

