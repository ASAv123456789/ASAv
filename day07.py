'''
1.
def A(a):
    best=int(max(a))
    res=0
    for i in a:
        i=int(i)
        if i>=best-10:
            print('Student '+str(res)+' socore is '+str(i)+' and grade is A')
        elif i>=best-20:
            print('Student '+str(res)+' socore is '+str(i)+' and grade is B')
        elif i >=best-30:
            print('Student '+str(res)+' socore is '+str(i)+' and grade is C')
        elif i>= best-40:
            print('Student '+str(res)+' socore is '+str(i)+' and grade is D')
        else:
            print('Student '+str(res)+' socore is '+str(i)+' and grade is F')
        res+=1
a,b,c,d=eval(input())
s=[a,b,c,d]
A(s)
'''
'''
2.
def a(b):
    print(b[::-1])
c=str(input())
c=c.split()
a(c)
'''
'''
3.
def count(num):
    num = num.split()
    s = []
    for q in range(0, 102):
        s.append(0)
    for i in range(len(num)):
        s[int(num[i])] += 1
    for i in range(0, 102):
        if s[i] != 0:
            if s[i] == 1:
                print(str(i) + " occurs " + str(s[i]) + " time")
            else:
                print(str(i) + " occurs " + str(s[i]) + " times")
num = input("Enter integers between 1 and 100: ")
count(num)
'''
'''
4.
def a(b):
    s=0
    n=0
    y=0
    z=0
    for i in b:
        i=int(i)
        s=s+i
        n+=1
    p=s/n
    for x in b:
        x=int(x)
        if x<p:
            y+=1
        elif x>p:
            z+=1
    print('大于  '+str(z)+'  小于  '+str(y))
c=input()
c=c.split()
a(c)
'''
'''
5.
def a():
    import random
    counts=[]
    for i in range(10):
        counts.append(0)
    s=[]
    for n in range(1000):
        z=random.randint(0,9)
        s.append(z)
    for m in s:
        counts[m]+=1
    for x in range(len(counts)):
        print(str(x)+' : '+str(counts[x]))
a()
'''
'''
6.
def index0fSmallestElement(lst):
    c=min(lst)
    for i in range(len(lst)):
        if c==lst[i]:
            print(lst[i],i)
            break
a=input()
a=a.split()
index0fSmallestElement(a)
'''
'''
7.
def a(b):
    import random
    c=[]
    x=len(b)
    for i in range(len(b)):
        z=random.randint(0,x-1)
        x-=1
        y=b.pop(z)
        c.append(y)
    print(c)
u=input()
u=u.split()
a(u)
'''
'''
8.
def a(b):
    x=[]
    for i in b:
        if i not in x:
            x.append(i)
    print(x)
c=input()
c=c.split()
a(c)
'''
'''
9.

def a(b):
    for i in range(1,len(b)):
        if int(b[i])>=int(b[i-1]):
            if i ==len(b)-1:
                print('The list is already sorted')
        else:
            print('The list is not sorted')
            break
c=input()
c=c.split()
a(c)
'''
'''
10.
def a(b):
    for n in range(len(b)-1):
        for i in range(len(b)-n-1):
            if int(b[i])>int(b[i+1]):
                b[i],b[i+1]=b[i+1],b[i]
    print(b)
c=input()
c=c.split()
a(c)
'''
'''
11.
def a():
    import random
    m=0
    b=['1','2','3','4','5','6','7','8','9','10','11','12','13']
    c=['hongtao','heitao','meihua','fangkuai']
    while 1:
        z=[]
        for i in range(4):
            x=random.randint(0,len(b)-1)
            y=random.randint(0,len(c)-1)
            z.append(b[x])
            z.append(c[y])
        m+=1
        g=z[0]+z[1]
        h=z[2]+z[3]
        j=z[4]+z[5]
        k=z[6]+z[7]
        if z[1]!=z[3] and z[1]!=z[5] and z[1]!=z[7] and z[3]!=z[5] and z[3]!=z[7] and z[5]!=z[7]:
            print(m,' 牌 ',g,h,j,k)
            break
a()
'''
