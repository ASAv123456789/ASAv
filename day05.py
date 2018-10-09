'''
class Rectangle:
    def __init__(self,width,height):
        self.width=width
        self.height=height
    def getArea(self):
        res=self.width*self.height
        print(self.width,self.height,res)
    def getPerimeter(self):
        res2=2*(self.width+self.height)
        print(res2)
Rectangle(4,40).getArea()
Rectangle(4,40).getPerimeter()
Rectangle(3.5,35.7).getArea()
Rectangle(3.5,35.7).getPerimeter()
'''
'''
class Account:
    def __init__(self,a,b,annuallnterestRate):
        self.__id=int(a)
        self.__balance=float(b)
        self.__annuallnterestRate=float(annuallnterestRate)
    def getMonthlyInterestRate(self):
        monthlyInterestRate=self.__annuallnterestRate/100/12
        return monthlyInterestRate
    def getMonthlyInterest(self):
        monthlyInterest=self.__balance*Account.getMonthlyInterestRate(self)
        return monthlyInterest
    def withdraw(self,c):
        self.__balance=self.__balance-c
    def deposit(self,d):
        self.__balance=self.__balance+d
    def pr(self):
        print(self.__id,self.__balance,Account.getMonthlyInterestRate(self),Account.getMonthlyInterest(self))
Account1=Account(1122,20000,4.5)
Account1.withdraw(2500)
Account1.deposit(3000)
Account1.pr()
'''
'''
class Fan:
    def __init__(self,a,b,c,d):
        self.__speed=int(a)
        SLOW=1
        MEDIUM=2
        FAST=3
        if self.__speed==SLOW:
            self.__speed='SLOW'
        elif self.__speed==MEDIUM:
            self.__speed='MEDIUM'
        elif self.__speed==FAST:
            self.__speed='FAST'
        self.__on=bool(b)
        self.__radius=float(c)
        self.__color=str(d)
    def pr(self):
        print(self.__speed,self.__radius,self.__color,self.__on)
Fan1=Fan(3,1,10,'yellow')
Fan1.pr()
Fan2=Fan(2,0,5,'blue')
Fan2.pr()
'''
'''
import math

class LinearEquation:
    def __init__(self,a,b,c,d,e,f):
        self.__a=a
        self.__b=b
        self.__c=c
        self.__d=d
        self.__e=e
        self.__f=f
    
    def isSolvable(self):
        if (self.__a*self.__d-self.__b*self.__c)!=0:
            return True

    def getX(self):
        x=(self.__e*self.__d-self.__b*self.__f)/(self.__a*self.__d-self.__b*self.__c)
        return x
    
    def getY(self):
        y=(self.__a*self.__f-self.__e*self.__c)/(self.__a*self.__d-self.__b*self.__c)
        return y
    
a,b,c,d,e,f=eval(raw_input('Enter a,b,c,d,e,f:'))
m=LinearEquation(a,b,c,d,e,f)
if m.isSolvable()!=True:
    print('The equation has on solution')
else:
    print('x is '+str(m.getX())+' and '+'y is '+str(m.getY()))
'''
'''
import math

class RegularPolygon:
    def __init__(self,n=3,side=1,x=0,y=0):
        self.__n=n
        self.__s=side
        self.__x=x
        self.__y=y

    def getPerimeter(self):
        p=self.__n*self.__s
        print('Perimeter:'+str(p))

    def getArea(self):
        a=(self.__n*self.__s**2)/(4*math.tan(math.pi/self.__n))
        print('Area:'+str(a))

print('--------1--------')
RegularPolygon().getPerimeter()
RegularPolygon().getArea()
print('--------2--------')
RegularPolygon(6,4).getPerimeter()
RegularPolygon(6,4).getArea()
print('--------3--------')
RegularPolygon(10,4,5.6,7.8).getPerimeter()
RegularPolygon(10,4,5.6,7.8).getArea()
'''
'''
import math

class LinearEquation:
    def __init__(self,a,b,c,d,e,f):
        self.__a=a
        self.__b=b
        self.__c=c
        self.__d=d
        self.__e=e
        self.__f=f

    def isSolvable(self):
        if (self.__a*self.__d-self.__b*self.__c)!=0:
            return True

    def getX(self):
        x=(self.__e*self.__d-self.__b*self.__f)/(self.__a*self.__d-self.__b*self.__c)
        return x

    def getY(self):
        y=(self.__a*self.__f-self.__e*self.__c)/(self.__a*self.__d-self.__b*self.__c)
        return y

x1,y1,x2,y2=eval(raw_input('Enter the endpoints of the first line segment:'))
x3,y3,x4,y4=eval(raw_input('Enter the endpoints of the second line segment:'))
a=y1-y2
b=x2-x1
e=x2*y1-x1*y2
c=y3-y4
d=x4-x3
f=x4*y3-x3*y4
print(a,b,e,c,d,f)
m=LinearEquation(a,b,c,d,e,f)
if m.isSolvable()!=True:
    print('The equation has on solution')
else:
    print('The intersecting point is:('+str(m.getX())+','+str(m.getY())+')')
'''

