from factorial.factorial import fact
from exp_root.exponentiation import exp2
from exp_root.exponentiation import exp3
from exp_root.root import root2
from exp_root.root import root3
from logarithm.logarithm import log
from logarithm.logarithm import lg
from logarithm.logarithm import ln

def main(ch):
    """
    This function is print result for the selected function 
    """
    try:
        # Here is the search and launch of the selected function
        if ch == '1':
            result = fact(int(input("Factorial for ")))
        if ch == '2':
            result = exp2(float(input("Square exponention for ")))                                                         
        if ch == '3':
            result = exp3(float(input("Cube exponention for ")))
        if ch == '4':
            result = root2(float(input("Square root for ")))
        if ch == '5':
            result = root3(float(input("Cube root for ")))
        if ch == '6':
            a = float(input("Enter a base for this logarithm: "))
            b = float(input("Enter b in this logarithm: "))
            result = log(a,b)
        if ch == '7':
            b = float(input("Enter b in this logarithm: "))
            result = lg(b)
        if ch == '8':
            b = float(input("Enter b in this logarithm: "))
            result = ln(b)
        # Here is output result
        print("Result:",result)
    except ArithmeticError:
        print("Incorrect a values")

if __name__ == "__main__":
    print('='*80)
    # Here is input guide this program
    print("Enter '1' if you want use factorial for n")
    print("Enter '2' if you want use a square exponention for n")
    print("Enter '3' if you want use a cube exponention for n")
    print("Enter '4' if you want use a square root for n")
    print("Enter '5' if you want use a cube root for n")
    print("Enter '6' if you want use a daily logarithm")
    print("Enter '7' if you want use a decimal logarithm")
    print("Enter '8' if you want use a natural logarithm")
    print("To close program enter Ctr + Z")
    print('='*80)
    # Here the loop is repeated indefinitely
    while True:
        try:
            # Here to wait a choice
            choise = input("Your choise: ")
            # Here to check a choise
            if not choise in ['1','2','3','4','5','6','7','8']:
                raise ValueError("This variant choise does not exist")
            # Start a choise function
            main(choise)
            print('='*80)
        except EOFError:
            # System exit and broke the loop
            exit("Program is close")
        except ValueError as iden:
            # Here is print identifier 
            print("Incorrect a values")



            
    