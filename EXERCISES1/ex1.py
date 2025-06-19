# q1.remove number 9
numbers  = [1,2,3,9,2,9,9,4]
# arrayNumbers = []
# for num in numbers:
#     if num != 9:
#         arrayNumbers.append(num)
# print(arrayNumbers)


# q2.change numbers 9 to 5
# for i in range(len(numbers)):
#     if numbers[i] == 9:
#         numbers[i] = 5
# print(numbers)


# q3. change first number 9 to 5
# numbers[3]=(5)
# print(numbers)


# q4.sum odd and even number
# even_sum = 0
# odd_sum = 0
# for num in numbers:
#     if num % 2 == 0:
#         even_sum += num
#     else:
#         odd_sum += num
# print("even number is:",even_sum,"odd number is",odd_sum)


# q5.count odd and even number
even_sum = 0
odd_sum = 0
for num in numbers:
    if num % 2 == 0:
        even_sum += 1
    else:
        odd_sum += 1
print("even number is:",even_sum,"odd number is",odd_sum)