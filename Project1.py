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

with open('outputText.txt', 'r') as r:
    read = r.read()
    lsInput2 = re.sub('(.+2046)|2047', "", read)
    lsInput2 = re.sub(',0+', "", lsInput2)
    lsInput2 = re.sub('[A-Za-z]', "", lsInput2)
    lsInput2 = re.sub(',,', ",", lsInput2)
    print(lsInput2)

filepath = 'C:\\Users\\mehdi\\PycharmProjects\\Project\\outputText.txt'


def getText(filepath):
    with open(filepath, 'w') as tf:
        for line in lsInput:
            tf.write(line)
            tf.write('\n')

getText(filepath)
