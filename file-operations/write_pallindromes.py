pallidromes=["hello","racecar","malayalam","world","madam"]

fp="D:\\Develpment journey\\python_works\\file-operations\\words.txt"

fw=open(fp,"w")
for w in pallidromes:
    if w==w[::-1]:
        fw.write(w+"\n")

