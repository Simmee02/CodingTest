def solution(n, m):
    
    def gcd(x,y):
        while y != 0:
            x, y = y, x % y
        return x
    
    gcd_value = gcd(n,m)
    lcm_value = n*m // gcd_value

    answer = [gcd_value,lcm_value]
    
    return answer