print("Choose an option:")
print("1. Area of Triangle")
print("2. Area of Rectangle")

choice = int(input("Enter your choice (1 or 2): "))

if choice == 1:
    base = float(input("Enter base of the triangle: "))
    height = float(input("Enter height of the triangle: "))
    area = area_of_triangle(base, height)
    print("Area of Triangle =", area)

elif choice == 2:
    length = float(input("Enter length of the rectangle: "))
    width = float(input("Enter width of the rectangle: "))
    area = area_of_rectangle(length, width)
    print("Area of Rectangle =", area)
