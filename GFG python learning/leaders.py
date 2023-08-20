    
#For picking Leaders in an array i.e. if [23, 5,3,6, 6562,3, 6,3, 6,4, 5] then leaders are [5, 6, 6, 6562]
class Solution:
    #Back-end complete function Template for Python 3
    
    #Function to find the leaders in the array.
    def leaders(self, A, N):
        lst = []
        max_value = float('-inf')  
        """inf is used to represent positive infinity
     a value that is greater than any finite number. 
    It's a special floating-point value that indicates
     a value that is unbounded and beyond the scope of regular numeric values. 
    The counterpart of positive infinity is negative infinity (-inf), which 
    represents a value that is lower than any finite number."""
        for i in range(N-1, -1, -1):
            if A[i] > max_value:
                lst.append(A[i])
                max_value = A[i]
                
        lst.reverse()
        return lst

