def f(mnumbers):
    import re
    if len(mnumbers)>1 and len(mnumbers)<7:
        pattern = re.compile(r'^[+-]?[1-7a-dA-D]+$')
        return sum(1 for x in mnumbers if pattern.match(x))
    
    
# print(f(["A15","-31","7abC","+D1","-g4"]))
# print(f(["A05","-3+1","7ab8C","+Bb7","-22c55"]) )