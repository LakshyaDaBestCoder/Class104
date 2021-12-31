import csv
from collections import Counter

mtlist=[]
with open('C:/Users/lenovo/Desktop/Python/Class 104/MeanMedianMode-master/c104/height-weight.csv',newline='')as f:
    reader=csv.reader(f)
    mtlist=list(reader)
mtlist.pop(0)
total=0
for e in mtlist:
    total=total+float(e[2])
mean=total/len(mtlist)
print("The mean is",mean)

heightList=[]
for e in mtlist:
    total=total+float(e[1])
    heightList.append(e[1])

heightList.sort()
length=len(heightList)
if length%2==0:
    median1=float(heightList[length//2])
    median2=float(heightList[length//2-1])
    median=(median1+median2)/2
else:
    median=heightList[length//2]
print("The Median is", median)


new_data=[]
for i in range(len(mtlist)):
	n_num = mtlist[i][1]
	new_data.append(n_num)

data = Counter(new_data)
mode_data_for_range = {
                        "50-60": 0,
                        "60-70": 0,
                        "70-80": 0
                    }
for height, occurence in data.items():
    if 50 < float(height) < 60:
        mode_data_for_range["50-60"] += occurence
    elif 60 < float(height) < 70:
        mode_data_for_range["60-70"] += occurence
    elif 70 < float(height) < 80:
        mode_data_for_range["70-80"] += occurence

mode_range, mode_occurence = 0, 0
for range, occurence in mode_data_for_range.items():
    if occurence > mode_occurence:
        mode_range, mode_occurence = [int(range.split("-")[0]), int(range.split("-")[1])], occurence
mode = float((mode_range[0] + mode_range[1]) / 2)
print("The Mode is", mode)