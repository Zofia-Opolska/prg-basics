# (p7.py) A valid username consists of 4 to 12 characters: lowercase letters, numbers and the underscore character. 
# Define a function f(array) that, for a given array of usernames, returns the number of valid usernames in the array. 
# Example: 
# f(["uek","water_7_x","anna.may","a_b_c_d_e_f"])  2 

def f(array):
    n=0
    count=0
    while n<len(array):
        for array[0] in array:
            if len(array[0])>=4 and len(array[n])<=12:
                for i in array[0]:
                    if i in list(map(chr, range(97, 123))) and ['_']:
                        count+=1
                        n+=1
    return count

print(f(["uek","water_7_x","anna.may","a_b_c_d_e_f"]))


