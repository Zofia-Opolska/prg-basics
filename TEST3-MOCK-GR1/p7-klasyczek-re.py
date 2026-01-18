def f(files):
    import re
    return sorted(files, key=lambda x: re.search(r".([^.]+)$", x).group(1))



files = ['a.txt','bb.pdf','ccc.py','dddd.mpeg4']
print(f(files))