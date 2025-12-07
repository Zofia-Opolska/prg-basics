# (p5.py) Define a function f(first_letter,last_letter) that, for the data.txt file, returns the number of words that start 
# with the first_letter and end with the last_letter. Example: 
# f("w","d")  compare your result with other students 

def f(first_letter,last_letter):
    file_name='data.txt'
    count=0

    with open(file_name) as file:
        x=(file_name.read).split()
        clean_word = x.strip(".,!?;:[]()\"'’“”")
        for i in x:
            if clean_word[0]==first_letter and clean_word[-1]==last_letter:
                count+=1
    return count
    
print(f('w','d'))

