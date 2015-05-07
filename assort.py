'''
Merge a given set of input integers by using AS Sort.
'''

# START refers to the first element OR position of a list
# END refers to the last element OR position of a list
# ELEMENT refers to the element that is being inserted
# HEADER is the header which holds all the lists

import heapq
import random

def build_seq(ele):
	''' (int) -> None
	Sequential search for the correct position at which ELEMENT can be inserted.
	Efficiency class: O(n) where n is the number of lists.
	n <<< number of elements.
	'''
	global HEADER
	if HEADER == []:						# No lists are available.
		HEADER.append([ele])				# Create a new list and add it to the header.
		return

	for l in HEADER:						# l is the current list.
		if ele <= l[0]:						# ELEMENT smaller than START of current list.
			l.insert(0, ele)				# Insert ELEMENT to START of current list.
			return
		elif ele >= l[-1]:					# ELEMENT greater than END of current list.
			l.append(ele)					# Insert ELEMENT to END of current list.
			return

	HEADER.append([ele])					# Doesn't fit in any of the existing lists. So new list.

def build_bin(ele):
	''' (int) -> None
	Binary search for the correct position at which ELEMENT can be inserted.
	Efficiency class: O(ln(n)) where n is the number of lists.
	n <<< number of elements.
	'''
	global HEADER
	if HEADER == []:						# No lists are available.
		HEADER.append([ele])				# Create a new list and add it to the header.
		return

	low = 0
	high = len(HEADER)-1
	while low<=high:
		mid = (low + high) // 2				# Get index to current list.

		if mid == 0:						# Current list is the first list.
			if ele <= HEADER[0][0]:
				HEADER[0].insert(0, ele)	# Insert to START of first list.
				break
			elif ele >= HEADER[0][-1]:
				HEADER[0].append(ele)		# Insert to END of first list.
				break
			else:
				low = mid + 1				# Search for correct position towards the right.

		elif ele <= HEADER[mid][0]:			# ELEMENT is lesser than START of current list.
			if HEADER[mid-1][0] < ele:		# ELEMENT is greater than START of previous list.
				HEADER[mid].insert(0, ele)	# Insert to START of current list.
				break
			else:							# ELEMENT is lesser than START of previous list.
				high = mid - 1				# Search for correct position towards the left.

		elif ele >= HEADER[mid][-1]:		# ELEMENT is greater than END of current list.
			if HEADER[mid-1][-1] > ele:		# ELEMENT is lesser than END of previous list.
				HEADER[mid].append(ele)		# Insert at END of current list.
				break
			else:							# ELEMENT is greater than END of previous list.
				high = mid - 1				# Search for correct position towards the left.

		else:								# START < ELEMENT < END for current list.
			low = mid + 1					# Search for correct position towards the right.

	else:									# Doesn't fit in any of the existing lists.
		HEADER.append([ele])				# Create a new list with ELEMENT and add it to the END of HEADER.

def sort(ip_list):
	''' (list) -> None
	Sorts a list in O(n ln(n)) time and takes O(n) space.
	'''
	global HEADER
	HEADER = []

	heapq.heapify(ip_list)					# In-built heapify function. O(n)
											# Calling this function is optional.
											# It helps reduce the number number of lists.

	for ele in ip_list[::-1]:
		build_bin(ele)						# Call the O(ln(n)) function n times.
	ip_list[:] = heapq.merge(*HEADER)		# In-built merge function. O(n ln(k)) 
											# where k is the average number of elements per list
											# and n is the total number of elements.

#########################################################################################
### The functions below this line aren't called for anything other than generation of ###
### lists that are to be sorted and some other stat. collection. They may be ignored. ###
#########################################################################################

def get_worst_case(n):
	''' (int) -> list
	Returns a list which is the worst case for this sorting algorithm.
	(Worst case if you don't use heapify)
	'''
	l = []
	j = 0
	for i in range(n):
		if i%2==0:
			l.append(j)
		else:
			l.append(n-j-1)
			j += 1
	return l

def get_asc(n):
	''' (int) -> list
	Returns a list whose elements are in ascending order.
	'''
	l = [i for i in range(n)]
	return l

def get_desc(n):
	''' (int) -> list
	Returns a list whose elements are in descending order.
	'''
	l = [i for i in range(n-1, -1, -1)]
	return l

def get_random(n):
	''' (int) -> list
	Returns a list whose elements are in a random order.
	'''
	l = [random.randrange(100000) for i in range(n)]
	return l

def is_sorted(l):
	''' (list) -> bool
	Checks if the elements of a given are in sorted order.
	'''
	for i in range(len(l)-1):
		if l[i] > l[i+1]:					# Some element is not in correct position.
			print("Not sorted: ", l)
			return False
	return True

def verify():
	'''	(None) -> bool
	Checks if the header is valid.
	'''
	global HEADER
	for l in HEADER:						# Check if each list is sorted.
		if not is_sorted(l):
			return False
	l = [i[0] for i in HEADER]
	if not is_sorted(l):					# Check if STARTs of all lists are in ascending order.
		return False
	l = [i[-1] for i in HEADER][::-1]
	if not is_sorted(l):					# Check if last ENDs of all lists are in descending order.
		return False
	return True
