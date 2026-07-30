def add(a, b):
    return a + b
def subtract(a, b):
    return a - b
def multiply(a, b):
    return a * b        
def divide(a, b):
    if b == 0:
        print("Cannot divide by zero.")
        return None
    return a / b
service_times=0
while True:
    success_service=False
    result = None
    operation = input("请输入操作符 (+, -, *, /) 或 'q' 退出: ")
    if operation== "q":
        print("退出计算器。")
        break
    elif operation not in ["+", "-", "*", "/"]:
        print("无效的操作符，请输入 +, -, *, / 或 'q' 退出。")
        continue
    a=float(input("请输入第一个数字:"))
    b=float(input("请输入第二个数字:"))
    if operation == "+":
        result = add(a, b)
        success_service=True
    elif operation == "-":
        result = subtract(a, b)
        success_service=True
    elif operation == "*":
        result = multiply(a, b)
        success_service=True
    elif operation == "/":
        result = divide(a, b)
        if result is not None:
            success_service=True
        elif result is None:
            print("除数为零，无法计算结果。")
    else:
        print("Invalid operation.")
    if success_service==True:
        service_times=service_times+1
    print(f"结果: {result}")
print(f"服务次数: {service_times}")