class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        seen = dict()

        # O(n)
        for i in range (len(numbers)):

            # O(1)
            num = numbers[i]
            need = target - num
            
            # O(1)
            if (seen.get(need) is not None) and seen.get(need) != i:
                return [seen.get(need) + 1, i + 1] if seen.get(need) < i else [i + 1, seen.get(need) + 1]

            # O(1)
            seen[num] = i
        