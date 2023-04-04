# Your parking garage class should have the following methods:
# - takeTicket
# - This should decrease the amount of tickets available by 1
# - This should decrease the amount of parkingSpaces available by 1
# - payForParking
# - Display an input that waits for an amount from the user and store it in a variable
# - If the payment variable is not empty then (meaning the ticket has been paid) -> display a message to the user that their ticket has been paid and they have 15mins to leave
# - This should update the "currentTicket" dictionary key "paid" to True
# -leaveGarage
# - If the ticket has been paid, display a message of "Thank You, have a nice day"
# - If the ticket has not been paid, display an input prompt for payment
# - Once paid, display message "Thank you, have a nice day!"
# - Update parkingSpaces list to increase by 1 (meaning add to the parkingSpaces list)
# - Update tickets list to increase by 1 (meaning add to the tickets list)

# You will need a few attributes as well:
# - tickets -> list
# - parkingSpaces -> list
# - currentTicket -> dictionary



class Garage():
    current_tickets = {}

    def __init__ (self, user_vehicle):
        # self.user_vehicle = user_vehicle
        self.parkingSpaces = 5
        self.tickets = 5
        Garage.current_tickets.update()

    def takeTicket(self):
        # reduce tickets by 1, reduce parkingSpaces by 1, create current ticket

        if self.parkingSpaces < 1:
                print("Sorry! The parking garage is full.")
                    
        else:
            self.tickets -= 1
            self.parkingSpaces -= 1
            Garage.current_tickets['paid'] =  False
            print("Please take your ticket.")
            
        useGarage()

    def payForParking(self):
        # collect payment
        print(self.tickets)
        amount_paid = float(input("What is your parking fee total?\n"))
        if amount_paid > 0.00:
            for value in Garage.current_tickets:
                Garage.current_tickets['paid'] = True
            print(f"You have paid ${amount_paid}. You have 15 minutes to exit the garage.")
                
        else:
            print("Please swipe payment card or insert cash.")         
            return
        
        useGarage()

    def leaveGarage(self):
        # increase tickets by 1, increase parkingSpaces by 1
        if  self.current_tickets['paid'] == True:
            self.tickets += 1
            self.parkingSpaces += 1
            print("Thank you! Have a nice day.")
                                
        else:
            print("Please pay for parking first.")

            
        useGarage()


def useGarage():   
    user_vehicle = input("Please enter your license plate info\n")
    customer = Garage(user_vehicle)
    while True:        
        user_action = input("Welcome to the Python Parking Garage! What would you like to do? Choose option 1-4\n 1 - Park\n 2 - Pay for parking\n 3 - Leave garage\n 4 - Quit\n")
        if user_action == '4':
            print('Goodbye!')
            return
        
        elif user_action == '1':
            customer.takeTicket()
            
            print("Please take your ticket.")
                        
        elif user_action == '2':
            customer.payForParking()
            
        elif user_action == '3':
            customer.leaveGarage()
            
        else:
            print("Please try again.")
            continue

useGarage()

