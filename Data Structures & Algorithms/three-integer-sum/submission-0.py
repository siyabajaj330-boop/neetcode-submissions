class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        # Pseudocode:
        # For each num in nums: 
        # Check if target - num exists in the dictionary, and if so, append those pairs to this index 


        # Basically ,
        # Keep a dict mapping sums -> pairs of indexes that make up that sum
        # For each num in nums:
        # We know we need two other nums that add up to target - num
        # Check if target - num exists in the dict, if so, use that pair and add those indexes to 
        # num's index (if it hasnt already been accounted for)

        numPairs = defaultdict(list)
        numIndexes = dict()

        for i in range (len(nums)):
            num = nums[i]
            numIndexes[num] = i


        for i in range (len(nums)):
            num = nums[i]
            for otherNum, otherIndex in numIndexes.items():
                if (otherIndex != i):
                    newSum = num + otherNum
                    numPairs[newSum].append((i, otherIndex))

        #print(numPairs)

        res = []
        usedTriples = set()
        for i in range (len(nums)):
            num = nums[i]
            diff = 0 - num
            if numPairs.get(diff):
                for indexPair in numPairs.get(diff):
                    index1, index2 = indexPair
                    newTriple = (nums[i], nums[index1], nums[index2])
                    if (newTriple not in usedTriples) and (index1 != index2) and (i != index1) and (i != index2):
                        print(index1, index2, i)
                        res.append( [nums[i], nums[index1], nums[index2]] )
                        usedTriples.add((nums[i], nums[index1], nums[index2]))
                        usedTriples.add((nums[i], nums[index2], nums[index1]))
                        usedTriples.add((nums[index1], nums[index2], nums[i]))
                        usedTriples.add((nums[index1], nums[i], nums[index2]))
                        usedTriples.add((nums[index2], nums[i], nums[index1]))
                        usedTriples.add((nums[index2], nums[index1], nums[i]))

           # print(usedTriples)

        return res







