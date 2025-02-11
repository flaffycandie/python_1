score=float(input("Enter your score: "))
if score>=90:
    grade= "Congratulations ! You scored an 'A' "
elif score>=80:
    grade= "Very Good ! You scored a 'B' "
elif score>=70:
    grade= "Average Performance You scored a 'C' "
elif score>= 60:
    grade= "Do better ! You scored a 'D' "
else:
    grade= "Poor Performance ! You scored an 'E' "
print(grade)