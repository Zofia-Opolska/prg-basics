arr1=[7,3,4]
arr2=[1,4,2,3,5,4]


def f(arr1, arr2):
    for i in arr1:
        if i not in arr2:
            return False
    return True
print(f([7,3,4],[1,4,2,3,5,4]))