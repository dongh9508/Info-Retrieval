from stemming.porter2 import stem

posting = ['automate', 'automated', 'automates', 'automating', 'automation', 'operate', 'operating', 'operates', 'operation', 'operative', 'operatives', 'operational']

for element in posting :
    print(element + " : " + stem(element))

