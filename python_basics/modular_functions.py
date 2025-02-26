 # modular_functions.py

import math

# Function to calculate area of different shapes
def calculate_area(shape, dimension1, dimension2=0):
    if shape == "circle":
        return math.pi * (dimension1 ** 2)
    elif shape == "rectangle":
        return dimension1 * dimension2
    elif shape == "triangle":
        return 0.5 * dimension1 * dimension2
    else:
        return "Invalid shape"

# Testing the function with different shapes
print("Area of circle (radius=5):", calculate_area("circle", 5))
print("Area of rectangle (length=4, width=6):", calculate_area("rectangle", 4, 6))
print("Area of triangle (base=3, height=7):", calculate_area("triangle", 3, 7))