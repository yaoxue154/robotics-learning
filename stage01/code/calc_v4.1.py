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
def calculate(a, b, op):
    if op == "+":
        return add(a, b)
    elif op == "-":
        return subtract(a, b)
    elif op == "*":
        return multiply(a, b)
    elif op == "/":
        return divide(a, b)
service_times = 0
while True:
    operation = input("请输入操作符 (+, -, *, /) 或 'q' 退出: ")
    if operation == "q":
        print("退出计算器。")
        break
    elif operation not in ["+", "-", "*", "/"]:
        print("无效的操作符，请输入 +, -, *, / 或 'q' 退出。")
        continue
    a = float(input("请输入第一个数字:"))
    b = float(input("请输入第二个数字:"))
    result = calculate(a, b, operation)
    if result is not None:
        print(f"结果: {result}")
        service_times += 1
print(f"服务次数: {service_times}")