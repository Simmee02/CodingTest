def solution(array):
    answer = 0
    
    for i in range (len(array)):
        array_list = str(array[i])
        for j in range (len(array_list)):
            if array_list[j] == "7":
                answer += 1
        
    return answer