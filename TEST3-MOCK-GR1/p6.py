def f(fnc,res):
    lista=list(filter(fnc,res))
    result=max(lista)-min(lista)
    return result



res=[95,90,20,50,70]
fnc=lambda x: x>50
print(f(fnc,res))
