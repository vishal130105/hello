import cmath

print("Hello there!")
name = str(input("Name: "))
print("Hey "+name+"\nWelcome To Roots of Quadratic equation")
print("\n-----------------------------------------------------------------------\n")
print("\nA quadratic equation, f(x) is given by\n\tf(x) = Ax^2 + B^x + C")
print("\n\t where A and B are coefficients of x^2 and x and C is constant and A!=0")
print("\n-----------------------------------------------------------------------\n")

A = float(input("Enter value of A -> "))
B = float(input("Enter value of B -> "))
C = float(input("Enter value of C -> "))
print("Your entered equation is\n\t f(x) = ({0})x^2 + ({1})x + ({2})".format(A,B,C))

D = (B**2) - (4*A*C)

root1 = (-B-cmath.sqrt(D))/(2*A)
root1 = round(root1.real,3) + round(root1.imag,3)*1j
root2 = (-B+cmath.sqrt(D))/(2*A)
root2 = round(root2.real,3) + round(root2.imag,3)*1j

print("The solution to the equation is\n\t{0} & {1}".format(root1,root2))