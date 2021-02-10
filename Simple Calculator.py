# Simple calculator

#Addition func
def Suma():
    print("Addition")
    n = float(input("Write a number: "))
    t = 0
    ans = 0
    while n != 0:
        ans = ans + n
        t+= 1
        n = float(input("Write a number (or press 0 for the result) "))
    return [ans, t]

#Substraction func
def Resta():
    print("Substraction")
    n = float(input("Write a number: "))
    t = 0
    ans = 0
    while n != 0:
        ans = abs(ans) - n #absolute number ons ans 
        t+= 1
        n = float(input("Write a number (or press 0 for the result) "))
    return [ans, t]

#Multiplication func
def Multiplicacion():
    print("MULTIPLICATION")
    n = float(input("Write a number: "))
    t = 0
    ans = 1
    while n != 0:
        ans = ans * n
        t+= 1
        n = float(input("Write a number (or press 0 for the result) "))
    return [ans, t]

def Division():
    print("DIVISION")
    n1 = float(input("Write a number: "))
    t = 0
    ans = 0
    n2 = 1
    while n2 != 0:
        ans = n1 / n2
        t+= 1
        n2 = float(input("Write a number (or press 0 for the result) "))
    return [ans, t]
 
# Main
while True:
    list = []
    print("MY FIRST CALCULATOR")
    print("Press + to addition")
    print("Press - to substraction")
    print("Press * to multiplication")
    print("Press / to Division")
    print("Press Q to quit")
    c = input(" ")
    if c != "q":
        if c == "+":
            list = Suma()
            print("Answer = ", list[0], "Total inputs ", list[1])
        if c == "-":
            list = Resta()
            print("Answer = ", list[0], "Total inputs ", list[1])
        if c == "*":
            list = Multiplicacion()
            print("Answer = ", list[0], "Total inputs ", list[1])
        if c == "/":
            list = Division()
            print("Answer = ", list[0], "Total inputs ", list[1])

        else:
            print("invalid character")
    else:
        break



