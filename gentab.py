import assort

counts = []

## For others
for i in range(3, 16, 3):
	ip_list = assort.get_asc(2 ** i)
	# ip_list = assort.get_desc(2 ** i)
	# ip_list = assort.get_worst_case(2 ** i)

	assort.sort(ip_list)
	print(len(assort.HEADER))
	
## For random
for i in range(3, 4, 3):
	count = 0
	for _ in range(1000):
		ip_list = assort.get_random(2 ** i)
		assort.sort(ip_list)
		count += len(assort.HEADER)
		print(count)
	counts.append(count)
	print (counts)