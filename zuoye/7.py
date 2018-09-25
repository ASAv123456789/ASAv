a=input(">>")
num=0
for i in range(1,7):
    num=(num+a)*(1+0.00417)
    if i==6:
        print(num)
        break
