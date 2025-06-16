class ShoppingCart:
    def add_item(self, name, quantity=1):
        print(f"Adding {quantity} of {name} to the cart.")

cart = ShoppingCart()
cart.add_item("Apple")              
cart.add_item("Banana", 3)          