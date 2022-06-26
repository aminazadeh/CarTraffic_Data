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


<<<<<<< HEAD
=======
# Removing NA and Zero
for itemNA in new_d:
    for j in itemNA:
        if j == 'NA':
            itemNA.remove(j)

for item0 in new_d:
    for i in item0:
        if i == '0':
            item0.remove(i)

# Showing the result
# for _ in new_d:
#     print(_)

new_d.insert(0, ['Intersection', 'Time', '1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16'])


filepath = 'C:\\Users\\mehdi\\PycharmProjects\\Project\\output.csv'


def getCsv(filepath):
    with open(filepath, 'w', newline='') as cf:
        write = csv.writer(cf)

        write.writerows(new_d)

# Vase estefade badi

>>>>>>> 4b1f557ed81927e1f60170b82e81991545dc3ffe
def getText(filepath):
    with open(filepath, 'w') as tf:
        for line in lsInput:
            tf.write(line)
            tf.write('\n')

getText(filepath)
