sample_string = "Hello, World!"

print("Basic slicing:")
print("First five characters:", sample_string[:5])
print("Characters from index 7 to the end:", sample_string[7:])
print("Characters between index 3 and 8:", sample_string[3:8])
print()

print("Slicing with step:")
print("Every second character:", sample_string[::2])
print("Characters in reverse order:", sample_string[::-1])
print()

print("Negative indexing:")
print("Last five characters:", sample_string[-5:])
print("Characters from index -9 to -4:", sample_string[-9:-4])
print()

print("Slicing with specified step:")
print("Characters from index 1 to 10, with step 2:", sample_string[1:10:2])
print()

print("Omitting start and end index:")
print("All characters:", sample_string[:])
