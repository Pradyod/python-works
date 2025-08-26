text="this is python it is a simple lang"

words=text.split(" ")

wc={}

for i in words:
    if i in wc:
        wc[i]+=1
    else:
        wc[i]=1
    
# print(wc)

# srt_c=sorted(wc,reverse=True,key=wc.get)

# print(srt_c)

max_wc=max(wc.values())

for k,v in wc.items():
    if v==max_wc:
        print(k,v)
