# (p5.py) Define a function f(first_letter,last_letter) that, for the data.txt file, returns the number of words that start
# with the first_letter and end with the last_letter. Example:
# f("w","d")  compare your result with other students 

def f(first_letter,last_letter):
    import re
    with open('data.txt','r') as file:
        text=file.read()
        pattern = rf"\b{first_letter}[a-zA-Z]*{last_letter}\b"
        mathes=re.findall(pattern,text)
    return len(mathes)
print(f("w","d"))


def f(first_letter: str, last_letter: str) -> int:
    words = 0
    
    with open("data.txt", "r") as file:
        for line in file:
            line = line.split()
            
            for i in line:
                if ((i[0] == first_letter) and (i[-1] == last_letter)):
                    words += 1
                    
    return words