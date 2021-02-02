lass Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        ans = 0
        mx = ans
        for i in gain:
            ans+=i
            if ans > mx:
                mx=ans
        return mx