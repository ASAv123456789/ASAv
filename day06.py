'''
1.
def a(b):
    num=0
    for i in b:
        if i=='-':
            num+=1
    if num==2: 
        if b[3] and b[6] is'-':
            b=b.replace('-','')
            if b.isdigit() is True:
                print('Valid SSN')
            else:
                print('Invalid SSN')
        else:
            print('Invalid SSN')
    else:
        print('Invalid SSN')
c=str(input('按照格式ddd-dd-dddd输入一个社会安全号码:'))
a(c)
'''
'''
2.
def a(b,c):
    d=b in c
    print(d)
b=str(input())
c=str(input())
a(b,c)
'''
'''
3.
def a(b):
    if b.isalnum() == True:
        num=0
        for i in b:
            num+=1
        if num>=8:
            m=0
            for i in b:
                if i in '0123456789':
                    m+=1
            if m>=2:
                print('valid password')
            else:
                print('invalid password')
        else:
            print('invalid password')
    else:
        print('invalid password')
b=str(input())
a(b)
'''
'''
4.
def countLetters(s):
    x='abcdefghijklmnopqrstuvwxyz'
    for i in x:
        m=0
        for n in s:
            if i == n:
                m+=1
        print(i,'=',m)
a=str(input())
countLetters(a)
'''
'''
5.
def getNumber(uppercaseLetter):
    a=uppercaseLetter
    b=a.lower()
    b=b.replace('a','2')
    b=b.replace('b','2')
    b=b.replace('c','2')
    b=b.replace('d','3')
    b=b.replace('e','3')
    b=b.replace('f','3')
    b=b.replace('g','4')
    b=b.replace('h','4')
    b=b.replace('i','4')
    b=b.replace('j','5')
    b=b.replace('k','5')
    b=b.replace('l','5')
    b=b.replace('m','6')
    b=b.replace('n','6')
    b=b.replace('o','6')
    b=b.replace('p','7')
    b=b.replace('q','7')
    b=b.replace('r','7')
    b=b.replace('s','7')
    b=b.replace('t','8')
    b=b.replace('u','8')
    b=b.replace('v','8')
    b=b.replace('w','9')
    b=b.replace('x','9')
    b=b.replace('y','9')
    b=b.replace('z','9')
    print(b)
a=str(input())
getNumber(a)
'''
'''
6.


def reverse(s):
    print (s[::-1])
a=str(input())
reverse(a)
'''
'''
7.
def guize_1(n):
    if len(n)>=13 and len(n)<=16:
        if n.startswith('4')==True or n.startswith('5')==True or n.startswith('37')==True or n.startswith('6')==True:
            return True

def suanfa_1(n):
    sum_=0
    for i in n:
        z=int(i)*2
        if z>=10:
            a=z%10
            b=z/10
            z=a+b
        sum_=sum_+z
    return sum_

def suanfa_2(n):
    sum_=0
    for i in range(1,len(n)):
        if i%2!=0:
            sum_+=int(n[i])
    return sum_

def isValid(S):
    if guize_1(S)==True:
        if (suanfa_1(S)+suanfa_2(S))%10==0:
            print('Yes')
        else:
            print('No')
    else:
        print('No')

a=input('Enter number:')
isValid(a)
'''
'''
8.
def a(b):
    n=0
    m=0
    for i in b:
        i=int(i)
        if n%2==0:
            m=m+i
        else:
            m=m+3*i
        n+=1
    d13=str(10-m%10)
    if d13=='10':
        print(b+'0')
    else:
        print(b+d13)
c=str(input())
a(c)
'''
