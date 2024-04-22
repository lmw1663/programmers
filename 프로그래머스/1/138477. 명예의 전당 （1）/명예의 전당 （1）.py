def solution(k, score):
    representation=[]
    scores=[]
    for i in range(len(score)):
        representation.append(score[i])
        representation = sorted(representation,reverse=True)       
        if i<k:
            scores.append(representation[i])
        else:
            scores.append(representation[k-1])
        
    return scores