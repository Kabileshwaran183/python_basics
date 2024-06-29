def add(n1,n2):
    return n1+n2
def sub(n1,n2):
    return n1-n2
def mul(n1,n2):
    return n1*n2
def div(n1,n2):
    return n1/n2

def calculator():
    num1=float(input("Enter the first value : "))

    operations = {
        "+":add,
        "-":sub,
        "*":mul,
        "/":div,
    }
    for symbols in operations :
        print(symbols)
    should_continue = True
    while should_continue:    
        choose = input("choose one operation above:")
        num2=float(input("Enter the other value : "))
        calculation_symbol=operations[choose]
        result=calculation_symbol(num1,num2)
        print(f"{num1} {choose} {num2} = {result}")
        if input('Do you want to continue the calculations(type "y" - for continue or "no" - for another calculation) : ').lower() == "y" :
            num1 = result
        else:
            should_continue = False
            calculator()
calculator()
