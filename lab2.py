# Define sets A and B
A = {1, 2, 3}
B = {1, 2}
relation_R = [] # Initialize an empty list to store the relation R
for a in A: # Find the relation R
   for b in B:
       if a > b:
           relation_R.append((a, b))
print("Relation R:") # Print the relation R as a set of ordered pairs
for pair in relation_R:
 print(pair)
 # Create a matrix representation of the relation R
matrix_R = [[1 if (a, b) in relation_R else 0 for b in B] for a in A]
print("\nMatrix Representation of R:") # Print the matrix representation of the relation R
for row in matrix_R:
 print(row)