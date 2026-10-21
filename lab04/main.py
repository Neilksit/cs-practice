from stats import average_by_city, read_valid, warmest_city, warmest_city1
import sys


cnt_t, cnt_f = 0, 0
print('Ввод:')
lines = sys.stdin.read().splitlines()
print('Вывод:')
print(warmest_city1(read_valid(lines)))