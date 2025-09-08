def solution(i, j, k):
    answer = 0
    
    for x in range(i,j+1):
        for z in range(len(str(x))):
            str_x = str(x)
            if int(str_x[z]) == k : 
                answer += 1
        i+=1
        
    return answer