D={}
D={'Obama':87, 'Clinton':95, 'Bush':91}
print(D)
print(len(D))
print(D['Bush'])

if 'Obama' in D: print('Obama is in D')
else: print('Obama is not in D')

if 'Bush' not in D: print('Bush is not in D')
else: print('Bush is in D')

D['Lincoln']=100
print(D)

del D['Bush']
print(D)

for key in D:
	print(key,D[key])
# end for

for key in sorted(D): # sort by key
	print(key,D[key])
# end for

for key in sorted(D,key=D.get,reverse=True): # sort by value in descending order
	print(key,D[key])
# end for
