def longest_common_substring(s1,s2):
	
	if len(s1)<len(s2):
		temp = s1
		s1 = s2
		s2 = temp
	m = len(s1)
	n = len(s2)

	res = 0
	end = 0
	l = [[0 for j in range(m)]for i in range(2)]
	cr = 0
	for i in range(m+1):
		for j in range(n+1):
			if i==0 or j==0:
				l[cr][j] = 0
			elif (s1[i-1]==s2[j-1]):
				l[cr][j] = l[1-cr][j-1]+1
				if l[cr][j]>res:
					res = l[cr][j]
					end = i-1
			else:
				l[cr][j] = 0
		cr = 1-cr
	if res==0:
		return -1
	return s1[end-res+1:end+1]
s1 = "abhishek"
s2 = "abhiswila"
m = len(s1)
n = len(s2)
print(longest_common_substring(s1,s2))