# Text: I completely agree with you
# No. of letters in words: [1,10,5,4,3]
sentence = 'I completely agree with you'
split_sentence=sentence.split()
result = list(map(lambda x:len(x), split_sentence))
print(result)