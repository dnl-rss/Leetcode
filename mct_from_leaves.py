class Solution:
    def mctFromLeafValues(self, arr: List[int]) -> int:
        """
        Recursive property:         
            for any non-leaf node, 
            mct(node) = mct(node.left) + mct(node.right) + node.val
            node.val = maxleaf(node.left) + maxleaf(node.right)
        
        BASE CASE 1: only 1 leaf, mct([x1]) = 0
        BASE CASE 2: only 2 leaves, implies one parent above, node.val = x1*x2, mct([x1,x2]) = x1*x2
        RECURSIVE CASE: more than 2 leaves, mct([arr]) is the minimum of all possibilities resulting from split of L and R subarrays
            mct[arr] = min( [ mct(arr[:k]) + mct(arr[k:]) + max(arr[:k])*max(arr[k:]) for k in range(len(arr)) ] ) 
        
        -------------------------------------------------------------
        Ex1
        arr = [6,2,4]
        
        mct([6,2,4] = min(
            mct([6]) + mct([2,4]) + max([6])*max([2,4]) , 
            mct([6,2]) + mct([4]) + max([6,2])*max([4])
        )
        
        Results array:                      
                                                *not mct        *mct
        mct([6]) mct([2]) mct([4])              6   2      |     2   4   
             0        0        0                 \  /      |      \  /
           mct([6,2]) mct([2,4])                  12   4   |   6    8
                12          8                      \  /    |    \  /
                mct([6,2,4])                        24     |     24
                      32 = 12+0+(6*4)                           
        ----------------------------------------------------------
        Ex2
        arr = [2,4,1]
        
        mct([2,4,1] = min(
            mct([2]) + mct([4,1]) + max([2])*max([4,1]) , 
            mct([2,4]) + mct([1]) + max([2,4])*max([1])
        )
        
        Results array:                      
                                                *two possible mcts
        mct([2]) mct([4]) mct([1])              2   4      |     4   1   
             0        0        0                 \  /      |      \  /
           mct([2,4]) mct([4,1])                   8   1   |   2    4
                 8          4                      \  /    |    \  /
                mct([6,2,4])                         4     |     8
                      12 = 8+0+(4*1) or 4+0+(4*2)          
        -----------------------------------------------------------
        Ex3
        arr = [6,2,4,1]
        
        mct([6,2,4,1]) = min(
            mct([6]) + mct([2,4,1]) + max([6])*max([2,4,1])
            mct([6,2]) + mct([4,1]) + max([6,2])*max([4,1])
            mct([6,2,4]) + mct([4]) + max([6,2,4])*max([1])
        ) 
        
        Results array:
                                                        *mct
        mct([6]) mct([2]) mct([4]) mct([1])                 4   1
            0*         0        0        0                  \   /
         mct([6,2]) mct([2,4]) mct([4,1])                2    4
              12          8          4                    \   /
             mct([6,2,4])   mct([2,4,1])                6    8 
                   32             12*                    \  /
                     mct([6,2,4,1])                       24 
                            36 = min( 0+12+(6*4), 12+4+(6*4), 32+0+(6*1) )
        ----------------------------------------------------------------------
        
        bottom-up approach:
        to find mct(arr), we need the results from every possible split of L and R subarrays
        store these results in an array doubly indexed by (start_index, length)
        """
        
        length = 1
        
        # DP lookup table, indexed by (length, start_index)
        mcts = {}
        
        # Base Case 0: no leaves, mct = None, this is not really necessary
        mcts[0] = [None]*len(arr)

        # Base Case 1: only 1 leaf, mct=0
        mcts[1] = [0 for x1 in arr]
            
        # Base Case 2: only 2 leaves, mct = x1*x2
        mcts[2] = [ arr[i]*arr[i+1] for i in range(len(arr)-1) ]
            
        # Recursive Case:
        # Start with the smallest recursive case (l=3) building upon results of the base cases, and compute results for all l=3,4,...len(arr)
        for l in range(3,len(arr)+1):
            mcts[l] = []
            
            # For all possible subarrays of the given length l, 
            # iterate through all the possible starting locations s=0,1,2,...len(arr)-l
            for s in range(len(arr)+1-l):
                
                # We must compute the mct for each of these subarrays, all of with can be subdivided at possible position k=1,2,...len(subarray)
                # Take the minimum value of the resulting possibilities 
                #                    lookup mcts of subarrays               / add node value             / for all possible cut locations k
                #                       length k    remainder of the length / product max L and R leaves    
                #                         at s        after s finishes
                mcts[l].append( min( [ mcts[k][s] + mcts[l-k][s+k] + max(arr[s:s+k])*max(arr[s+k:s+l]) for k in range(1,l)] ) )        
        
        # By the end of the loop, the mct for the longest possible length (the whole array) should exist
        # Return that result
        return mcts[len(arr)][0]
