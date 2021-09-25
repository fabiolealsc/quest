import sys

n1 = int(sys.argv[1])
n2 = int(sys.argv[2])

if n1 + n2 <= 0:
    print('You have chosen the path of destitution.')
elif 1 <= (n1 + n2) <= 100:
    print('You have chosen the path of plenty.')

else:
    print('You have chosen the path of excess.')
