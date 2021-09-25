import sys

inputs = sys.argv[1]

for i in inputs:
    i = int(i.removeprefix('-'))
    if float(i) / 3 == 0:
        print('fizz')
    elif float(i) / 5 == 0:
        print('buzz')
    elif float(i) / 3 == 0 and i / 5 == 0:
        print('fizzbuzz')
    else:
        print(i)