# 4. Function Returning Multiple Values
# Problem: Create a function that returns both the area and circumference of a circle given its radius.
import math as m

def circle_stats(radius):
    circumference =  2* m.pi * radius
    area = m.pi * (radius ** 2)
    return area, circumference

radius = float(input("Enter your radius in cm : "))

area, circumference = circle_stats(radius)

print("Area of circle is", round(area, 2))
print(f"Circumference of circle is {circumference:.2f}")