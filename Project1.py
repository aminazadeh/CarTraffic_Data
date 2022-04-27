import re
cleaned = set()
newList = []
from collections import deque

with open('2018-December.txt', 'rt') as f:
    Lines = f.read()

    with open('dat.txt', 'w') as w:

        replace1 = re.sub('\n*\w+ \d+.{4}[a-z]* \d{4} \d*:\d*', '', Lines)
        replace2 = re.sub('[1-9]*.=', '', replace1)
        replace3 = re.sub('Int\s*\d+\s*', '', replace2)
        w.writelines(replace3)


index0 = 0
index1 = 1

with open('dat.txt', 'r') as r:
    file = r.readlines()



    while(index0 < len(file) - 1):

        if len(file[index0]) > len(file[index1]):
            newVar = file[index0].replace('\n', ' ') + file[index1].replace('\n', ' ')
            print(newVar)

        else:
            print(file[index0], end='')
            index0 += 2
            newVar = file[index1].replace('\n', ' ') + file[index0].replace('\n', ' ')
            print(newVar)
        index0 += 2
        index1 += 2



def ThreeLiner(Getfile):
    line = set()
    with open(Getfile, 'r') as f:
        file = f.readlines()
        index0 = 0
        index1 = 1

        while(index0 < len(file) - 1):
                if file[index0] > file[index1]:
                    Gather = file[index0].replace('\n', '') + '\t'+ file[index1].replace('\n', '')
                    flag = file[index1]

                    if len(flag) > len(file[index1 + 1]) & len(flag) < len(Gather):
                        Gather = Gather + '\t' +  file[index1 + 1].replace('\n', '')

                        index0 += 1
                        index1 += 1
                index0 += 1
        print(Gather)






# ThreeLiner('new_raw_data.txt')




def TwoLiner():

    index0 = 0
    index1 = 1
    pass







# Code Snippets
#This is for COMMA Seperator
# with open('hello.txt', 'r') as f:
#     fh = f.read()
#     new = re.split(r'\b\s{3,5}', fh)

