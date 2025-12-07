# (p4.py) The dictionary contains the names of subjects and the grades obtained. Define a function f(subjects) that, for 
# the given subjects and their grades, returns the name of the subject for which the average grade is the highest. 
# Example: 
# f({"math":[3,4,4],"geo":[5,4,4,4],"comp":[5,4]})  "comp" 


def f(subjects):
    best_subject = None
    best_average = float("-inf")
    
    for subject, grades in subjects.items():
        if grades:  # avoid division by zero
            avg = sum(grades) / len(grades)
            if avg > best_average:
                best_average = avg
                best_subject = subject
    
    return best_subject

print(f({"math":[3,4,4],"geo":[5,4,4,4],"comp":[5,4]}))