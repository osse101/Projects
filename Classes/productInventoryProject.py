
'''
**Product Inventory Project** - Create an application
which manages an inventory of products.  Create a
product class which has a price, id, and quantity on
hand.  Then create an inventory class which keeps
track of various products and can sum up the inventory
class
'''

class Product:
    productId=0

    def __init__(self):
        Product.productId += 1
        self.productId = Product.productId
        self.price = 0.0
        self.quantity = 0

    def __init__(self, p, q):
        Product.productId += 1
        self.productId = Product.productId
        self.price = p
        self.quantity = q

    def setPrice(self, price):
        assert price >= 0
        self.price = price

    def setQuantity(self, quantity):
        self.quantity = quantity

    def getQuantity(self):
        return self.quantity

    def getPrice(self):
        return self.price

    def getId(self):
        return self.productId

class Inventory:

    def __init__(self):
        self.products = []

    def addProduct(self, p):
        self.products.append(p)

    def sumProducts(self):
        sum = 0.0
        for p in self.products:
            q = p.getQuantity()
            sum += (q*p.getPrice())
        return sum

def main():
    print 'Running'
    p1 = Product(p=12.4, q=3)
    p2 = Product(p=1.00, q=50)
    p3 = Product(p=5.50, q=10)

    i = Inventory()
    i.addProduct(p1)
    i.addProduct(p2)
    i.addProduct(p3)
    print i.sumProducts()


if __name__ == "__main__":
    main()
