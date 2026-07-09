#Q1
count = 1
while(count<=5) :
    print(count)
    count +=1
#Q2
#printing even numbers with for loop
for i in range(2,21,2) :
    print(i)
#printing even numbers with while loop
num = 2
while(num <= 20) :
    print(num)
    num +=2
#Q4
for i in range(11) :
    if i == 5:
        continue
    print(i)
#Q5 I didn't understood stopping a loop when it reaches 7 which means if i write a python loop range(8) it automatically stops at 7 
for i in range(10):
    print(i)
    if i == 7 :
        print("finished! because it reached 7")
        break
    
