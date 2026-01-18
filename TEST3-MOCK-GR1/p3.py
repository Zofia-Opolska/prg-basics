def f(vname):
    if len(vname)>1 and len(vname)<5:
        for i in vname:
            if i[0] in vname not in [1,2,3,4,5,6,7,8,9,0]:
                return True
            else: 
                return False
    else:
        return False
    

print(f("8aBC"))