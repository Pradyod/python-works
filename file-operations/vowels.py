fp="D:\\Develpment journey\\python_works\\file-operations\\words_vw.txt"

fr=open(fp,'r')

wrds=[]

for w in fr:
    wrds.append(w.rstrip("\n"))

print(wrds)

# for w in wrds:
#     if w[0] in ('a','e','i','o','u'):
#         print(w)

result=[w for w in wrds if w[0] in ('a','e','i','o','u')]
print(result)
    