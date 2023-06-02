import pysimplegui as sg

sg.Window(title="DailyCoding", layout=[[]], margins=(100, 50)).read()


k = int(input("Input k value \n ")) 
store = [3,5,8,12]
result = False
for i in range(len(store)-1):               #add first element to all items
    for j in range(len(store)-1):           #iter through list comparing each element
        if store[i] + store[j] == k:
            result = True                   #only change to true if found
print(result)

print("Daily Coding Complete - 01/06/23")