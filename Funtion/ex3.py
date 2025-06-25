def upper_string(string):
    result = ""
    for i in range(len(string)):
        result += string[i].upper()
    return result

names = ['abc','him','rady']
new = []
for i in range(len(names)):
    new.append(upper_string(names[i]))
print(new)