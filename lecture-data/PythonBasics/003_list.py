L=[]
L=['a','b','c','d']
print(L)
print(L[0])
print(L[-1])
print(len(L))
L.append('e')
del L[0]
s='-'.join(L)
print(s)

s='ZZZ ABC DEF GHI JKL'
print(s)
L=s.split()
print(L)

if 'ABC' in L: print('ABC is in L')
else: print('ABC is not in L')

for e in L:
	print(e)
# end for

print()

for e in sorted(L):
	print(e)
# end for

print()

for e in sorted(L,reverse=True):
	print(e)
# end for

print()

for i in range(len(L)):
	print(i,L[i])
# end for

print()

for i in range(0,len(L),1):
	print(i,L[i])
# end for

print()

for i in range(len(L)-1,-1,-1):
	print(i,L[i])
# end for
