
file=open("test.txt","r+")
wordcount={}
for each in file.read().split():
    if each not in wordcount:
        wordcount[each]=1
    else:
            wordcount[each]+=1
print(each,wordcount)