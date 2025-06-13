numbers = [1,2,3,4,5]
arrayOddnumbers = []
for num in numbers:
    if num % 2 == 1:
        arrayOddnumbers.append(num)
print(arrayOddnumbers)
arrayEvennumbers = []
for i in range(len(numbers)):
    if numbers[i] % 2 == 0:
        arrayEvennumbers.append(numbers[i])
print(arrayEvennumbers)
