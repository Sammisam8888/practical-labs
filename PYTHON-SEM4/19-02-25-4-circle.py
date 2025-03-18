class Circle:
    def __init__(self, radius):
        self.radius = radius

    def calculatearea(self):
        return 3.14159 * self.radius * self.radius

    def calculateperimeter(self):
        return 2 * 3.14159 * self.radius

# Example usage
circle = Circle(5)
print(f"Area: {circle.calculatearea()}")
print(f"Perimeter: {circle.calculateperimeter()}")
