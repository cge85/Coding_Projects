# numbers =[1, 2, 3]
# new_list = []
# for n in numbers:
#     add_1 = n + 1
#     new_list.append(add_1)
# print(new_list)

# List Comprehension
# new_list = [new_item for item in list]
# new_list = [n + 1 for n in numbers]
# print(new_list)

# Conditional list comprehension
# new_list = [new_item for item in list if test]
# Show short names with less than 4 letters
# names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
# short_name = [ name for name in names if len(name) < 5]
# print(short_name)

# Show names more than 4 letters in uppercase
# names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
# long_names_upper = [name.upper() for name in names if len(name) > 5]
# print(long_names_upper)

# show list of squared numbers
# numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
# squared_numbers = [ number ** 2 for number in numbers]
# print(squared_numbers)

# Show filtered even numbers
# numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
# result = [e_num for e_num in numbers if e_num % 2 == 0]
# print(result)

# Show Data overlap numbers in file1 and file2
with open("file1.txt") as file1:
    read_file1 = file1.readlines()
    file1 = []
    for f1 in read_file1:
        file1.append(f1.replace("\n", ""))
with open("file2.txt") as file2:
    read_file2 = file2.readlines()
    file2 = []
    for f2 in read_file2:
        file2.append(f2.replace("\n", ""))

result = [int(num) for num in file1 if num in file2]
print(result)

# Angela code Will not get the correct results in VSC, but it will on replit
# with open("file1.txt") as file1:
#     file_1_data = file1.readlines()

# with open("file2.txt") as file2:
#     file_2_data = file2.readlines()

# result = [int(num) for num in file_1_data if num in file_2_data]
# print(result)