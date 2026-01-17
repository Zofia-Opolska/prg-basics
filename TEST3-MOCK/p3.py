def f(file):
    if len(file)>1 and len(file)<6:
        if file[0] == "_" or file[0] not in ["0","1","2","3","4","5","6","7","8","9"]:
            for i in range(1,6):
                if file[-i] == "_": #sprawdzam od tylu czy pohawia sie _ ???
                    return False
        else: 
            return False
    else: 
        return False


print(f("_te_t"))
print(f("2te_t"))
print(f("testttt"))
print(f("te_t"))


#do dokonczenia