iF=open('i.txt')
for line in iF:
	print(line)
# end for

iF=open('i.txt')
oF=open('o.txt','w')
for line in iF:
	L=line.rstrip().split()
	for t in L:
		print(t)
		oF.write(t+'\n')
	# end for
# end for
oF.close()
