# (p4.py) The dictionary contains the names of subjects and the grades obtained. Define a function f(subjects) that, for 
# the given subjects and their grades, returns the name of the subject for which the average grade is the highest. 
# Example: 
# f({"math":[3,4,4],"geo":[5,4,4,4],"comp":[5,4]})  "comp" 

def f(subjects):
    sub=[

    ]
    for count in subjects.values():
        print(count)
        sub.append(count)
    n=0
    sum1=0
    sum2=0
    sum3=0
    for i in sub[0]:
        sum1+=i
    for i in sub[1]:
        sum2+=i
    for i in sub[2]:
        sum3+=i

    avg1=sum1/len(sub[0])
    avg2=sum2/len(sub[1])
    avg3=sum3/len(sub[2])



print(f({"math":[3,4,4],"geo":[5,4,4,4],"comp":[5,4]}))