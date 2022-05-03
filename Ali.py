import re
from datetime import datetime

fileDir = "C:\\Users\\alisa\\Desktop\\rawData.txt"
with open(fileDir, "rt") as input:
    lsInput = input.read()

lsInput = re.sub("\n|\d?.=|(?<=Int).", "", lsInput)
lsInput = re.sub("\s+", ",", lsInput)
lsInput = re.sub("(\w+)day|Int", "\n", lsInput)


def convertDate(strDate):
    format = "%A,%d,%B,%Y,%H:%M"
    date = datetime.strptime(strDate, format)
    return date.timestamp() * 1000


# for row in lsInput:
#     print(row)

print(lsInput)
# print(convertDate("Saturday,01,December,2018,00:15"))
