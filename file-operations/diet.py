fp="D:\\Develpment journey\\python_works\\file-operations\\food_logs.csv"

fr=open(fp,'r')

food_logs=[]

for line in fr:
    data=line.rstrip('\n').split(",")

    if len(data)>1:
        dictionary={
                    'date':data[0],
                    "meal_type":data[1],
                    'name':data[2],
                    'serving_size':data[3],
                    'calories':data[4]
                    }

        food_logs.append(dictionary)

# print(food_logs)


#get the sum of calorie consumed each day

daily_summary={}

for f in food_logs:
    date=f.get("date")
    calorie=int(f.get("calories"))

    if date in daily_summary:
        daily_summary[date]+=calorie
    else:
        daily_summary[date]=calorie

print(daily_summary)

#get the max calorie

max_calorie=[daily_summary,key=lambda c;c.get("calorie")]