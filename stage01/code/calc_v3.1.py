count=0
while True:
    operation=input("the operation: ")
    if operation=="q": 
            break
    first_number=float(input("the first number: "))
    second_number=float(input("the second number: "))
    count=count+1
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
print(f"已服务{count}次")