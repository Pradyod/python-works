fp1="D:\\Develpment journey\\python_works\\file-operations\\all_students.txt"
fp2="D:\\Develpment journey\\python_works\\file-operations\\fail_stds.txt"

fr1=open(fp1,"r")

fr2=open(fp2,"r")

fw=open("D:\\Develpment journey\\python_works\\file-operations\\pass_stds.txt","w")


all_std=set()

fail_stds=set()

for name in fr1:
    all_std.add(name.rstrip("\n"))

print(all_std)

for name in fr2:
    fail_stds.add(name.rstrip("\n"))

print(fail_stds)

pass_stds=set(all_std.difference(fail_stds))

print(pass_stds)

for name in pass_stds:
    fw.write(name+"\n")