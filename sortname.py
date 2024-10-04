#Problem -> Sorting the names
#Order out alphabetically
#Store the sorted naes in a new text file called: sortname.txt

#1.Read the names from names.txt and store them in a variable
names = [] #declare an empty list that can store name string values

with open("./names.txt","r") as data_file:
    #print(data_file.readline())#we print the .readline() to see what it generates
    for line in data_file.readlines():
        value = line.replace("\n","")
        names.append(value) #For all list we can use .append to add the given argument to the back of the list
#end of getting names

#Sort the names in alphabetical order, we will use the selection sort algorithm
"""
Selection Sort Algorithm:
    1. Start with the first element as the initial position.
    2. Find the smallest element in the unsorted portion of the array.
    3. Swap this smallest element with the first unwanted element.
    4. Move the boundary of the sorted portion one element forward.
    5. Repeat steps 2-4 for the remaining unsorted element until entire array is sorted.

[3,1,4], [3] is considered sorted, then we see if [1,4] has a smaller value
if [1,4] has a smaller value swap 2 locaions
"""

i = 0
while i<len(names):
    j=i+1

    smallest_name=names[i]
    smallest_index = j
    while j<len(names):
        if names[j] < smallest_name:
            smallest_name = names[j]
            smallest_index = j
        j+=1

    if smallest_name<names[i]:
        names[i], names[smallest_index] = names[smallest_index],names[i]
    i+=1

print(f"Sorted name:\n{names}")

#3. Write the names into a new file called "sortednames.txt"
with open("sortedNames.txt","w") as data_file:
    for line in names:
        data = f"{line}\n"
        data_file.write(data)
    print("sortedNames.txt completed")