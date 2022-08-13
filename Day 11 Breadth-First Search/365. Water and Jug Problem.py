class Solution:
    def canMeasureWater(self, x: int, y: int, z: int) -> bool:
        def gcd(x, y):
            if x < y : 
                x, y = y, x
            while x != y and y != 0 :
                remainder = x % y 
                x = y
                y = remainder
            return x
        
        g = gcd(x,y)
        if g == 0:
            return z == 0
        return (x+y) >= z and z % g == 0 