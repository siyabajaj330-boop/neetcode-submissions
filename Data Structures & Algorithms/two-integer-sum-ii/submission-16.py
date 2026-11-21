class Solution:
    from collections import defaultdict

    def twoSum(self, numbers: List[int], target: int) -> List[int]:
       
        freq = defaultdict(int)
        indices = defaultdict(set)
        for i in range (len(numbers)):
            num = numbers[i]
            indices[num].add(i + 1)
            freq[num] += 1

        for i in range (len(numbers)):
            num = numbers[i]
            diff = target - num
            if (num == diff) and freq[diff] >= 2:
                index1 = indices[num].pop()
                index2 = indices[num].pop()
                return [index1, index2] if index1 < index2 else [index2, index1]
            elif diff != num and freq[diff] >= 1:
                index1 = indices[num].pop()
                index2 = indices[diff].pop()
                return [index1, index2] if index1 < index2 else [index2, index1]
            else:
                continue

        

            