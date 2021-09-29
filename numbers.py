import sys

n1 = float(sys.argv[1])
n2 = float(sys.argv[2])

result_sum = n1 + n2
result_difference = n1 - n2
result_product = n1 * n2
result_quotient = n1 / n2

print(f'{n1} plus {n2} equals {result_sum}')
print(f'{n1} minus {n2} equals {result_difference}')
print(f'{n1} mult {n2} equals {result_product}')
print(f'{n1} quot {n2} equals {result_quotient}')