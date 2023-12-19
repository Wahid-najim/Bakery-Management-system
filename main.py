# importing time module to use it in date sector
import time

print("Welcome to Tokyo Ghoul Bakery Shop")
# creating a class bakery
class Bakery:
    def __init__(self, name, date, quantity, cell_number, delivery_date, bakery_type, bakery_item):
        self.name = name
        self.date = date
        self.quantity = quantity
        self.cell_number = cell_number
        self.delivery_date = delivery_date
        self.bakery_type = bakery_type
        self.bakery_item = bakery_item

    def management(self):
        self.name = input("Please Enter Your Name : ")
        self.date = time.strftime("%d/%m/%Y")  # Get the current date
        # if the delevary date is in future then it will not show any error
        self.delivery_date = input("Please enter the delivery date (dd/mm/yyyy): ")
        self.quantity = int(input("Please enter the quantity :"))
        self.cell_number = int(input("Please enter your cell number: "))
        self.bakery_type = input("What would you like to order, cake or bread? ")
        
        if self.bakery_type.lower() == 'cake':
            self.bakery_item = input("Which cake would you like, dark forest, red velvet, or white forest? ")
        elif self.bakery_type.lower() == 'bread':
            self.bakery_item = input("Which bread would you like, normal, fruit, or garlic? ")

        # Store the data in a text file
        with open('bakery_data.txt', 'a') as f:
            f.write(f'Name: {self.name}, Date: {self.date}, Delivery Date: {self.delivery_date}, Quantity: {self.quantity}, Cell Number: {self.cell_number}, Bakery Type: {self.bakery_type}, Bakery Item: {self.bakery_item}\n')

bakery = Bakery(None, None, None, None, None, None, None)
bakery.management()
