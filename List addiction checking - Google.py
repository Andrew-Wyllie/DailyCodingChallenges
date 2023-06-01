k = int(input("Input k value \n "))
store = [3,5,8,12]
result = False
for i in range(len(store)-1):
    for j in range(len(store)-1):
        if store[i] + store[j] == k:
            result = True
print(result)