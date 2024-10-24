print(" 1. Addition \n 2. Subtraction \n 3. Multiplication \n 4. Division")
option =int(input("Enter your choice: "))
if option == 1:
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    print("Sum =",a+b)
elif option == 2:
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    print("Difference =",a-b)
elif option == 3:
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    print("Product =",a*b)
elif option == 4:
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    print("Quotient =",a/b)
else:
    print("Invalid option")