
class item:
    def __init__(self,name,price,quantity):
        #assigning to the self object
        self.name=name
        self.price=price
        self.quantity=quantity

    def totalprice(self):
        total_price=self.price*self.quantity
        return total_price


#The 'self' keyword is gonna make the interpreter read from the level that we are calling from .. that is
#if we are calling from the instance level, it reads from that level and vice versa
#Creating instances
item1=item("Phone",13000,2)
item2=item("Laptop",80000,1)

