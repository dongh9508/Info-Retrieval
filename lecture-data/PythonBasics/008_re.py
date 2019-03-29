import	re

s='2015-11-10 13:45:21 (Tue)'
print(re.split(':',s))
print(re.split('[-:]',s))
print(re.split('[-:\s]+',s))
print(re.split('[-:\s\(\)]+',s))
m=re.search('(\d\d\d\d)',s)
if m: print(m.group(1))
print(re.findall('\d+',s))
