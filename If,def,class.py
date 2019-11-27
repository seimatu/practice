# scora = 90
# if scora == 90:
#     print('good')
#     print(scora == 90)

# money = 1200
# bank = 600
# chocoreat = 200

# if money+bank == 1100:
#     print('total money')
# else :
#     print('Not enough')


# scora = 81

# if scora >= 80:
#     print('great')
# elif scora >= 60:
#     print('good')
# else :
#     print('bad')

# scora = 68

# if scora >= 80:
#     print('great')
# elif scora >= 60:
#     print('good')
# else :
#     print('bad')

# scora = 20

# if scora >= 80:
#     print('great')
# elif scora >= 60:
#     print('good')
# else :
#     print('bad')


# a = 12
# if a <= 15 and a >= 10:
#     print('opening school')

# b = 6
# if b == 7 or b > 4:
#     print('you can buy')

# c = 100
# if not c == 99:
#     print('you have miss')


#defについて
# def heikin(kokugo, sansuu):
#     '''国語と算数の平均点をの算出
#     (入力値)　kokugo:国語の点数、sansuu:算数の点数
#     (戻り値) 国語と算数の平均点'''
#     return (kokugo + sansuu) / 2
 
# taro_name = '太郎'
# taro_kokugo = 50
# taro_sansuu = 45
# taro_heikin = heikin(taro_kokugo, taro_sansuu)
 
# hanako_name = '花子'
# hanako_kokugo = 90
# hanako_sansuu = 85
# hanako_heikin = heikin(hanako_kokugo, hanako_sansuu)
 
# print(taro_name, 'の平均点：', taro_heikin)
# print(hanako_name, 'の平均点：', hanako_heikin)

#classについて
class Tokuten_deta:
    def __init__(self):
        self.name=''
        self.kokugo=0
        self.sannsu=0
        self.heikin=0.0
    def heikin_cal(self):
        self.heikin=(self.kokugo+self.sannsu)/2

sei=Tokuten_deta()
sei.name='sei'
sei.kokugo=40
sei.sannsu=80
sei.heikin_cal()

daiki=Tokuten_deta()
daiki.name='daiki'
daiki.kokugo=70
daiki.sannsu=90
daiki.heikin_cal()

print(sei.name,'の平均点は',sei.heikin)
print(daiki.name,'の平均点は',daiki.heikin)
