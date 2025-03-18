class ShoppingBag:
    def __init__(self):
        self.items = []

    def additem(self, itemname, price):
        self.items.append({'name': itemname, 'price': price})

    def removeitem(self, itemname):
        self.items = [item for item in self.items if item['name'] != itemname]

    def calculatetotalprice(self):
        return sum(item['price'] for item in self.items)

# Example usage
bag = ShoppingBag()
bag.additem("Apple", 1.5)
bag.additem("Banana", 0.75)
print(f"Total Price: {bag.calculatetotalprice()}")
bag.removeitem("Apple")
print(f"Total Price after removing Apple: {bag.calculatetotalprice()}")
