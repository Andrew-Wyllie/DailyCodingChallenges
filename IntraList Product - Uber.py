import numpy as np
input = input("Give the input list")
input = input.split(",")
print(input)
output = []

for i in range(len(input)):
    input[i] = int(input[i])

for i in range(len(input)):
    output.append(np.prod(input)/input[i])

print(output)
print("Daily Coding Complete - 02/06/23")
