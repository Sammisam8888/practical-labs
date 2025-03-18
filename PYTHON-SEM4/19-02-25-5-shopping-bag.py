class ShoppingBag:
    def __init__(self):
        self.items = []

    def add_item(self, item_name, price):
        self.items.append({'name': item_name, 'price': price})

    def remove_item(self, item_name):
        self.items = [item for item in self.items if item['name'] != item_name]

    def calculate_total_price(self):
        return sum(item['price'] for item in self.items)

# Example usage
bag = ShoppingBag()
bag.add_item("Apple", 1.5)
bag.add_item("Banana", 0.75)
print(f"Total Price: {bag.calculate_total_price()}")
bag.remove_item("Apple")
print(f"Total Price after removing Apple: {bag.calculate_total_price()}")
