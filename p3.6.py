num1 = int(input( "Please Enter the First Number : "))
num2 = int(input( "Please Enter the Second Number: "))
Bmm = 0

if num1 > num2:
    x = num2

elif num1 < num2:
    x = num1

for i in range(1 , x+1):
    if num1 % i == 0 and num2 % i == 0:
        Bmm = i


kmm = int((num1 * num2)/Bmm)
print("Kmm = " , kmm)