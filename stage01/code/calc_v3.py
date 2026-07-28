operation=input("the operation: ")
count=0
while operation=="q":
    exit()
while operation!="q":
    count=count+1
    first_number=float(input("the first number: "))
    second_number=float(input("the second number: "))
    print(f"serve times:{count}")
    if second_number==0 and operation=="/":
        print("Error: Division by zero is not allowed.")
    elif operation=="+":
        print(f"{first_number} + {second_number} = {first_number + second_number}")   
    elif operation=="-":
        print(f"{first_number} - {second_number} = {first_number - second_number}")
    elif operation=="*":
        print(f"{first_number} * {second_number} = {first_number * second_number}")
    elif operation=="/":
        print(f"{first_number} / {second_number} = {first_number / second_number}")
    else:
        print("Invalid operation")
    operation=input("the operation: ")

