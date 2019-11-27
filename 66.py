class Place:
    def __init__(self,trip,price,dist,photo):
        self.trip=trip
        self.price=price
        self.dist=dist
        self.photo=photo

    def Myprice(self):
        print('hello im going to pay ',self.trip,self.price)

    def Myprices(self):
        print('im going to pay',self.price)


myTrip=Place('India','10,000','6000km','fs')

myTrip.Myprice()
