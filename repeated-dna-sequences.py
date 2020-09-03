class Solution:

    def findRepeatedDnaSequences(self, s: str) -> List[str]:        
        
        #Initialize a dict to count occurences of subsequences and an empty list for solution
        seqcounts = {}
        solution = []
        
        #Iterate over all 10-character subsequences in s:
        #   1. Get the count of each subsequence from dict (if not in dict, count = 0)
        #   2. If the subsequences was seen once before, add it to solution 
        #   3. Increase the count of the subsequence in dict by one
        for i in range(len(s)-9):
            seq = s[i:i+10]
            if (count := seqcounts.get(seq,0)) == 1:
                solution.append(seq)
            seqcounts[seq] = (count + 1)
        return solution
