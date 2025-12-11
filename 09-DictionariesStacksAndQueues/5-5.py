paragraph = "cat dog mouse cat rat cat mouse"
par=paragraph.split()
dic={}
for i in par:
    dic[i]=0
for i in par:
    if i in dic:
        dic[i]+=1

for key,value in dic.items():
    print(f'Word {key} appeared {value} time(s)')