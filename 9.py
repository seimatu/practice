#tuple deta type

# a=100,'Lohit'
# print(a)

# list=(1,2,3,4, 'Lohit ')
# print(list)

# #select by index
# print(list[0])
# print(list[2])
# print(list[1])

# list[2]=7

# empty_tuple=()
# print(empty_tuple)

# tuple1=(100,200,300)
# tuple2=('lohit','python')

# print(tuple1+tuple2)

# tuple i can not change leter 

#lengeth of tuple
# tuple10=('python','php','java')
# # print(len(tuple10))

# tuples=('add',45345.353,'jpohjhn',5463)
# tinytuple=(123,'join')

# print(tuples[2:1])
# print(tuples[:])
# print(tinytuple*3)
# print(tuples[::-1])

# print('---------------------------------------')

# tup=('physics','maths',1000,249)
# print(tup)
# del tup
# print(tup)

#nested tuple
# n_tuple=('mouse trap', [8,7,6],(1,2,3,4,5, 'yuri'))
# print(n_tuple)
# print(n_tuple[1])
# print(n_tuple[1][1])
# print(n_tuple[2][5][3])

# print('------------------step------------------') 

# my_tuple=('p','u','j','s','g','b','q','m')
# print(my_tuple[:-5])
# print(my_tuple[1:5:2])
# print(my_tuple[0:8:3])


# print('------------------select reverse------------------------') 
# print(my_tuple[0:-2])



tuplex = "w", 3, "r", "s", "o", "u", "r", "c", "e"
print(tuplex)
#tuples are immutable, so you can not remove elements
#using merge of tuples with the + operator you can remove an item and it will create a new tuple
tuplex = tuplex[:2] + tuplex[3:]
print(tuplex)
#converting the tuple to list
listx = list(tuplex) 
#use different ways to remove an item of the list
listx.remove("c") 
#converting the tuple to list
tuplex = tuple(listx)
print(tuplex)


# membership operater

print('---------------------boolean--------------------')
# my_new_operater=('a','b','c','d','e')
# print('a' in my_new_operater)
# print('sei' in my_new_operater)

# # not in operater
# print('sei'not in my_new_operater)


