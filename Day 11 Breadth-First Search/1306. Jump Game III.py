class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        def helper(pos: int) -> bool:
            if 0 <= pos < len(arr) and arr[pos] < len(arr) and pos not in seen:
                seen.add(pos)
                return arr[pos] == 0 or helper(pos + arr[pos]) or helper(pos - arr[pos])
            return False
    
        seen = set()
        return helper(start)