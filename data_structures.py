# list_data_structure
# lists are mutable
# lists are ordered
# lists are indexed
fruits=['apple', 'banana', 'mango', 'orange','pineapple', 'pear']
fruits[0]="Watermelon"
numbers=[1, 2, 3, 4, 5, 6, 7, 8]
numbers2=[34, 576,45, 90, 76, 47, 54]
print(numbers)
print(fruits)
print(f"I love eating {fruits[3]}")
numbers.append(11)
print(numbers)
numbers2.sort(reverse=True)
print(numbers2)
# tuple_data_structure
# tuple is immutable
# tuple is ordered
# tuple is indexed
cars=('audi','toyota', 'subaru', 'mercedes', 'honda')
# cars[0]='bentley'
print(cars)
nambari=(43, 46, 239, -187, -48, 148, 3489, -256, -57, 190, 25, -981, 34, 85, 52)
print(cars)
print(sorted(nambari))
# set_data_structure
# set is unordered
# set lacks index
computers= {"HP", "Asus", "Lenovo", "Toshiba", "Acer", "Mac"}
computers.add("google")
print(computers)
num1={1, 2 ,3}
num2={4, 5, 6}
union_set=num1.union(num2)
# dictionary_data_structure
student={'name':'John', 'Age':5, 'Gender': 'Male', 'School':'University of Nairobi'}
print(student ['name'])
print(f'The name is {student['name']}')
print(f'The students gender is {student['Gender']}')
print(f'The students school is {student['School']}')
print(f'The students name is {student['name']} and his gender is {student['Gender']}, he studies in {student['School']} ')