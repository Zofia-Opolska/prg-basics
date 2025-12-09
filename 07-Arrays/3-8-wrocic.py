

'''2: **
6: ******
4: ****
9: *********
7: *******
'''
arr=[2,6,4,9,7]

def star(n):
    star_arr=[]
    for i in n:
        star_arr.append(i * "*")
    return star_arr

result = star(arr)                          #nwm jak to inaczej zrobic
for value, stars in zip(arr, result):
    print(f"{value}: {stars}")  



