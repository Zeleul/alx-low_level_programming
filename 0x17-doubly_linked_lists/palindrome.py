#!usr/bin/python3
product = (a * b for a in range(999, 99, -1) for b in range(a, 99, -1))
print(sorted(filter(lambda a: str(a) == str(a)[::-1], product))[-1])

# or
#def ispalindrome(n):
#    string = str(n)
#   return string == string[::-1]
#
#arr = []
#for i in range(999, 99, -1):
#    for j in range(i, 99, -1):
#        if ispalindrome(i * j):
#            arr.append(i * j)
#print(max(arr))
		
