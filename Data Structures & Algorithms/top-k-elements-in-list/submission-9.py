# Input: nums = [1,2,2,3,3,3], k = 2

# topK = { (3, 3), (2, 2) }
# others = { (1, 1) }

# Pseudocode:
# Keep 2 sets: 1 with the top k frequent elems so far, and one with the rest 

# For each num in nums:
# if len(topK) < k:
    # add (nums, freq to k)
# else:
    # if freq of num is > minFreq in topK set, swap (num, freq) with (otherNum, otherFreq)

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        frequencies = dict()
        topK = set()
        others = set()

        for num in nums:
            #print(f"TopK: {topK} Others: {others}\n")

            if frequencies.get(num) is None:
                frequencies[num] = 1
            else:
                frequencies[num] += 1
        
            numFreq = frequencies[num]
                
            minFreqInTopK = None
            if (len(topK) > 0):
                minFreqInTopK = min(topK, key=lambda item: item[1])
            
            # Cases:

            # if this number is already in our top K, just update the frequency 
            if ((num, numFreq - 1) in topK):
                topK.remove((num, numFreq -1))
                topK.add((num, numFreq))
            
            # if this number is not in our top K, but now surpasses another number from topK
            elif (minFreqInTopK is not None) and (numFreq > minFreqInTopK[1]) and (num != minFreqInTopK[0]):
                others.add(minFreqInTopK)
                topK.remove(minFreqInTopK)
                topK.add((num, numFreq))

                if ((num, numFreq) in others):
                    others.remove((num, numFreq))
            
            elif len(topK) < k:
                topK.add((num, numFreq))
            
            else:
                others.add((num, numFreq))

        res = []
        for elem in topK:
            res.append(elem[0])
        return res





topK = { (5, 1), (1, 3) }
others = { (3, 1) }
        