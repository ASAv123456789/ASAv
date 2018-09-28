'''
b=0
c=0
d=0
for i in range(10000):
    a=input()
    if a == 0:
        break
    elif a<0:
        b+=1
    elif a>0:
        c+=1
    a=d+a
print('zhengshu',c,'fushu',b,'pingjun',a/(b+c))
'''
'''
i=0
a=10000
d=0
e=0
while i<14:
    a=1.05*a
    if i==9:
        e=a
    elif i>9 and i<14:
        d=d+a
    i+=1
print('shinianzhihou',e,'yihouxuefei',d)
'''
'''
a=0
for i in range(100,1001):
    if i%5==0:
        if i%6==0:
            print(i,' ',end="")
            a+=1
            if a%10==0 :
                print(' ')

'''
'''
n=1
while n**2<=12000:
    n+=1
print(n,n-1)
'''
'''
a=0
b=0
c=1
d=50000
while c<50001:
    a=a+1/(c*1.0)
    c+=1
while d>0:
    b=b+1/(d*1.0)
    d=d-1
print(a)
print(b)
'''
'''
a=0
b=1
c=3
while b<=97:
    a=a+b/(c*1.0)
    b+=2
    c+=2
print(a)
'''
'''
a=0
b=1
c=0
d=1
while d<=100000:
    q=1/(d*1.0)
    a=a+b*q
    b=b*-1
    d=d+2
    c=c+1
    if c==5000:
        print(d-1,4*a)
        c=0
'''

'''
for i in range (1,10000):
    a=0
    for m in range(1,i):
        if i%m==0:
            a=a+m
    if i==a:
        print(i)
'''
'''
a=0
for i in range(1,8):
    for m in range(i+1,8):
        a+=1
        print(i,m)
print(a)
'''
