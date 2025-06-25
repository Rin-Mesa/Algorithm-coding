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