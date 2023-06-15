#A product database

class Product:

    def __init__(self, name, amount, price):

        self.n = name
        self.a = amount
        self.p = price

    def get_price(self, x):
        while x <= self.a:
            if x<10:
                cost = x * self.p
            elif 10 < x < 100: 
                cost = (x * self.p) - ((10 / 100) * (x * self.p))
            elif x > 100:
                cost = (x * self.p) - ((20 / 100) * (x * self.p))
            return '{} units of {} cost ${}'.format(x, self.n, cost)
        else:
            return 'Not in stock. {} units left'.format(self.a)
        
    
    def make_purchase(self, x):
        stock = self.a - x
        return '{} units left'.format(stock)



buy = Product('Pistol', 300, 350)
print(buy.get_price(103))
print(buy.make_purchase(103))