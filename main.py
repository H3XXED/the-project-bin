import sqlite3
from School import Database_Creation

print('Welcome to the greatest activity finder ever!')
print('Loading activity list now this takes just a moment.')

"""call the function to create the database and populate it with activities"""
Database_Creation.create_database()


class Customer:
    def __init__(self):
        self.cart = []

    def view_cart(self):
        """Prints out the list of activities in the cart and the total price."""
        total_price = 0
        if not self.cart:
            print("Your cart is empty.")
        else:
            print("Activities in your cart:")
            for activity in self.cart:
                print(f"{activity[0]} - ${activity[3]}")
                total_price += activity[3]
            print(f"Total price: ${total_price}")

    def add_to_cart(self, activity_id):
        """Adds an activity to the cart."""
        conn = sqlite3.connect('activities.db')
        c = conn.cursor()
        c.execute("SELECT * FROM activities WHERE key=?", (activity_id,))
        activity = c.fetchone()
        if activity:
            self.cart.append(activity)
            print(f"Added: {activity[0]} to your cart.")
        else:
            print("Activity not found.")
        conn.close()

    def purchase_cart(self):
        """Empties the cart after the customer purchases the activities."""
        if not self.cart:
            print("Your cart is empty.")
        else:
            total_price = 0
            print("Thank you for your purchase of:")
            for activity in self.cart:
                print("- " + activity[0] + ": $" + str(activity[3]))
                total_price += activity[3]
            print("Total price: $" + str(total_price))
            self.cart = []


def show_activities():
    """Prints out the list of activities."""
    conn = sqlite3.connect('activities.db')
    c = conn.cursor()
    c.execute("SELECT * FROM activities")
    rows = c.fetchall()
    for row in rows:
        print(row)
    conn.close()


def browse_by_type():
    """Prints out choices for types of activities for user to choose and prints the list."""
    while True:
        conn = sqlite3.connect('activities.db')
        c = conn.cursor()
        c.execute("SELECT DISTINCT activity_type FROM activities")
        rows = c.fetchall()
        print('*********************************************************')
        print("Available types:")
        for row in rows:
            print(row[0])
        type_choice = input("Enter a type to browse (or q to return to main menu.): ")
        if type_choice == 'q':
            break
        c.execute("SELECT * FROM activities WHERE activity_type=?", (type_choice,))
        rows = c.fetchall()
        if not rows:
            print("Please make a choice from the list.")
        else:
            for row in rows:
                print(row)
        conn.close()


def browse_by_price():
    """Gives the user a max amount for price to choose and provides list of lower prices."""
    conn = sqlite3.connect('activities.db')
    c = conn.cursor()
    while True:
        try:
            price_choice = input("Enter a maximum price to browse (in USD) or q to return to main menu: ")
            if price_choice == 'q':
                break
            price_choice = float(price_choice)
            print('*********************************************************')
            c.execute("SELECT * FROM activities WHERE price<=?", (price_choice,))
            rows = c.fetchall()
            if not rows:
                print("No activities found within the price range.")
            else:
                for row in rows:
                    print(row)
        except ValueError:
            print("Please enter a valid number or q to return to main menu.")

    conn.close()


def main():
    """Creates the database and displays the menu list."""
    """create a new Customer instance"""
    customer = Customer()
    while True:
        print('*********************************************************')
        print("Select an option:")
        print("1. Show full activity list")
        print("2. Browse by type")
        print("3. Browse by price")
        print("4. View Cart")
        print("5. Add items to your cart.")
        print("6. Purchase the items in cart.")
        print("0. Exit")
        choice = input("Enter your choice: ")
        print('*********************************************************')
        if choice == "1":
            show_activities()
        elif choice == "2":
            browse_by_type()
        elif choice == "3":
            browse_by_price()
        elif choice == "4":
            customer.view_cart()
        elif choice == "5":
            activity_id = input("Enter the activity ID to add to your cart: ")
            customer.add_to_cart(activity_id)

        elif choice == "6":
            customer.purchase_cart()
        elif choice == "0":
            print('Thank you for using the ultimate Activity Finder!')
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
