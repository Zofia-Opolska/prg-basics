# (p7.py) A valid username consists of 4 to 12 characters: lowercase letters, numbers and the underscore character.
# Define a function f(array) that, for a given array of usernames, returns the number of valid usernames in the array.
# Example:
# f(["uek","water_7_x","anna.may","a_b_c_d_e_f"])  2 

def f(array):
    valid=0
    for word in array:
        if 4 < word > 12:
            if word 