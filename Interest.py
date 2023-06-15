#This code calculates simple interest given principal, time in years and interest rate

class Investment:

    def __init__(self, p, i):
        self.p=p
        self.i=i
    def value_after(self,n):
        nn = self.p * (( 1 + (self.i/100) ) ** n)
        return '{:2f}'.format(nn)
    def _str_(self):
        return 'Principal - ${:02d} , Interest rate - {:02}%'.format(self.p, self.i)
    
econs = Investment(15,1)

print(econs._str_())
print(econs.value_after(5))