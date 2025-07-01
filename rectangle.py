import calculate

length = float(input("Enter the lenght of the Rectangle: "))
width = float(input("Enter the width of the Rectangle: "))

area = calculate.area(length, width)
perimeter = calculate.perimeter(length, width)

print(f"The area of the Rectangle is: {area}")
print(f"The perimeter of the Rectangle is: {perimeter}")