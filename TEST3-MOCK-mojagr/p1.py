def help(word,index):
    ref=list(word)
    ref[index] = ref[index].upper()
    wynik = "".join(ref)
    return wynik


def f(word):
    result = ""
    count = len(word)
    for i in range(count):
        result = result +help(word,i) + "-"  
    return result[0:len(result)-1]


#print(f("water"))