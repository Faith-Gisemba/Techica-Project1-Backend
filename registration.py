class Customer:
    def __init__(self, name, email,password,confirmation):
        self.name = name
        self.email = email
        self.password = password
        self.confirmation = confirmation
class Registrer:
    def __init__(self):
        self.customer = []
    def register(self, name, email, password,confirmation):
        new_customer = Customer(name, email, password,confirmation)
        self.customer.append(new_customer)
        return f"Hello {name},Thank you for choosing Imarika Groceries"