###
# Sums numbers entered by user
#
total_sum = 0
arithmetic_mean = 0
inputs = 0


while True:
    number = int(input("Enter a number (0 to stop): "))
    
    if number == 0:
        break  # Exit the loop when 0 is entered
    total_sum += number
    inputs += 1
arithmetic_mean = total_sum/inputs
print(f"The total sum of the numbers is: {total_sum} mean:{arithmetic_mean}")