def f(fnc,prods):
    str='' 
    



prods = ["water","cheese","tomato"]
fnc1 = lambda x: "id:"+x[:2]
print(f(fnc1,prods)) #returns "id:wa,id:ch,id:to"
fnc2 = lambda x: (x[0]+x[-1]).upper()
print(f(fnc2,prods)) #returns "WR,CE,TO" 