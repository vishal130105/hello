print("Hello there!\n")
name=input("Enter your name: ")
print("\nWelcome",name,"to Powers/Exponent calculation of a number in Python.")
print("\n*For Example: 2 raised to power 10 (i.e. 2^10) =",2**10)
print(" In this example, 2 is known as Base/Index Value & 10 is known as power/exponent.")

index = int(input("\nEnter base Index Value: "))

power = int(input("\nEnter the power/exponent: "))

result = index**power

print("\nThe number",index,"raised to the power",power,"is equals to",result)
print("\n\nThanks",name,"for using my program!")
