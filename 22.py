# slicing in for loop

offices=['lohit',1234,'sei',90889,'python','KLE']

# for office in offices[0:3]:
#     print(office)

# check the item is matching

for office in offices:
    if office=='python':
        print('the programing languege is',office)
    elif office=='KLE':
        print('The university is ',office)
    else:
        print('all ohter is ',office)