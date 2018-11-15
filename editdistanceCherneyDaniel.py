# Edit Distance by Daniel Cherney CWID: 889195004
# Computes the Edit Distance between two words
# Produces the optimal alignment
# Ensure that you have python3 installed on your system
# Run the program on command line by using the following syntax:
# python3 editdistanceCherneyDaniel.py [argument1] [argument2]
# If on windows,

#If on windows, comment the following section out

#!/usr/bin/python

import sys

word1 = sys.argv[1]
word2 = sys.argv[2]

#If on windows, uncomment this section

#word1 = input("What is word one: ")
#word2 = input("What is word two: ")

def edit_distance(word1, word2):
	word1 = word1.lower()
	word2 = word2.lower()
	len1 = len(word1)
	len2 = len(word2)

	if len2 > len1:
		temp = word2
		word2 = word1
		word1 = temp
		temp = len2
		len2 = len1
		len1 = temp

	if len1 == 0:
		return len2
	
	columns = len1 + 1
	rows = len2 + 1
	graph = [[0 for x in range(columns)] for x in range(rows)]
	
	for i in range(1, rows):
		graph[i][0] = i

	for i in range(1, columns):
		graph[0][i] =i

	for i in range(0, len2):
		for j in range(0, len1):
			top = graph[i][j+1]
			left = graph[i+1][j]
			diag = graph[i][j]
			if word2[i] == word1[j]:
				graph[i+1][j+1] = diag
			else:
				if top + 1 < left + 1 and top + 1 < diag + 1:
					graph[i+1][j+1] = top + 1
				elif left + 1 < top + 1 and left + 1 < diag + 1:
					graph[i+1][j+1] = left + 1
				else:
					graph[i+1][j+1] = diag + 1

	print("\nThe matrix:\n")

	for i in range(rows):
		print(graph[i])

	print("\nThe edit distance is: " + str(graph[len2][len1]) + "\n")

	print("The optimal alignment is: \n")
	print(word1)

	word = 0
	x = 0
	y = 0
	position = graph[x][y]
	while x != len2 and y != len1:
		if x <= len2-1:
			right = graph[x+1][y]
		else:
			right = 1000
		if y <= len1-1:
			bottom = graph[x][y+1]
		else:
			bottom = 1000
		if x <= len2-1 and y <= len1-1:
			diag = graph[x+1][y+1]
		else:
			diag = 1000
	
		if diag < bottom and diag < right:
			print(word2[word], end='')
			word = word + 1
			position = graph[x+1][y+1]
			x = x + 1
			y = y + 1
		if bottom < diag and bottom < right and right == 1000:
			print(word2[word], end='')
			word = word + 1
			position = graph[x][y+1]
			y = y + 1
		if bottom < diag and bottom < right:
			print("_", end='')
			position = graph[x][y+1]
			y = y + 1
		if right < diag and right < bottom and bottom == 1000:
			print(word2[word], end='')
			word = word + 1
			position = graph[x+1][y]
			x = x + 1
		if right < diag and right < bottom:
			print("_", end='')		
			position = graph[x][y+1]
			y = y + 1
		if right == diag == bottom:
			print(word2[word], end='')
			word = word + 1
			position = graph[x+1][y+1]
			y = y + 1
			x = x + 1

	print("\n")
edit_distance(word1,word2)
