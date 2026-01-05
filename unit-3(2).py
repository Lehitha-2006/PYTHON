# Define matrices
M1 = [[1, 2, 3],
      [4, 5, 6]]

M2 = [[7, 8, 9],
      [10, 11, 12]]

# Create an empty result matrix with same size
M3 = [[0 for _ in range(len(M1[0]))] for _ in range(len(M1))]

for i in range(len(M1)):  #loop over runs
    for k in range(len(M2)):  #loop over columns
        M3[i][k] = M1[i][k] + M2[i][k]

# Print result
print("Resultant Matrix (M3):")
for row in M3:
    print(row)
