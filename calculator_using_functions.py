#addition function 
def add(a,b):
                return a+b
#subtraction function 
def sub(a,b):
    return a-b
#multiplication function     
def multiply(a,b):
              return a*b
#division function 
def div(a,b):
                   if b==0:
                       return "division not possible"
                   else:
                       return a/b              
#power function
def power(a,b):
                 return a**b
#modulus function
def modulus(a,b):
                 if b==0:
                     return "not possible"
                 else:
                     return a%b  
#floor division 
def floor_div(a,b):
                  if b==0:
                      return "cannot divide by zero"
                  else:
                      return a//b
#square function                                       
def square(a):
    return a*a                                
#sqrt function 
def sqrt(a):
    return a**0.5   
#even odd function
def even_odd(a):
    if a%2==0:
        return "even"    
    else:
        return "odd"   
#maximum function 
def maximum (a,b):
    if a > b:
        return a 
    else:
        return b
#swap function 
def swap(a,b):
    return b,a
print ("___ Calculator ___")
#list of operations
print ("\nlist of operations:")
print ("1.addition")
print ("2.subtraction")
print ("3.multiplication")
print ("4.division")
print ("5.power")
print ("6.module")
print ("7.floor division")
print ("8.square")
print ("9.sqrt")
print ("10.even_odd")
print ("11.maximum")
print ("12.swap")
print ("13.exit")

#user input
print ("\n--- User Input ---")
x=int(input("enter 1st integer value:"))
y=int(input("enter 2nd integer value:"))
n=int(input("\nenter number of chances to perform operations : "))
for i in range(n):
    print (f"\nchance {i+1}")
    #user input for which operation perform 
    user_operation=int(input("enter number for operation "))
    match user_operation:
        case 1 :
            print (f"addition of {x} & {y} is {add(x,y)}")
        case 2:
         print (f"subtraction of {x} & {y} is {sub(x,y)}")
        case 3:
            print (f"multiplication of {x} & {y} is {multiply(x,y)}")
        case 4:
            print (f"division of {x} & {y} is {div(x,y):.2f}")
        case 5:
            print( f"power of {x} & {y} is {power(x,y)}")
        case 6:
            print(f"modulus of {x} & {y} is {modulus(x,y)}")
        case 7:
             print (f"floor division of {x} & {y} is {floor_div(x,y)}")
        case 8:
            print(f"square of {x} is {square(x)}")
        case 9:
            print(f"sqrt of {x} is {sqrt(x):.2f}")
        case 10:
            print (f"{x} is {even_odd(x)}")
        case 11:
            print (f"maximum of {x} & {y} is {maximum(x,y)}")
        case 12:
            a,b = swap(x,y)
            print(f"after swapping: {a} & {b}")
        case 13:
             print ("close calculator")
             break 
        case _:
            print("out of bound operation ")


