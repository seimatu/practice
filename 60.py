#calculating with *args

def calculate(*args):
        print (sum(args))


calculate(10,20,30)

#one mare way

def calculate(*args):

    sum=0
    for arg in args:
        sum=sum+arg
    print('The sum is ',sum)
sum=0
calculate(10,20,30,40,50)
#110 will be printed as the sum
print('Value of sum outside the function',sum)#0 will be peinted

def calculate(*args):
    
    sum=0
    for arg in args:
        sum=sum+arg
    print('The sum is ',sum)
sum=0
calculate(10,20,30,40,50)
#110 will be printed as the sum
print('Value of sum outside the function',sum)#0 woll be peinted
