d1='바그다드에서 발생한 폭탄 테러로 한국대사관의 유리창이 깨지는 등'
d2='아프간에서 일어난 자살 테러로 인해 최소 3명이 사망하고 17명이 부상하는 등'
d3='뭄바이에서 발생한 테러와 관련하여 한국대사관에서는 한국인들의 사망과 부상 피해를'

C=[d1,d2,d3]
Posting={}
for docNo,doc in enumerate(C):
    for t in doc.split():
        if t not in Posting: Posting[t]=[]
        Posting[t].append(docNo)
    # end for
# end for

while(True):
    Q=input('Query: ')
    score={}
    for qt in Q.split():
        if qt not in Posting: continue
        for docNo in Posting[qt]:
            if docNo not in score: score[docNo]=0
            score[docNo]+=1
        # end for
    # end for

    for docNo in sorted(score,key=score.get,reverse=True):
        print(score[docNo],C[docNo])
    # end for
# end while