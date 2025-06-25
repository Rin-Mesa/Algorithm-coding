

def reverse_string(string):
    result = ""
    for i in range(len(string)):
        result += string[len(string)-i-1]
    return result

new_array = []
names = ['abc','him','rady']
for i in range(len(names)):
    new_array.append(reverse_string(names[i]))
print(new_array)


def upper_string(string):
    result = ""
    for i in range(len(string)):
        # print(string[i].upper())
        result += string[i].upper()
    return result

names = ['abc','him','rady']
new = []
for i in range(len(names)):
    new.append(upper_string(names[i]))
print(new)




def count_a(string):
    count = 0
    for i in range(len(string)):
        if string[i] == 'a':
            count += 1
    return count

new_arr = []
names = ['natiya','yatoya','rady']
for i in range(len(names)):
    new_arr.append(count_a(names[i]))
print(new_arr)


