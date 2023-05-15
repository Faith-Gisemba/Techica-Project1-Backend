class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

class Customer:
    def __init__(self, name, email):
        self.name = name
        self.email = email

class Order:
    def __init__(self, customer, products):
        self.customer = customer
        self.products = products


    def calculate(self):
        total = 0
        for product in self.products:
            total += product.price
        return total

class CustomerService:
    def __init__(self):
        self.orderss = []

    def place_order(self, customer, productcs):
        order = Order(customer, products)
        self.orderss.append(order)
        return order