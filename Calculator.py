def start():
    question = input("Enter the question(exit to close): ")

    if question.lower() == "exit":
        close()
        return 0

    values = question.split(" ")
    if len(values) != 3:
        error()

    operator = values[1]
    a = values[0]
    b = values[2]

    analyze_question(a,b,operator)

def analyze_question(a,b,operator):
    if operator == '+':
        answer = add(a,b)
    elif operator == '-':
        answer = minus(a,b)
    elif operator == "x" or operator == "*":
        answer = multiply(a,b)
    elif operator == "/":
        answer = division(a,b)
    elif operator == "%":
        answer = modulus(a,b)
    else:
        error()

    try:
        print(f"Answer : {answer}")
        print()
    except:
        pass

    start()
    
def add(a,b):
    return(int(a) + int(b))

def minus(a,b):
    return(int(a) - int(b))

def multiply(a,b):
    return(int(a) * int(b)) 

def division(a,b):
    return(int(a) / int(b)) 

def modulus(a,b):
    return(int(a) % int(b)) 

def error():
    print("Invalid!!")
    print()

def close():
    print("______________________________________________________________________")
    print("                             Goodbye                                  ")
    print("----------------------------------------------------------------------")
    print("----------------------------------------------------------------------")

print("______________________________________________________________________")
print("                          Python calculator                           ")
print("----------------------------------------------------------------------")
start()