'''
import math
r=input(">>")
s=2*r*math.sin(math.pi/5)
Area=5*s*s/(4*math.tan(math.pi/5))
print(Area)
'''
'''
import math
x1,y1,x2,y2=input(">>")
x3,y3,x4,y4=math.radians(x1),math.radians(y1),math.radians(x2),math.radians(y2)
d=6371.01*math.acos(math.sin(x3)*math.sin(x4)+math.cos(x3)*math.cos(x4)*math.cos(y3-y4))
print(d)
'''
'''
import math
s=input(">>")
Area=5*s**2/(4*math.tan(math.pi/5))
print(Area)
'''
'''
import math
n,s=input(">>")
Area=n*s**2/(4*math.tan(math.pi/n))
print(Area)
'''
'''
a=input(">>")
b=chr(a)
print(b)
'''
'''
a=str(raw_input("xingming>>"))
b=input("shijian>>")
c=input("baochou>>")
d=input("lianbangshui>>")
e=input("zhoushui>>")
print(a)
print(b)
print(c)
print(b*c)
print(b*c*d)
print(b*c*e)
print(b*c*(d+e))
print(b*c-b*c*(d+e))
'''
'''
a=input(">>")
while(a!=0):
    print(a%10),
    a=a/10
'''
'''
import math
a,b,c=input()
if b**2-4*a*c>0:
    r1=(-b+math.sqrt(b**2-4*a*c))/2*a
    r2=(-b-math.sqrt(b**2-4*a*c))/2*a
    print r1,r2
elif b**2-4*a*c==0:
    r1=(-b+math.sqrt(b**2-4*a*c))/2*a
    print r1
else:
    print('The equation has no real roots')
'''
'''
import random
b=random.randint(0,100)
a=random.randint(0,100)
print(a,b)
c=input("lianggeshudehe")
if a+b==c:
    print("true")
else:
    print("flase")
'''
'''
a,b=input(">>")
c=(a+b)%7
if c==0:
   print('Sunday')
elif c==1:
   print('Monday')
elif c==2:
    print('Tuesday')
elif c==3:
    print('Wednesday')
elif c==4:
    print('Thursday')
elif c==5:
    print('Friday')
elif c==6:
    print('Saturday')
'''
'''
a,b,c=input()
t=int()
if a>b:
    t=a
    a=b
    b=t
if a>c:
    t=a
    a=c
    c=t
if b>c:
    t=b
    b=c
    c=t
print(a,b,c)
'''
'''
a,b=input()
c,d=input()
if a*b>c*d:
   print(2)
if a*b<c*d:
   print(1)
'''
'''
a,b=input()
if a==1:
    print('31')
elif a==2:
    if b%100==0:
        if b%400==0:
            print("29")
        else:
            print("28")
    elif b%4==0:
        print('29')
    else:
        print('28')
elif a==3:
    print('31')
elif a==4:
    print('30')
elif a==5:
    print('31')
elif a==6:
    print('30')
elif a==7:
    print('31')
elif a==8:
    print('31')
elif a==9:
    print('30')
elif a==10:
    print('31')
elif a==11:
    print('30')
elif a==12:
    print('31')
'''
'''
import random
a=random.randint(0,1)
b=input()
if a==b:
    print('Ture')
else:
    print('Flase')
'''
'''
import random
a=random.randint(0,2)
print(a)
b=input()
if a-b==1:
    print('lose')
elif a==0 and b==2:
    print('lose')
elif a-b==0:
    print('draw')
else:
    print('win')
'''
'''
import random
a=random.choice(['Ace','2','3','4','5','6','7','8','9','Jack','Queen','King'])
b=random.choice(['meihua','hongtao','fangkuai','heitao'])
print(a+' '+'of'+' '+b)
'''
'''
a=int(input(""))
a=str(a)
b=a[::-1]
if(a==b):
    print('yes')
else:
    print('no')
'''
'''
a,b,c=input()
if a+b>c:
    if a+c>b:
        if b+c>a:
            print(a+b+c)
        else:
            print('feifa')
    else:
        print('feifa')
else:
    print('feifa')
'''
