sum=0
for i in range(0,10+1,1):
	sum+=i
# end for
print(sum)

sum=0
for i in range(11):
	sum+=i
# end for
print(sum)

i=0
sum=0
while(i<=10):
	sum+=i
	i+=1
# end while
print(sum)

i,sum=0,0
while(True):
	if i>10: break
	i+=1
	if i%2==0: continue
	sum+=i
# end for
print(sum)
