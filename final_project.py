"""
ASSIGNMENT 9B: SPRINT 2 - FUNCTIONAL STUBS
Project: Ghost's Pizzeria
Developer: Caleb Casper
"""

TOPPINGS = ("Pepperoni (+$1.00)", "Sausage (+$1.00)", "Bacon (+$2.00)", "Cheese")
STYLE = ("Thin", "Regular", "Deep dish")
DRINK = ("Water", "Coke (+$2.00)", "Tea (+$2.00)")


class PizzaOrder:
    def __init__(self, name, location, size, topping, style, drink):
        self.__name = name
        self.__location = location
        self.__size = size
        self.__topping = topping
        self.__style = style
        self.__drink = drink

    # Getters
    def get_name(self):
        return self.__name

    def get_location(self):
        return self.__location

    def get_size(self):
        return self.__size

    def get_topping(self):
        return self.__topping

    def get_style(self):
        return self.__style

    def get_drink(self):
        return self.__drink

    # Setters
    def get_size(self, size):
        if size in ("Small", "Medium", "Large"):
            self.__size = size

    def set_topping(self, topping):
        self.__topping = topping

    def set_drink(self, drink):
        self.__drink = drink

    # Calculating total (for final project)
    def calculate_total(self):
        if self.__size == "Small":
            size_total = 3.00
        elif self.__size == "Medium":
            size_total = 5.00
        else:
            size_total = 6.00
        if self.__topping == "Bacon":
            topping_total = 2.00
        elif self.__topping == "Pepperoni" or self.__topping == "Sausage":
            topping_total = 1.00
        else:
            topping_total = 0
        if self.__drink == "Water":
            drink_total = 0
        else:
            drink_total = 2.00
        return size_total + topping_total + drink_total

    # Order Summary
    def order_summary(self):
        total = self.calculate_total()
        return (
            f"-Order Summary-\n"
            f"Customer name: {self.__name}\n"
            f"Location: {self.__location}\n"
            f"Size: {self.__size}\n"
            f"Topping: {self.__topping}\n"
            f"Order total: ${total:.2f}"
        )


def get_customer_info():
    name = input("Please enter your name:")
    location = input("Please enter a location for your order:")
    return name, location


def take_order():
    print("--Welcome to Ghost's Pizzeria!--")
    while True:
        size = (
            input("Please select a size for your pizza (Small/Medium/Large):")
            .title()
            .strip()
        )
        print("Toppings (Additional fees may apply.): ", TOPPINGS)
        toppings = input("Please select a topping for your pizza:").title().strip()
        print("Styles: ", STYLE)
        style = input("Please select a style: ").title().strip()
        print("Drinks (Additional fees may apply.): ", DRINK)
        drink = input("Please select a drink:").title().strip()
        delivery_choice = (
            input("Please choose either pickup or delivery: ").title().strip()
        )
        finalize_order = (
            input(
                "Type 'C' to confirm your order (Or type E to edit, and X to cancel):"
            )
            .upper()
            .strip()
        )
        if finalize_order == "C":
            print("Order Confirmed! Thank you.")
            return size, toppings, drink, style
        elif finalize_order == "E":
            print("Please make any change you'd like.")
        elif finalize_order == "X":
            print("Order Cancelled")
            exit()
        else:
            print("Invalid input.")


def main():
    name, location = get_customer_info()
    size, toppings, drink, style = take_order()
    order = PizzaOrder(name, location, size, toppings, style, drink)
    print(order.order_summary())


main()
