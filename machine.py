import tkinter as tk
import os

#Base ui, but UI will only be impleted once the entire function is running in terminal
# def main():
#     # Create a Tkinter window
#     window = tk.Tk()

#     # Set the window title
#     window.title('My GUI App')

#     # Set the window size
#     window.geometry('300x200')

#     # Create a label
#     label = tk.Label(window, text='Hello, Tkinter!')
#     label.pack()

#     # Create a button
#     button = tk.Button(window, text='Click me!', command=on_button_click)
#     button.pack()

#     # Start the main event loop
#     window.mainloop()

# def on_button_click():
#     print('Button clicked!')

def display_items(items):
    for key, value in items.items():
        print(f"{key}: {value['name']} - RM{value['price']}")

def display_items_admin(items):
    for key, value in items.items():
        print(f"{key}: {value['name']} - RM{value['price']} - Quantity: {value['quantity']}")        

def add_item(items, key, name, price, quantity):
    items[key] = {'name': name, 'price': price, 'quantity': quantity}
    print("Item added successfully.")

def remove_item(items, key):
    if key in items:
        del items[key]
        print("Item removed successfully.")
    else:
        print("Item not found.")

def replace_item(items, key, name, price, quantity):
    if key in items:
        items[key] = {'name': name, 'price': price, 'quantity': quantity}
        print("Item replaced successfully.")
    else:
        print("Item not found.")

def admin_mode():
    os.system('cls')  
    attempt = 3
    while attempt > 0:
        pin_num = input("What is the 4-digit Pin Number for admin mode? You have " + str(attempt) + " attempts left.\n")
        if pin_num == "0000":
            while True:  # Use this loop to continuously display admin options until the user chooses to exit
                os.system('cls')
                print("You are now in admin mode")
                print("1. View Items")
                print("2. Add Items")
                print("3. Remove Items")
                print("4. Replace Items")
                print("5. Go back to Main Menu")
                admin_choice = input("Please choose an action in Admin Mode: ")

                if admin_choice == "1":
                    os.system('cls')
                    display_items_admin(items)
                    input("Press any key to return to Admin Mode.")
                elif admin_choice == "2":
                    max_key = max([int(k) for k in items.keys()], default=0)
                    new_key = str(max_key + 1)
                    key = new_key
                    name = input("Enter item name: ")
                    price = float(input("Enter item price: "))
                    quantity = int(input("Enter item quantity: "))
                    add_item(items, key, name, price, quantity)
                elif admin_choice == "3":
                    key = input("Enter item number to remove: ")
                    remove_item(items, key)
                elif admin_choice == "4":
                    key = input("Enter item number to replace: ")
                    name = input("Enter new item name: ")
                    price = float(input("Enter new item price: "))
                    quantity = int(input("Enter new item quantity: "))
                    replace_item(items, key, name, price, quantity)
                elif admin_choice == "5":
                    return  #Exit the admin mode and return to main menu
                else:
                    print("Invalid Choice. Please Try again.")
                    input("Press ENTER to try again.")  
        else:
            print("That is the wrong PIN code. You have " + str(attempt-1) + " attempts left.")
            attempt -= 1
            if attempt == 0:
                print("You typed the wrong code too many times. Returning to main menu.")
                break  # 3 attemps failed will go back to main menu
            input("Press ENTER to try again.")

#Just prefilling the vend machine with items we can use
items = {
        '1': {'name': 'Milo', 'price': 3.00, 'quantity': 10},
        '2': {'name': 'Cola', 'price': 2.00, 'quantity': 15},
        '3': {'name': 'Pepsi', 'price': 3.50, 'quantity': 20},
        '4': {'name': 'Teh Ais', 'price': 2.50, 'quantity': 12}
}

def main():
    while True:
        os.system('cls')  # TODO make it only run clear once, currently it keeps looping like crazy
        print("\nWelcome to the Vending Machine!")
        print("1. Display available items and prices")
        print("2. Admin Mode")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            display_items(items)
            print("Please choose what you would like to do")
            print("1. Purchase Item")
            print("2. Return to Main Menu")
            print("3. Exit the Vending Machine Menu")
            item_view_choice = input("Enter your choice of action: ")

            if item_view_choice == "1":
                selection = input("Enter the item number you wish to purchase: ")
                if selection in items:
                    selected_item = items[selection]
                    print(f"You have selected {selected_item['name']} - RM{selected_item['price']}")
                    amount_due = selected_item['price']

                    #Create debt when item has been selected
                    while amount_due > 0:
                        try:
                            payment = float(input(f"Please insert RM{amount_due:.2f}: "))
                            if payment >= amount_due:
                                change = payment - amount_due
                                print(f"Thank you for your purchase! Your change is RM{change:.2f}.")
                                items[selection]['quantity'] -= 1 
                                break
                            
                            else:
                                print("Insufficient payment. Please insert more money.")
                                amount_due -= payment
                        except ValueError: #Check if value is number or not
                            print("Invalid payment amount. Please enter a valid number.")
                else:
                    print("Invalid item selection.")

        elif choice == "2":
            admin_mode()
            continue
        elif choice == "3":
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
    

