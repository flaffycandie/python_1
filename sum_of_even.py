numbers=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
sum_of_even=0
for number in numbers:
    if number % 2 ==0:
        sum_of_even += number
print(f"The sum of even numbers is {sum_of_even}")
sum_of_all= 0
for i in numbers:
    sum_of_all += i
print(f'The sum of odd numbers is {sum_of_all}')
sum_of_odd=0
for number in numbers:
    if number % 2 !=0:
        print(f'{number} is odd')
        sum_of_odd += number
print(f'The sum of odd numbers is {sum_of_odd}')

# codility
# hackerrank
# leetcode
