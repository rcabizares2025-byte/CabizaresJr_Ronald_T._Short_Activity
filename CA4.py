list = ["Alice", "Bob", "Carol", "Dave"]
print()

list.append("Eve")    
list.insert(1, "Frank")     

list.remove("Carol")

list.sort()

print("Sorted list:")
for name in list:
    print(name)
