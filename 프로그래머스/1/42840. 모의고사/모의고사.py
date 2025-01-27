def solution(answers):
    answer = []
    A = [1,2,3,4,5]
    B = [2,1,2,3,2,4,2,5]
    C = [3,3,1,1,2,2,4,4,5,5]
    
    list_person = [A,B,C]
    scores = [0, 0, 0]
    
    for i in range(len(list_person)):
        pattern = list_person[i]
        for j in range(len(answers)):
            if answers[j] == pattern[j%len(pattern)]:
                scores[i] +=1
        
    max_score = max(scores)
    for i in range(len(scores)):
        if scores[i] == max_score:
            answer.append(i+1)
    
    return answer