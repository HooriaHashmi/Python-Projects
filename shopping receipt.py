#start by using class functions to oragnise tasks at hand
class ShopAttendant:
    def initial(self, name, password):
        self.name = name
        self.password = password
        self.logged_in = False

    def login(self, name, password):
        if name == self.name and password == self.password:
            self.logged_in = True
            return True
        else:
            return False
        

class PointOfSale:
#store items into lists and dictionaries
    def initial(self):
        self.items = {'Bread': 10, 'Water': 15, 'Pizza': 35, 'Salad': 20}
#an empty list to keep all the transactions that will be made
        self.transactions = []


#another function for the transactions
    def process_transaction(self, attendant):
        total_amount = 0
        while True:
#while all that is true allow the user to enter the items 
            item_name = input("Enter item name (or type 'done' to finish): ").capitalize()
#if he enters done break and move on to the next line
            if item_name == 'Done':
                break
#in the case where the item is not spelt right or not in the lsit tell the attendant to try again
            elif item_name not in self.items:
                print("Invalid item name. Please try again.")
                continue
#refer to the dictionary and add the total amount
            quantity = int(input("Enter quantity: "))
            total_amount += self.items[item_name] * quantity
        amount_paid = float(input("Enter amount paid: "))
        change = amount_paid - total_amount
#the total amount needs to be added to the transactions list
        self.transactions.append(total_amount)
#print out the change after the user enters how much he received from the client
        print("Total amount:", total_amount)
        if change > 0:
            print("Change:", change)

# generate the bill
    def generate_bill(self):
        pass  
#calculate the attendant's salary
    def calculate_attendant_pay(self, hours_worked):
        base_pay = 100 * hours_worked
        if hours_worked > 8:
            extra_pay = (hours_worked - 8) * 50
            return base_pay + extra_pay
        else:
            return base_pay
def main():
    attendant = ShopAttendant("Joe", "12345")
    pos = PointOfSale()
        
#------------------------------------------------------------------------------------
#the program now has to run      
    while True:
        if not attendant.logged_in:
            name = input("Enter your name: ")
            password = input("Enter your password: ")
            if attendant.login(name, password):
                print("Login successful.")
            else:
                print("Invalid credentials. Please try again.")
                continue

#print the menu for the user to choose from
        print("\nMenu:")
        print("1. Process Transaction")
        print("2. Generate Bill")
        print("3. Calculate Attendant Pay")
        print("4. Logout")

#allow the user to enter the option he wants to work on and print it out accordingly

        choice = input("Enter your choice: ")

        if choice == '1':
            pos.process_transaction(attendant)
        elif choice == '2':
            pos.generate_bill()
        elif choice == '3':
            hours_worked = float(input("Enter hours worked: "))
            pay = pos.calculate_attendant_pay(hours_worked)
            print("Attendant pay:", pay, "cedis")
        elif choice == '4':
            attendant.logged_in = False
            print("Logged out.")
        else:
            print("Invalid choice. Please try again.")

#end of program

if __name__ == "__main__":
    main()




