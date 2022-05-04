import csv
import re
from datetime import datetime

fileDir = "C:\\Users\\alisa\\Desktop\\rawData.txt"
with open(fileDir, "rt") as input:
    lsInput = input.read()
    input.close()

lsInput = re.sub("\n|\d?.=|(?<=Int).", "", lsInput)
lsInput = re.sub("\s+", ",", lsInput)
lsInput = re.sub("(\w+)day|Int", "\n", lsInput)


def convertDate(strDate):
    format = ",%d,%B,%Y,%H:%M"
    date = datetime.strptime(strDate, format)
    return date.timestamp() * 1000

lsInput = lsInput.split()
for i, row in enumerate(lsInput):
    if row[0] == ",":
        date = convertDate(row)
        lsInput.remove(row)
        lsInput[i] = lsInput[i][:5] + "%f,"%date + lsInput[i][6:]
        continue
    lsInput[i]=row[:5]+"%f,"%date+row[6:]

def getArr():
    return lsInput

def getCsv(dir):
    with open(dir,'w') as f:
        write = csv.writer(f)

        # write.writerow(fields)
        write.writerows(lsInput)



getCsv("C:\\Users\\alisa\\Desktop\\out.csv")