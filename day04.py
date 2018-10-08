'''
i=1
c=0
a=1
def getPentagonalNumber(n):
   d=n*(3*n-1)/2
   return int(d)
while i >0:
    print(getPentagonalNumber(a),' ',end="")
    c+=1
    a+=1
    if c%10==0:
        print(' ')
    if c==100:
        break
'''
'''

def sumDigits(n):
    b=0
    while n>0:
        b=n%10+b
        n=int(n/10)
    return b
print(sumDigits(int(input())))
'''
'''
def d(nu1,nu2,nu3):
    if nu1>nu2:
        nu1,nu2=nu2,nu1
    if nu1>nu3:
        nu1,nu3=nu3,nu1
    if nu2>nu3:
        nu2,nu3=nu3,nu2
    return(nu1,nu2,nu3)
a,b,c=eval(input())
print(d(a,b,c))
'''
'''
def fu(a,b,c):
    i=0
    b=b/100
    c=c*12
    while c>i:
        a=a*(1+(b/12))
        i+=1
    return a
x,y=eval(input())
for i in range(1,31):
    print(i,' ',fu(x,y,i))
'''
'''
import math
def printChars(ch1,ch2,numberPerLine):
    for i in range(1,ord(ch2)-ord(ch1)):
        print('{} '.format(chr(ord(ch1)+i)),end='')
        if i%numberPerLine==0:
            print()
s1='1'
s2='Z'
n=10
printChars(s1,s2,n)
'''
'''
def num(year):
    year=int(year)
    if year%4==0:
        if year%100==0:
            if year%400==0:
                print(366)
            else:
                print(365)
        else:
            print(366)
    else:
        print(365)
for i in range(2010,2021):
    num(i)
'''
'''
import math
def distance(x1,y1,x2,y2):
    return math.sqrt((x2-x1)**2+(y2-y1)**2)

x,y,n,m=eval(input())
print(distance(x,y,n,m))
'''
'''
for p in range(1,32):
    fg=0
    if 2**p-1==1:
        continue
    for i in range(2,2**p-1-1):
        if (2**p-1)%i==0:
            fg=1
            break
    if fg==0:
        print(p,' ',2**p-1)

'''
'''
import time

now=time.time()
mon=time.localtime(now)[1]
day=time.localtime(now)[2]
year=time.localtime(now)[0]
hour=time.localtime(now)[3]
mins=time.localtime(now)[4]
sec=time.localtime(now)[5]

print('Current date and time is '+str(mon)+' '+str(day)+','+str(year)+' '+str(hour)+':'+str(mins)+':'+str(sec))
'''
'''
import random
a=random.randint(1,6)
b=random.randint(1,6)
n=a+b
if n==2 or n==7 or n==12:
    print('You rolled ',a,'+',b,'=',n)
    print('You lose')
elif n==7 or n==11:
    print('You rolled ',a,'+',b,'=',n)
    print('You win')
else:
    print('You rolled',a,'+',b,'=',n)
    print('point is ',n)
    i=n
    while i!=7:
        x=random.randint(1,6)
        y=random.randint(1,6)
        m=x+y
        if i==m :
            print('You rooled ',x,'+',y,'=',m)
            print('You win')
            break
        elif m==7:
            print('You rooled ',x,'+',y,'=',m)
            print('You loss')
            break
        else:
            print('You rooled ',x,'+',y,'=',m)
            print('point is ',m)
        i=m
'''
'''
#coding: utf-8    
  
import smtplib    
from email.mime.multipart import MIMEMultipart    
from email.mime.text import MIMEText    
from email.mime.image import MIMEImage 
from email.header import Header   
    
#设置smtplib所需的参数
#下面的发件人，收件人是用于邮件传输的。
smtpserver = 'smtp.163.com'
username = '15047919190@163.com'
password='xxxxx'
sender='15047919190@163.com'
#receiver='XXX@126.com'
#收件人为多个收件人
receiver=['kafeioulei@qq.com']

subject = 'Python email test'
#通过Header对象编码的文本，包含utf-8编码信息和Base64编码信息。以下中文名测试ok
#subject = '中文标题'
#subject=Header(subject, 'utf-8').encode()
    
#构造邮件对象MIMEMultipart对象
#下面的主题，发件人，收件人，日期是显示在邮件页面上的。
msg = MIMEMultipart('mixed') 
msg['Subject'] = subject
msg['From'] = '15047919190@163.com <15047919190@163.com>'
msg['To'] = '896446511@qq.com'
#收件人为多个收件人,通过join将列表转换为以;为间隔的字符串
#msg['To'] = ";".join(receiver) 
#msg['Date']='2012-3-16'

#构造文字内容   
text = "Hi!\nHow are you?\nHere is the link you wanted:\nhttp://www.baidu.com"    
text_plain = MIMEText(text,'plain', 'utf-8')    
msg.attach(text_plain)
       
#发送邮件
smtp = smtplib.SMTP()    
smtp.connect('smtp.163.com')
#我们用set_debuglevel(1)就可以打印出和SMTP服务器交互的所有信息。
#smtp.set_debuglevel(1)  
smtp.login(username, password)    
smtp.sendmail(sender, receiver, msg.as_string())    
smtp.quit()
'''
