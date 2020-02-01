# The greedy approach will work, because DP cannot achieve better.
# Can do better than this with Next Greater Element
​
class Solution:
    def mctFromLeafValues(self, arr: List[int]) -> int:
        if not arr:
            return 0
        cost = 0
        while len(arr) > 1:
            
            minVal = float('inf')
            minPos = -1
            for indx, val in enumerate(arr):
                if val < minVal:
                    minVal, minPos = val, indx
            
            left = float('inf')
            right = float('inf')
            
            if minPos-1 >= 0:
                left = arr[minPos-1]
            if minPos+1 < len(arr):
                right = arr[minPos+1]
            
            
            if(left <= right):
                newVal = left
                cost += left * minVal
                arr.remove(minVal)
                arr[minPos-1] = newVal
            else:
                newVal = right
                cost += right * minVal
                arr.remove(minVal)
                arr[minPos] = newVal
        
        return cost
                
