import sys

order_of_succesion = sys.argv
order_of_succesion.pop(0)

for n, l in enumerate(order_of_succesion):
    print(f'{n+1}. {l}')
    