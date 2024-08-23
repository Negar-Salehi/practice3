print (" We will sort your array ")
print (" Please enter an array of numbers ")
print (" when your array is finish enter 'end' ")

array = []

while True : 
    user_array = input (" Please enter the input : ")

    if user_array == "end" :
        break

    else :
        n = int ( user_array )
        array.append ( n )

array.sort ()
print ( array )