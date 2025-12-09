# 1. ["water","book","sky"]   ["water","book","sky"]
# 1. [True,False]   [True,False,True]
# 1. [5,3,1][5,3,1]
# 1. [3,2,1][3,2]

def f(arr1,arr2):
    b=[]
    a=len(b)
    if len(arr1)==len(arr2):
        while a<len(arr1):
           if arr1[a]==arr2[a]:
               a+=1
        return True
    return False 

print(f(["water","book","sky"] ,["water","book","sky"]))
print(f([True,False],[True,False,True]))
print(f([5,3,1],[5,3,1]))
print(f([3,2,1],[3,2]))

#################

def f(a1, a2):
    return a1 == a2


print(f(["water","book","sky"] ,["water","book","sky"]))
print(f([True,False],[True,False,True]))
print(f([5,3,1],[5,3,1]))
print(f([3,2,1],[3,2]))


