###incomplete

def IntegerAList(input):
    for i in range(len(input)):
        input[i] = int(input[i])
    return input

greatest = 0

input = input("give an array in the format [1,2,3]")
input = input.split(",")
print("input =", type(input))
input = IntegerAList(input)
print("input =", type(input[0]))
for i in range(len(input)):
    print("element ", i, " is ", input[i])

greatest = max(input)

print(greatest)

print(input)

###incomplete