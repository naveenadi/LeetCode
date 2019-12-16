class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        
        if len(a:=nums1) > len(b:=nums2):
            a, b = b, a
            
        n = len(a)
        m = len(b)
        
        median, i, j = 0, 0, 0
        
        min_index = 0
        max_index = n 

        while (min_index <= max_index) : 
            i = int((min_index + max_index) / 2) 
            j = int(((n + m + 1) / 2) - i) 

            if (i < n and j > 0 and b[j - 1] > a[i]) : 
                min_index = i + 1
            elif (i > 0 and j < m and b[j] < a[i - 1]) : 
                max_index = i - 1
            else : 
                if (i == 0) : 
                    median = b[j - 1] 
                elif (j == 0) : 
                    median = a[i - 1]		 
                else : 
                    median = maximum(a[i - 1], b[j - 1]) 
                break

        if ((n + m) % 2 == 1) : 
            return median 
        if (i == n) : 
            return ((median + b[j]) / 2.0) 
        if (j == m) : 
            return ((median + a[i]) / 2.0) 
        return ((median + minimum(a[i], b[j])) / 2.0)
    

def maximum(a, b) : 
	return a if a > b else b 

def minimum(a, b) : 
	return a if a < b else b 