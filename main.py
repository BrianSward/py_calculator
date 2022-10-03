from art import logo

#calc functions
def add(n1,n2):
    """adds one number to another"""
    return n1+n2

def sub(n1,n2):
    """minus one number to another"""
    return n1-n2
     
def mult(n1,n2):
    """multiply one number to another"""
    return n1*n2
    
def div(n1,n2):
    """divide one number to another"""
    return n1/n2


operations = {
    "+": add,
    "-": sub,
    "*": mult,
    "/": div
}
def calculator():
    print (logo)
    num1 = float(input("What is the first number: \n"))
    
    for op in operations:
        print (op)
    
    cont = True
    
    while cont:
        oper = input("What is the operator: \n")
        
        num2 = float(input("What is the next number: \n"))
        
        # my way below
        # if oper == "+":
        #     answer = add(num1,num2)
        # elif oper == "-":
        #     answer = sub(num1,num2)
        # elif oper == "*":
        #     answer = mult(num1,num2)
        # elif oper == "/":
        #     answer = div(num1,num2)
        # else:
        #     print ("invalid operator")
        
        #her way below - much shorter
        calc = operations[oper]
        answer = calc(num1,num2)
        
        print(f"{num1} {oper} {num2} = {answer}")
        
        response = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to exit.\n")
        if response == "y":
            num1 = answer
        else:
            cont = False
            calculator()


calculator()
