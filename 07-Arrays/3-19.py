#Write a program that, for the given array of real numbers, prints the number of elements that are greater than the given value entered from the keyboard.
arr=[15,38,7,23,14]
x=int(input('Enter your number: '))
count=0
for i in arr:
    if i > x:
        count+=1
print(count)