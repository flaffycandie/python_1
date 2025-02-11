weight=float(input("Enter your Weight In Kilograms"))
height=float(input("Enter your Height in metres"))
BMI= (weight/(height**2))
print(f"Your Body Weight in kilograms is {weight}")
print(f"Your Body Height in centimetres is {height}")
print(f"Your Body Mass Index is {BMI:.2f}")
if BMI<=18.5:
    print("You are unfortunately underweight, Attempt to eat more. Thank You")
elif BMI>=18.5:
    print("Congratulations ! Healthy Body Mass Index (BMI). Good Work. Thank You")
elif BMI>=24.9:
    print("You are sadly overweight, Please attempt to eat less. Thank You")
elif BMI>=30.0:
    print("Unhealthy Body Mass Index (BMI). Embark on weight loss to avoid complications. Thank You")
elif BMI>=35.0:
    print("Extreme Obesity, Please seek medical advice. Thank You")
