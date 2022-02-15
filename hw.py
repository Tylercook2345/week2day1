cubes = [number**3 for number in range(1,11)]

for cube in cubes: 
    print(cube)
    if cubes > 1000:
        break
        
for num in range(0,101):
   if num > 1:
       for i in range(2,num):
           if (num % i) == 0:
               break
       else:
           print(num)
            
            

age = int(input("What is your age?: "))
if age < 18:
    print ("kids") 
elif age >= 18 and age < 65:
    print("adults")
else: 
    print("seniors")