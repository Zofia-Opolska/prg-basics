# (p7.py) A valid username consists of 4 to 12 characters: lowercase letters, numbers and the underscore character. 
# Define a function f(array) that, for a given array of usernames, returns the number of valid usernames in the array. 
# Example: 
# f(["uek","water_7_x","anna.may","a_b_c_d_e_f"])  2 

def f(array):
    count = 0
    
    for username in array:
        if 4 <= len(username) <= 12:
            valid = True
            for ch in username:
                if not (ch.islower() or ch.isdigit() or ch == "_"):
                    valid = False
                    break
            if valid:
                count += 1
    return count
print(f(["uek","water_7_x","anna.may","a_b_c_d_e_f"]))


