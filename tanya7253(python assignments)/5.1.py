my_list = [10, 20, 30, 40, 50]

print("First element:", my_list[0])
print("Last element:", my_list[-1])

print("Sliced list:", my_list[1:4])

my_list[2] = 35
print("Modified list:", my_list)

my_list.append(60)
print("After appending:", my_list)

my_list.remove(20)
print("After removal:", my_list)

print("Length of the list:", len(my_list))

print("Is 30 in the list?", 30 in my_list)

new_list = [70, 80, 90]
combined_list = my_list + new_list
print("Combined list:", combined_list)
