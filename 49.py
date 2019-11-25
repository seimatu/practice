#only if its list
#そのリストの場合のみ。

def myfun2(x):
    x[0]=120
#after below line link of x with previous
#object gets broken, A new object is assigned
#オブジェクトがなくなり、新しいオブジェクトが与られる。#Xの前の行の下のリンク
# to x.
#

X=[20,30,40]

#driver code (note that 1st is not modified
#after function call.
#関数呼出後、１番目のコードは変更されないことを注意。グローバルコード
lst = [10,11,12,13,14,15]
myfun2(lst)
print(lst)



#this is not list
#これはリストではない。

def myfun(x):
    #After below line link of x with previous
    #objict gets broken. A new object is assigned
    #オブジェクトがなくなり、新しいオブジェクトが与られる。Xの前の行の下のリンク
    #to x.
    x = 20
    print('------value here is 20-----------')
#Driver Code (Note that x is not modified
#after function call.
#関数の呼出後はXは変更されない。
x=10
myfun(x):
print(x)