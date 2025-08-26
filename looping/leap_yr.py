start=1879
stop=2026

while start<=stop:
    if start%4==0 and start%100!=0 or start%400==0:
        print(start)
    start+=1