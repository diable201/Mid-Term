a = int(input())
my_list = []

for i in range(a):
    data = int(input())
    my_list.append(data)

peak = (max(my_list))
print(my_list.index(peak))