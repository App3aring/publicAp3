import tkinter

def add(x,y):
    return x + y
def subtract(x,y):
    return x - y
def multiply(x,y):
    return x * y 
def divide(x,y):
    return x / y
print("Select Operation.")
print("1.add")
print("2.subtract")
print("3.multiply")
print("4.divide")
while True:
    choice = input("Enter Your Choice!(1/2/3/4): ")
    if choice in ('1', '2', '3', '4'):
        number1 =float(input("Enter First Number: "))
        number2 =float(input("Enter Second Number: "))
        if choice == '1':
            print(number1, "+", number2, "=", add(number1, number2))
        elif choice == '2':
            print(number1, "-", number2, "=", subtract(number1, number2))
        elif choice == '3':
            print(number1, "*", number2, "=", multiply(number1, number2))
        elif choice == '4':
            print(number1, "/", number2, "=", divide(number1, number2))
        break
    else:
        print("Entered Input is Invalid")
        