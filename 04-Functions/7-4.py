def f(phrase,letter):
    count=0
    letter in ['a','ą','b','c','ć','d','e','ę','f','g','h','i','j','k','l','ł','m','n','o','ó','p','r','s','ś','t','u','w','y','z','ź','ż']
    for char in phrase:
        if char == letter:
            count+=1
    return count
    
print(f('You never get a second chance to make a first impression','e'))