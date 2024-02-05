class Product:
    def __init__(self, price):
        self._price = price

    @property
    def price(self):
        return self._price
    
    @price.setter
    def price(self, value):
        if value < 0:
            raise ValueError('Product price cannot be negative')
        else:
            self._price(value)

    def __str__(self):
        return f'This product price is {self.price}'
        
product = Product(10)

print(product.price)


