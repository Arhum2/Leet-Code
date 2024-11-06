# given x and n return x^n

def myPow(x: float, n: int) -> float:
    #recursive helper
    def helper(x, n):
        #base case's
        if x == 0:
            return 0

        if n == 0:
            return 1
        
        #divide and conquer, keep dividing n by 2 and building up the result
        res = helper(x, n//2)
        #if n is even, return res*res
        res = res*res

        #if n is odd, return x*res*res since we miss one x in the division
        if n % 2 == 1:
            return x * res
        else:
            return res

    #if n is negative, return 1/res
    res = helper(x, abs(n))
    if n >= 0:
        return res
    else:
        return 1/res

myPow(2, 10) # 1024