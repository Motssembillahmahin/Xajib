import numpy as np
MR1 = np.array([ # Define the matrices for MR1 and MR2
 [1, 1, 1],
 [1, 0, 1],
 [0, 1, 0]
])
MR2 = np.array([
 [1, 0, 1],
 [0, 1, 1],
 [1, 1, 0]
])
 # Calculate the union (MR1 ∪ MR2) by element-wise logical OR
union_result = np.logical_or(MR1, MR2).astype(int)
 # Calculate the symmetric difference (MR1 ⊕ MR2) by element-wise XOR
symmetric_diff_result = np.logical_xor(MR1, MR2).astype(int)
print("MR1 ∪ MR2 (Union):") # Print the results
print(union_result)
print("\nMR1 ⊕ MR2 (Symmetric Difference):")
print(symmetric_diff_result)
