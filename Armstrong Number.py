i = int(input("Enter Number : "))
M = i
sum = 0
while (i>0):
    sum = sum + (i%10)*(i%10)*(i%10)
    i = i//10

if M == sum:
    print("Number is Armstrong")

else:
    print("Number is not Armstrong")
