import math
def solution(w,h) :
    if math.gcd(w, h) == 1:
        return (w-1) * (h-1)
    elif math.gcd(w, h) != 1:
        return ((w-1) * (h-1)) + (math.gcd(w, h)-1)