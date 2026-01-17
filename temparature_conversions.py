def ctof(c):
    return (c * 9/5) + 32

def ftoc(f):
    return (f - 32) * 5/9

while True:
    print("Temperature Converter")
    print("1.Celsius to Fahrenheit")
    print("2.Fahrenheit to Celsius")
    print("3.Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        c = float(input("Enter Celsius: "))
        print("Fahrenheit:", round(ctof(c), 2))

    elif choice == "2":
        f = float(input("Enter Fahrenheit: "))
        print("Celsius:", round(ftoc(f), 2))
    elif choice == "3":
        print("Thank you for using 😍")
        break

    else:
        print("Invalid option.")


