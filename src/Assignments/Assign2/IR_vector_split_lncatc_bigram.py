import math, collections
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
    posting, docText, docLen, N = {}, {}, {}, 0.
    for line in open(iF, encoding='utf-8'):
        N += 1
        docNo, doc = line.rstrip().split('\t')
        docText[docNo] = doc[:30]
        TF = collections.Counter(twogram(doc))

        # docLen[docNo]=math.sqrt(sum([(1+math.log(tf))**2 for tf in TF.values()]))
        V = []
        for tf in TF.values(): V.append((1 + math.log(tf)) ** 2)
        docLen[docNo] = math.sqrt(sum(V))

        for t, tf in TF.items():
            if t not in posting: posting[t] = []
            posting[t].append((docNo, tf))
    # end for
    # end for

    # df={t:len(posting[t]) for t in posting}
    df = {}
    for t in posting: df[t] = len(posting[t])

    return {'posting': posting, 'docText': docText, 'docLen': docLen, 'N': N, 'df': df}

# end def


def retrieval(Q, IndexDB):
    posting, docLen, N, df = IndexDB['posting'], IndexDB['docLen'], IndexDB['N'], IndexDB['df']
    score, qLen = {}, 0.
    qTF = collections.Counter(twogram(Q)) # 질의 tf
    maxTF = max(qTF.values())
    for qt, qtf in qTF.items():
        if qt not in posting: continue
        qtw = (0.5 + ((0.5 * qtf)/maxTF)) * math.log(N / df[qt])
        qLen += qtw * qtw
        for docNo, dtf in posting[qt]:
            if docNo not in score:
                score[docNo] = 0
            dtw = (1 + math.log(dtf))
            score[docNo] += qtw * dtw
    # end for
    # end for
    for docNo in score:
        score[docNo] /= math.sqrt(qLen) * docLen[docNo]
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
