import re
import datetime

def convertDate(strDate):
    format = "%A %d %B %Y %H:%M"
    date = datetime.strptime(strDate, format)
    return date.timestamp()*1000


with open('2018-December.txt', 'rt') as f:
    Lines = f.read()

    with open('data1.txt', 'w') as w:
        
        replace1 = re.sub('[1-9]*.=', '', Lines)
        replace2 = re.sub('Int ', '#', replace1)
        replace3 = re.sub('(\s{3,4})', ' ', replace2)
        w.writelines(replace3)


with open('data1.txt', 'r') as f:
    with open('data2.txt', 'w') as w:
        file = [file.replace('\n', '') for file in f.readlines()]

        file2 = [i.replace('#', '\n') for i in file]

        for i in file2:
            w.writelines(i)

        # d = []
        # for i in file2:
        #     if re.findall('^[A-Z]+.+',i,re.M):
        #         d.append(i)
