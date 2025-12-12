# (p4.py) The dictionary contains the names of subjects and the grades obtained. Define a function f(subjects) that, for
# the given subjects and their grades, returns the name of the subject for which the average grade is the highest.
# Example:
# f({"math":[3,4,4],"geo":[5,4,4,4],"comp":[5,4]}) -> "comp"

def f(subject):
    highest_avr=0
    sub_with_highest_avr=None
    for subject,grades in subject.items():
        avr = sum(grades)/len(grades)
        if avr>highest_avr:
            highest_avr=avr
            sub_with_highest_avr=subject
    return sub_with_highest_avr 

print(f({"math":[3,4,4],"geo":[5,4,4,4],"comp":[5,4]}))