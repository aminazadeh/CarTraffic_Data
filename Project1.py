import io
import re
import locale
import csv


# Initial data cleansing with regex 



with open('2018-December.txt', 'rt') as f:
    Lines = f.read()

    with open('data1.txt', 'w') as w:

        replace1 = re.sub('\n*\w+ \d+.{4}[a-z]* \d{4} \d*:\d*', '', Lines)
        replace2 = re.sub('[1-9]*.=', '', replace1)
        replace3 = re.sub('Int ', '#', replace2)
        rep = re.sub('( {3}| {4}| {5}| )', ' ', replace3)
        w.writelines(rep)


index0 = 0
index1 = 1
index2 = 2


with open('data1.txt', 'r') as r:
    file = r.readlines()


# Converting 3-2 lines into a single line
    if file[index0] == '\n':
        del file[index0]

    with open('cleaned.txt', 'w') as y:

        while (index2 < len(file) - 1):
            if len(file[index0]) > len(file[index1]):

                newvar = file[index0].replace('\n', '') + '  ' + file[index1].replace('\n', '')
                flag = file[index1]

                if len(flag) > len(file[index2]):
                    newvar_ = flag.replace('\n', '') + '  ' + file[index2].replace('\n', '')

                    newvar = file[index0].replace('\n', '') + '  ' + newvar_


                s = io.StringIO(newvar)
                TheCase = s.readlines()


                for h in TheCase:
                    if  h.startswith('#'):
                        newCase = h

                #Replacing Int with # and removing extra spaces
                newCase2 = re.sub('.#\d{2,4}.*','', newCase)
                newCase3= re.sub(' {3}','  ', newCase2)


                # Comma separating
                newCase4 = re.sub(' {1,}', ',', newCase3)
                for i in newCase4.splitlines():
                    y.write(i+'\n')


            index0 += 1
            index1 += 1
            index2 += 1


# an Excel compatible csv delimiter.
locale.setlocale(locale.LC_ALL, '')
DELIMITER = ',' if locale.localeconv()['decimal_point'] == ';' else ';'

with open('cleaned.txt', 'r') as r:
    file = r.read()

    split = file.splitlines()

    with open('file.csv', 'w', newline='') as csv_writer:
        csv_writer = csv.writer(csv_writer, delimiter = DELIMITER)

        for item in split:
            csv_writer.writerow([item])