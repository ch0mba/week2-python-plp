#Create an empty list called my_list

my_list = []

#Append the folloing elements to my_list: 10, 20, 30, 40.
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)

#Insert 15 at the second position in the list.
my_list.insert(1, 15)

#Extend the list by adding the following elements: 50, 60, 70.
my_list.extend([50, 60, 70])

#Remove the element at the third position in the list.
my_list.pop(2)

#Sort the list in ascending order.
my_list.sort()

#Find and print the index of the value 30 in the list.
index = my_list.index(30)

#Print the list.
print(my_list)