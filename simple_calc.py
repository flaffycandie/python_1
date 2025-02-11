# Prompt user first number
num1=float(input("Enter First Number"))
# prompt user to select operator
operator=input("Enter operator: (+, -, *, /, %, **, //)")
# Prompt user second number
num2=float(input("Enter Second number"))
# perform calculation
if operator=='+':
    answer: num1+num2
elif operator=='-':
    answer= num1-num2
elif operator=='*':
    answer= num1*num2
elif operator=='/':
    if num2 !=0:
        answer= num1/num2
    else:
        print("ERROR, Division by zero")
elif operator=='%':
            answer= num1%num2
elif operator=='**':
    answer= num1**num2
elif operator=='//':
    answer= num1//num2
else:
    answer="Sorry, Invalid Operator"
print(f"Thank you, Your result is {answer}")


