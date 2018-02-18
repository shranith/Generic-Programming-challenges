# http://algorithms.tutorialhorizon.com/separate-even-and-odd-integers-in-a-given-array/


def separateevenodd(arr):
	m = 0
	n = len(arr) - 1
	while 1:
		while arr[m]&1 == 0:
			m+=1
		while arr[n]&1 == 1:
			n-=1
		if m >= n:
			break
		c = arr[n]
		arr[n] = arr[m]
		arr[m] = c
	print(arr)

def main():
	arr = [1,2,3,4,5,6,7,8,9,10]
	separateevenodd(arr)


if __name__ == '__main__':
	main()