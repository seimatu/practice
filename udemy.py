# x=20
# y=x
# y=5
# print(y)
# print(x)

# x=['a','b']
# y=x
# y[0]='p'
# print(y)
# print(x)

# print('-----------------リストのコピー-------------------')

# x=[1,2,3,4,5,6,]
# y=x
# y[1]=100
# print('y=' ,y)
# print('x=' ,x)

# x=[1,2,3,4,5,6,]
# y=x.copy()
# y[1]=100
# print('y=' ,y)
# print('x=' ,x)

#リストの使い所(POPの使用)
# seat=[]
# min=0
# max=5

# min<=len(seat)<max
# if min==True:
#     seat.appding(min+1)
#     print(seat)
# else:
#     print(seat)

# print('---------------タプルの使い所---------------------')

# choise_from_two=('A','B','C')
# answer=[]

# answer.append('A')
# answer.append('c')
# print(choise_from_two)
# print (answer)


# min,max=0,100
# print(min,max)

# a=100
# b=500
# print(a,b)
# a,b=b,a
# print(a,b)

# print('---------------dictinaly---------------------')
# d={'x':10,'y':20}
# print (d['x'])

# d['x']=100
# print (d)

# d['y']='sei'
# print (d)

# d['z']=1000
# print (d)

# print(d.keys())
# print()

# print('---------------in.not---------------------')
# y=[1,2,3]
# x=1

# if x in y :
#     print('in')

# if 100 not in y:
#     print('not in')

# a=1
# b=2
# if not a==b:
#     print('true')
# if a!= b:
#     print('true')

print('---------------while,for---------------------')
# count = 0
# while True:
#     if count>=10:
#         break

#     if count==2:
#         count+=1
#         continue

#     print(count)
#     count+=1

# while True:
#     word=input('enter :')
#     if word=='OK':
#         break
#     print('next')

# for i,fruit in enumerate(['apple','banana','orange']):
#     print(i,fruit)

days=['Mon','Tue','wen']
fruits=['apple','banana','orange']
drinks=['coffee','tea','beer']

for i in range(len(days)):
    print(days[i],fruits[i],drinks[i])

#上下同じ意味

for day,fruits,drink in zip(days,fruits,drinks):
    print(day,fruits,drink)