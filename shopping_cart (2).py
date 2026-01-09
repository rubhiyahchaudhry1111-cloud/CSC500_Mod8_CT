"""
Online Shopping Cart - Portfolio Project
Implements ItemToPurchase and ShoppingCart with a menu-driven interface.

Compatible with ZyBooks / introductory Python environments.
"""

from dataclasses import dataclass
from typing import List


def fmt_money(value: float) -> str:
    """Format money without trailing .0 when value is whole."""
    return f"{value:g}"


@dataclass
class ItemToPurchase:
    item_name: str = "none"
    item_description: str = "none"
    item_price: float = 0.0
    item_quantity: int = 0

    def print_item_cost(self) -> None:
        total = self.item_price * self.item_quantity
        print(f"{self.item_name} {self.item_quantity} @ ${fmt_money(self.item_price)} = ${fmt_money(total)}")


class ShoppingCart:
    def __init__(self, customer_name: str = "none", current_date: str = "January 1, 2020"):
        self.customer_name = customer_name
        self.current_date = current_date
        self.cart_items: List[ItemToPurchase] = []

    def add_item(self, item: ItemToPurchase) -> None:
        self.cart_items.append(item)

    def remove_item(self, item_name: str) -> None:
        for i, item in enumerate(self.cart_items):
            if item.item_name == item_name:
                del self.cart_items[i]
                return
        print("Item not found in cart. Nothing removed.")

    def modify_item(self, item: ItemToPurchase) -> None:
        """Modify description, price, and/or quantity of an existing item."""
        for existing in self.cart_items:
            if existing.item_name == item.item_name:
                if item.item_description != "none":
                    existing.item_description = item.item_description
                if item.item_price != 0:
                    existing.item_price = item.item_price
                if item.item_quantity != 0:
                    existing.item_quantity = item.item_quantity
                return
        print("Item not found in cart. Nothing modified.")

    def get_num_items_in_cart(self) -> int:
        return sum(item.item_quantity for item in self.cart_items)

    def get_cost_of_cart(self) -> float:
        return sum(item.item_price * item.item_quantity for item in self.cart_items)

    def print_total(self) -> None:
        print(f"{self.customer_name}'s Shopping Cart - {self.current_date}")
        num_items = self.get_num_items_in_cart()
        print(f"Number of Items: {num_items}")

        if not self.cart_items:
            print("\nSHOPPING CART IS EMPTY")
            print(f"\nTotal: ${fmt_money(0)}")
            return

        for item in self.cart_items:
            item.print_item_cost()
        print(f"Total: ${fmt_money(self.get_cost_of_cart())}")

    def print_descriptions(self) -> None:
        print(f"{self.customer_name}'s Shopping Cart - {self.current_date}")
        print("Item Descriptions")
        for item in self.cart_items:
            print(f"{item.item_name}: {item.item_description}")


def print_menu(cart: ShoppingCart) -> None:
    menu = (
        "MENU\n"
        "a - Add item to cart\n"
        "r - Remove item from cart\n"
        "c - Change item quantity\n"
        "i - Output items' descriptions\n"
        "o - Output shopping cart\n"
        "q - Quit\n"
    )

    choice = ""
    while choice != "q":
        print(menu)
        choice = input("Choose an option:\n").strip().lower()

        while choice not in {"a", "r", "c", "i", "o", "q"}:
            choice = input("Choose an option:\n").strip().lower()

        if choice == "a":
            print("ADD ITEM TO CART")
            name = input("Enter the item name:\n")
            desc = input("Enter the item description:\n")
            price = float(input("Enter the item price:\n"))
            qty = int(input("Enter the item quantity:\n"))
            cart.add_item(ItemToPurchase(name, desc, price, qty))
            print()

        elif choice == "r":
            print("REMOVE ITEM FROM CART")
            name = input("Enter name of item to remove:\n")
            cart.remove_item(name)
            print()

        elif choice == "c":
            print("CHANGE ITEM QUANTITY")
            name = input("Enter the item name:\n")
            qty = int(input("Enter the new quantity:\n"))
            cart.modify_item(ItemToPurchase(item_name=name, item_quantity=qty))
            print()

        elif choice == "i":
            print("OUTPUT ITEMS' DESCRIPTIONS")
            cart.print_descriptions()
            print()

        elif choice == "o":
            print("OUTPUT SHOPPING CART")
            cart.print_total()
            print()


def main() -> None:
    customer_name = input("Enter customer's name:\n")
    current_date = input("Enter today's date:\n")
    print(f"\nCustomer name: {customer_name}")
    print(f"Today's date: {current_date}\n")

    cart = ShoppingCart(customer_name, current_date)
    print_menu(cart)


if __name__ == "__main__":
    main()
