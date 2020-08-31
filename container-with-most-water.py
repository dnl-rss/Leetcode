class Solution:
    def maxArea(self, height: List[int]) -> int:
        '''
        The container with the most water can be found as such:
        
        1. Initialize a left bound index (L) as zero, 
              right bound index (R) as n (length of 'height' array), 
              and max container area tracker (maxA) as zero
        2. Repeat this loop n times:
           a. Compute the area (A) contained by the rectangle 
                formed by the smaller height of the L/R bounds, 
                and the horizontal distance between them
           b. Increment the smaller height of the L/R by one 
                (increase for L, decrease for R) 
           c. If A is greater than maxA, update maxA with the value of A 
        3. When loop (2.) terminates, 
            maxA has the value of the maximum area container 
            bounded by the 'height' array
        '''
        L = 0
        R = len(height)-1
        
        maxA = 0
        
        for i in range(len(height)):
            
            #Compute area
            if height[L] < height[R]: 
                A = height[L]*(R-L)
                L += 1
            else:
                A = height[R]*(R-L)
                R -= 1
                
            #Update max
            if maxA < A:
                maxA = A
        
        return maxA
