import math
import re

def twogram(doc):
    grams = []
    doc = re.split('[\s\(\)\,\;\.]+', doc)
    for t in doc:
        if len(t) == 1:
            grams.append(t)
            continue
        for i in range(len(t)):
            if i+1 < len(t) and re.match("[^a-zA-Z\-]", t[i]):
                grams.append(t[i:i+2])
            elif i == len(t)-1 and re.match("[^a-zA-Z]", t[i]) and re.match("[a-zA-Z]", t[i-1]):
                grams.append(t[i])
            else:
                if i != 0 and re.match("[a-zA-Z\-]", t[i-1]):
                    if i < len(t)-1 and re.match("[^a-zA-Z]", t[i+1]):
                        grams.append(t[0:i+1])
                    if i == len(t)-1:
                        grams.append(t[0:i+1])
                else:
                    continue
    return grams


def indexing(iF):
    posting, docText, docLen = {}, {}, {}
    for line in open(iF, encoding='utf-8'):
        docNo, doc = line.rstrip().split('\t') # 탭을 기준으로 인덱스와 내용을 분리해서 나눔.
        docText[docNo] = doc[:30] # 나눈 인덱스를 키값으로 내용을 벨류로 딕셔너리에 넣는다.
        termSet = set(twogram(doc)) # 내용들을 공백을 기준으로 set에 기입한다.
        docLen[docNo] = math.sqrt(len(termSet))
        for t in termSet:
            if t not in posting:
                posting[t] = []
            posting[t].append(docNo)
    # end for
    # end for
    return {'posting': posting, 'docText': docText, 'docLen': docLen}


# end def

def retrieval(Q, IndexDB):
    posting, docLen = IndexDB['posting'], IndexDB['docLen']
    score = {}
    termSet = set(twogram(Q))
    for t in termSet:
        if t not in posting: continue
        for docNo in posting[t]:
            if docNo not in score:
                score[docNo] = 0
            score[docNo] += 1
    # end for
    # end for
    qLen = math.sqrt(len(termSet)) ## 질의 길이
    for docNo in score:
        score[docNo] /= qLen * docLen[docNo]
    # end for
    return score


# end def

IndexDB = indexing('collection')
while (True):
    q = input('Query: ')
    score = retrieval(q, IndexDB)
    for docNo in sorted(score, key=score.get, reverse=True)[:10]:
        print('%.4f\t%s\t%s' % (score[docNo], docNo, IndexDB['docText'][docNo]))
# end for
# end while
