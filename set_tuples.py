#sets examples:
set1 = {1, 2, 3, 4, 5}
print(set1)
print(type(set1))
set1.add(6)
print(set1)
set1.remove(2)
print(set1)
set2 = {"apple", "banana", "cherry", "cherry"}
print(set2) #remove duplicates

#tuples example
tuple1 = (1,2,3,4,5)
print(tuple1)
print(type(tuple1))
# tuples are immutable, cannot be changed
# useful for storing data that should not be changed
social_security_number = (123444, 4444445, 5676789)
print(social_security_number)