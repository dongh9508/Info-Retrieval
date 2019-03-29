import	shelve

DB=shelve.open('score.db',flag='n')
DB['Obama']='US'
DB['Bush']='UK'
DB['Clinton']='China'
DB.close()

DB2=shelve.open('score.db')
for t in DB2:
	print(t,DB2[t])
# end for
