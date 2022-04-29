import re


with open('2018-December.txt', 'rt') as f:
    Lines = f.read()

    with open('dat.txt', 'w') as w:

        replace1 = re.sub('\n*\w+ \d+.{4}[a-z]* \d{4} \d*:\d*', '', Lines)
        replace2 = re.sub('[1-9]*.=', '', replace1)
        replace3 = re.sub('Int ', '#', replace2)
        rep = re.sub('( {3}| {4}| {5}| )', ' ', replace3)
        w.writelines(rep)

#^Int.
#Int\s*\d+\s*


index0 = 0
index1 = 1
index2 = 2

with open('newdata.txt', 'r') as r:
    file = r.readlines()


    if file[index0] == '\n':
        del file[index0]

    while (index2 < len(file) - 1):
        if len(file[index0]) > len(file[index1]):

            newvar = file[index0].replace('\n', '') + '  ' + file[index1].replace('\n', '')
            flag = file[index1]

            if len(flag) > len(file[index2]):
                newvar_ = flag.replace('\n', '') + '  ' + file[index2].replace('\n', '')

                newvar = file[index0].replace('\n', '') + '  ' + newvar_


            print(newvar)
        index0 += 1
        index1 += 1
        index2 += 1
        


    #Test
    # while(index2 < len(file) - 1):
    #     if len(file[index0]) > len(file[index1]):
    #         flag = file[index1]
    #
    #         if len(flag) > len(file[index2]):
    #             newvar_ = flag.replace('\n', '') + '  ' + file[index2].replace('\n', '')
    #
    #             newvar = file[index0].replace('\n', '') + '  ' + newvar_
    #             print(newvar)
    #     index0 += 1
    #     index1 += 1
    #     index2 += 1






