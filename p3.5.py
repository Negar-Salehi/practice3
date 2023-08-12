num1 = int(input( "Please Enter the First Number : "))
num2 = int(input( "Please Enter the Second Number: "))

maghsoom_num1=[]
maghsoom_num2= []
for i in range (1 , num1+1):
  
   y = num1 % i
   if y == 0:
      maghsoom_num1.append(i)
      i+=1
   else:
      i+=1
print("Maghsoom alaih num1 = " , maghsoom_num1)      

for i in range (1 , num2+1):
  
   y = num2 % i
   if y == 0:
      maghsoom_num2.append(i)
      i+=1
   else:
      i+=1
print("Maghsoom alaih num2 = " , maghsoom_num2)

x=len(maghsoom_num1) 
y=len(maghsoom_num2)
i=1
j=1
same = []

for i in range(x):
      for j in range (y):
          
          if maghsoom_num1[i] == maghsoom_num2[j] :
                 same.append(maghsoom_num1[i]) 
                 j+=1
                 
          else:
             j+=1 
      i+=1                
print("maghsoom alaihe moshtarak = ", same) 
print("b.m.m = " , max(same))