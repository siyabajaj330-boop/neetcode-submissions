class Solution:
    from collections import defaultdict

    def twoSum(self, numbers: List[int], target: int) -> List[int]:
       
        freqs = defaultdict(int)
        indices = defaultdict(set)

        for i in range (len(numbers)):
            num = numbers[i]
            freqs[num] += 1
            indices[num].add(i + 1) # 1-indexed 

        

        for num in numbers:
            diff = target - num
            if (freqs[diff] >= 1) and ((diff != num) or (len(indices[num]) > 1)):
                index1 = indices[num]
                index2 = indices[diff]
                if (diff == num):
                    return [min(indices[num]), max(indices[num])]
                
                index1 = indices[num].pop()
                index2 = indices[diff].pop()
                return [index1, index2] if index1 < index2 else [index2, index1]

