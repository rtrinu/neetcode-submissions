class Solution:
    def mySqrt(self, x: int) -> int:
        l = 0
        r=x
        while l <= r:
            m = (l+r)//2
            product= m*m
            if product > x:
                r = m -1
            elif product <x :
                l = m+1
                result = m
            else:
                return m
        return result