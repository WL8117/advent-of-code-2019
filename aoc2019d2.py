Input = open("input2019d2.txt", "r")
Input2 = Input.readline()
'''Input2 = Input2.split(",")
Input3 = []
for x in Input2:
    Input3.append(int(x))
print(Input3)
print(len(Input3))
position = 0
insertingNumber = 0
continues = True
positionChanging = 0
addingNumber1 = 0
addingNumber2 = 0
while continues == True and position <= 121:
    if Input3[position] == 1:
        addingNumber1 = Input3[position + 1]
        addingNumber2 = Input3[position + 2]
        insertingNumber = Input3[addingNumber1] + Input3[addingNumber2]
        positionChanging = Input3[position + 3]
        Input3[positionChanging] = insertingNumber
        position += 4
    elif Input3[position] == 2:
        addingNumber1 = Input3[position + 1]
        addingNumber2 = Input3[position + 2]
        insertingNumber = Input3[addingNumber1] * Input3[addingNumber2]
        positionChanging = Input3[position + 3]
        Input3[positionChanging] = insertingNumber
        position += 4
    elif Input3[position] == 99:
        position += 999101101
        conntinues = False
print(Input3)'''
 
 
 
Input = open("input2019d2.txt", "r")
Input2 = Input.readline()
Input.close()
Input2 = Input2.split(",")
Input3 = []
Input4 = []
for x in Input2:
   Input3.append(int(x))
for x in Input2:
    Input4.append(int(x))
print(Input3)
print(len(Input3))
print(Input4)
position = 0
insertingNumber = 0
continues = True
positionChanging = 0
for i in range(99):
   for j in range(99):
       position = 0
       Input3 = list(Input4)
       Input3[1] = i
       Input3[2] = j
       while position <= 121:
           if Input3[position] == 1:
               addingNumber1 = Input3[position + 1]
               addingNumber2 = Input3[position + 2]
               insertingNumber = Input3[addingNumber1] + Input3[addingNumber2]
               positionChanging = Input3[position + 3]
               Input3[positionChanging] = insertingNumber
               position += 4
           elif Input3[position] == 2:
               addingNumber1 = Input3[position + 1]
               addingNumber2 = Input3[position + 2]
               insertingNumber = Input3[addingNumber1] * Input3[addingNumber2]
               positionChanging = Input3[position + 3]
               Input3[positionChanging] = insertingNumber
               position += 4
           elif Input3[position] == 99:
               position += 999101101
               if Input3[0] == 19690720:
                   print(Input3)
                   print(100 * i + j)