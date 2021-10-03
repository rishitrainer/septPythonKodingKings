class Customer:


    def __init__(self, cust_id, cust_name):
        self.id = cust_id
        self.name = cust_name
        print("Class is Initialized", self.id, self.name)

    def discount(self, validCust):
        if validCust:
            print(self.id, self.name, "Discount is 5%")
        else:
            print(self.id, self.name, "Discount is 0%")

    # methods - functionality
    # variables - data

# Instance of class - Object
# userDefinedName = ClassName()
# Customer() - Constructor - initializer
cust01 = Customer(cust_name="Ram", cust_id=101)
cust01.discount(True)
cust02 = Customer(102, "Laxman")
print(cust02.id, cust02.name)
print(cust01.id, cust01.name)
cust03 = cust02
print(cust03.id, cust03.name)
# <class 'method'>
print(type(cust01.discount))