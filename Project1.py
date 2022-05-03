import re
from datetime import datetime


def convertDate(strDate):
    format = "%A %d %B %Y %H:%M"
    date = datetime.strptime(strDate, format)
    return date.timestamp() * 1000


with open('2018-December.txt', 'rt') as f:
    Lines = f.read()

    with open('data1.txt', 'w') as w:
        lsInput = re.sub("\n|\d?.=|(?<=Int).", "", Lines)
        lsInput = re.sub("\s+", ",", lsInput)
        lsInput = re.sub("(\w+)day|Int", "\n", lsInput)

        for i in lsInput:
            w.writelines(i)
