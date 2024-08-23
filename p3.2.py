n = int(input("please enter the length of the array:"))

Array= []

for i in range(n):
    x = int(input("please enter your number:"))
    if x not in Array:
        Array.append(x)

        if len(Array) > 1: 
            if Array[i] > Array[i-1]:
                print("Right")
            else:  
                print("Your array is not from smallest to largest")
                print("Try again!")
                break
    print(Array)