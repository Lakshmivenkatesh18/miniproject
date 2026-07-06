#Display welcome message

print("Simple calculator")
print("-----------------")

#Get numbers from user

num1=float(input("Enter the first number : "))
num2=float(input("Enter the second number : "))

#ask which operation to be performed

print("Choose operation : ")
print("1. Addition")
print("2. Substraction ")
print("3. Multiplication ")
print("4. Division")

choice=input("Enter your choice (1/2/3/4) : ")

#perform calculation

if choice =="1":
    print("Result =",num1+num2)
elif choice=="2":
    print("Result = ",num1-num2)
elif choice=="3":
    print ("Result = ",num1*num2)
elif choice=="4":
    if num2 !=0:
        print("Result:= ",num1/num2)
    else:
        print("cannot divided with zero")
else :
    print("Inavlid choice")

