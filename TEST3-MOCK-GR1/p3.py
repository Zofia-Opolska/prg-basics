def f(vname):
    if len(vname)>=1 and len(vname)<=5:
        for i in vname:
            if i[0] not in ['1','2','3','4','5','6','7','8','9','0']:
                return True
            else: 
                return False
    else:
        return False
    

print(f("aBC"))
print(f("_8a_C"))
print(f("abcdef"))
print(f("8abC"))
print(f("_ab8_"))