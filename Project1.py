import re
from datetime import datetime
import csv


def convertDate(strDate):
    format = ",%d,%B,%Y,%H:%M"
    date = datetime.strptime(strDate, format)
    return date.timestamp() * 1000


fileDir = 'C:\\Users\\mehdi\\PycharmProjects\\Project\\2018-December.txt'

with open(fileDir, 'rt') as f:
    Lines = f.read()

    # with open('data1.txt', 'w') as w:

    lsInput = re.sub("\n|\d?.=|(?<=Int).", "", Lines)
    lsInput = re.sub("\s+", ",", lsInput)
    lsInput = re.sub("(\w+)day|Int", "\n", lsInput)

    # print(lsInput)
    lsInput = lsInput.split()
    for i, row in enumerate(lsInput):
        if row[0] == ',':
            date = convertDate(row)
            lsInput.remove(row)
            lsInput[i] = lsInput[i][:5] + "%.2f," % date + lsInput[i][6:]
            continue
        lsInput[i] = row[:5] + "%.2f," % date + row[6:]

    lsInput = [j.replace(',,', ',') for j in lsInput if ',,' in j]

    new_d = [k.split(',') for k in lsInput]


    def getCsv(dir):

        with open(dir, 'w') as f:
            write = csv.writer(f)

            write.writerows(new_d)

getCsv('C:\\Users\\mehdi\\PycharmProjects\\Project\\out.csv')
