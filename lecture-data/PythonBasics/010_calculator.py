import	sys,re

def sum(n1,n2):
	return int(n1)+int(n2)
# end def

def main():
	while(True):
		e=input('Enter expression(+,-,*,/): ')
		m=re.search('^\s*(\d+)\s*([\+\-\*\/])\s*(\d+)\s*$',e)
		if not m: continue
		n1,op,n2=m.group(1),m.group(2),m.group(3)	
		if op=='+': print(sum(n1,n2))
	# end while	
# end def

if __name__=='__main__':
        sys.exit(main())
# end if
