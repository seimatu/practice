# lists=[1,2,3,4,5,6,7,8,9]


# # break is oppsite of continue
# count=1

# for i in lists:
#     if i==4:
#         print('item is matched')

#         count=count+10
#         # no more looping after this line 
#         break
#     print('now the new value of count',count)

# print('the end')


print('-----------------------------------------------------------------')

# lists=[1,2,3,4,5,6,7,8,9]

# count=1

# for i in lists:
#     if i==4:
#         print('item is matched')

#         count=count+10
#         continue
#     print('now the new value of count',count)

# print('the end')




# test


score=[55,93,87,71,60,52,47,22,65,46,]

count=1

for number in score:
    if number>=90:
        print(number,'gread')

        count=count+10
    
    elif number>=60:
        print(number,'good')

    elif number>=31:
        print(number,'so-so')

    elif number<=30:
        break
        print(number,'bad')
    else :
        print('the end')

