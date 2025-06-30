# # 1 

# user_input = int(input("Please enter 7: "))
# while user_input != 7:
#     user_input = int(input("Try again: "))


# 2

# is_seven = False

# while not is_seven:
#     user_input = int(input("Please enter 7: "))
#     if user_input == 7:
#         is_seven = True
#         print("Correct!")

# 3

# email = input("Input email:")
# pws = input("Input password:")
# while email != "admin@gmail.com" and pws != "12345678":
#     print("Your gmail invalid")
#     email = input("Input email:")
#     pws = input("Input password:")

# # 4

# email = input("Input email:")
# pws = input("Input password:")
# count = 1
# while email != "admin@gmail.com" and pws != "12345678" and count < 3:
#     count += 1
#     print("Your gmail invalid")
#     email = input("Input email:")
#     pws = input("Input password:")
# if count >= 3:
#     print("Your try more tree times will lock")


# # 5
# def validate(email, psw):
#     correct = False
#     if email == "admin@gmail.com" and psw == "12345678":
#         correct = True
#     return correct

# email = input("Input email:")
# psw = input("Input password:")
# count = 1
# while not validate(email,psw) and count<3:
#     count += 1
#     print("Your gmail invalid")
#     email = input("Input email:")
#     psw = input("Input password:")
# if count>=3:
#     print('Your try more tree times will lock')

# # 6 
# def remove_minus(string):
#     result = ""
#     for char in string:
#         if char != "-":
#             result += char
#     return result
# is_countinue = True

# while is_countinue:
#     word = input("Enter word with minus:")
#     print(f'You word without minus is {remove_minus(word)}')
#     check = input("Do you want to continue ('Y/N'):")
#     if check.upper() != "Y":
#         is_countinue = False


# # 7

# def sum(num1, num2):
#     return num1 + num2

# num1 = int(input("Num1:"))
# num2 = int(input("Num2:"))

# print(sum(num1,num2))


# # 8

# def sum(num1, num2):
#     return num1 + num2

# total = 0
# count = int(input("Number of values: "))
# for i in range(count):
#     num = int(input(f'Value {i}:'))
#     total = sum(total,num)

# print(total)

# 9
def sum(num1, num2):
    return num1 + num2

start = int(input("Start value: "))
end = int(input("End value: "))

total = 0
for i in range(start, end + 1):
    total = sum(total, i)

print(f'The sum of numbers between {start} and {end} is : {total}')
