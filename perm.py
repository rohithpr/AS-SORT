from itertools import permutations
from heapq import heapify
import assort

def main(n):
	ip_lists = list(permutations([i for i in range(n)]))
	counter = {i: 0 for i in range(int((n/2)+3))}
	for l in ip_lists:
		ip_list = list(l)
		assort.sort(ip_list)
		count = len(assort.HEADER)
		counter[count] += 1
	print(n, counter)

if __name__ == '__main__':
	for i in range(9):
		main(i)
