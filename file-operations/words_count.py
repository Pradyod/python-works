fp="D:\\Develpment journey\\python_works\\file-operations\\words_c.txt"

fr=open(fp,"r")

words=[]

for w in fr:
    words.append(w.split())

temp=[i for w in words for i in w]
# print(temp)

result={w:temp.count(w) for w in temp}
print(result)






