# Python code to split a list
# into sublists of given length.

from itertools import islice

# Input list initialization
Input = [2,1,-1,1,5,2,2,-4,3,1,1,5]

# list of length in which we have to split
length_to_split = [4,4,4]

# Using islice
Inputt = iter(Input)
Output = [list(islice(Inputt, elem))
		for elem in length_to_split]

# Printing Output
print("Initial list is:", Input)
print("Split length list: ", length_to_split)
print("List after splitting", Output)
