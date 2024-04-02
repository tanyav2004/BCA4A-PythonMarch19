
size = int(input("Enter the size of the list: "))
my_list = []

for i in range(size):
    num = int(input("Enter element: "))
    my_list.append(num)

print("List before sorting:", my_list)

my_list.sort()

print("List after sorting:", my_list)
