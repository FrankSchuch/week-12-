# Objective:
# Students will understand how to create, modify, and access elements in Python lists.

# Topics Covered:
# Creating lists, indexing, slicing, appending, popping, sorting, reversing.
#lists are part of collections family in Python'
#Creating a list

#collections are used to store multiple items in a single variable
#lists are mutable, meaning you can change their content
#lists are created using square brackets []
# my_list1 = [1,2,3,4,5]
# print(my_list1) # [1, 2, 3, 4, 5]
# print(type(my_list1)) # <class 'list'>
# #Instead of typing a bunch of variables we can store them in a list.
# #This makes our job easier when we need to manage multiple itmes.
# #performance task answer
# #Access elements
# print(my_list1[0]) #1
# print(my_list1[1:4]) #[2,3,4]
# print(my_list1[0:]) #[1, 2, 3, 4, 5]
# #Modifying lists
# #Adding an item to the end of the list
# my_list1.append(6)
# print(my_list1) # [1, 2, 3, 4, 5, 6]
# my_list1.extend([10,11,12,13,14])
# print(my_list1)
# # my_list1.append(7)
# # print(my_list1) # [1, 2, 3, 4, 5, 6, 7]
# # my_list1.append(8)
# # print(my_list1) # [1, 2, 3, 4, 5, 6, 7, 8]
# #  # Examples:
# #add 500 more numbers to the list
# my_list1.extend(list(range(15,515)))
# print(my_list1)
# #add 600 more
# my_list1.extend(list(range(515, 1115)))
# print(my_list1)

new_list = ['a', 'b', 'c']
print(new_list) 
new_list.append('d')
print(new_list)
#removing an item from the list
removed_item = new_list.pop()
print(removed_item) #d
print(new_list)
remove_second_item = new_list.pop(1)
print(remove_second_item)
print(new_list)

#Sorting the list
numbers = [4, 2, 5, 1, 3]
numbers.sort()
print(numbers) # [1, 2, 3, 4, 5]
#Reversing the list
numbers.reverse()
print(numbers) # [5, 4, 3, 2, 1]
#inserting an item at a specific position
numbers.insert(2,10)
print(numbers)
# removed_number = numbers.pop() #remove last number
# numbers.append(15) #insert different number
# print(numbers)
third_list = [7, 8, 9]
third_list[0] = 6
print(third_list) #6, 8, 9
third_list[-1] = 10
print(third_list)
import random
random_list = random.sample(range(1, 100), 10)
#prints 10 random numbers from 1-100
print(random_list)
print(sorted(random_list))
sorted_list = sorted(random_list)
print(sorted_list)
#reverse the list
#remove every 3rd item from the list
sorted_list.reverse()
print(sorted_list)
newer_list = sorted_list[::3]
print(newer_list)

# my_list = ['apple', 'banana', 'cherry']
# print(my_list[0])         # apple
# print(my_list[1:])        # ['banana', 'cherry']

# my_list.append('grape')
# print(my_list)

# my_list.pop(1)
# print(my_list)

# numbers = [3, 1, 4, 2]
# numbers.sort()
# print(numbers)


# Practice Problems:

# Create a list with 5 of your favorite foods.

# Print the second and last item.

# Add a new item using .append().

# Remove the first item using .pop(0).

# Reverse your list using .reverse().

# Create a list of 3 lists (matrix), and access the middle element.