class Circle:
    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        return 3.14159 * self.radius * self.radius

    def calculate_perimeter(self):
        return 2 * 3.14159 * self.radius

# Example usage
circle = Circle(5)
print(f"Area: {circle.calculate_area()}")
print(f"Perimeter: {circle.calculate_perimeter()}")
