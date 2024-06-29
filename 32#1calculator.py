def add(n1,n2):
    return n1+n2
def sub(n1,n2):
    return n1-n2
def mul(n1,n2):
    return n1*n2
def div(n1,n2):
    return n1/n2

num1=int(input("Enter the first value : "))

operations = {
    "+":add,
    "-":sub,
    "*":mul,
    "/":div,
}

for symbols in operations :
    print(symbols)
choose = input("choose one operation above:")
num2=int(input("Enter the other value : "))
calculation_symbol=operations[choose]
result=calculation_symbol(num1,num2)
print(f"{num1} {choose} {num2} = {result}")
