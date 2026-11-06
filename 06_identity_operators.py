
# Identity Operators: is and is not

list1 = [10, 20, 30]
list2 = list1
list3 = [10, 20, 30]

print("list1 is list2:", list1 is list2)
print("list1 is list3:", list1 is list3)

print("list1 is not list3:", list1 is not list3)
print("list2 is not list3:", list2 is not list3)
