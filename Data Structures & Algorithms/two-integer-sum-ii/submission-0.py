class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        seen = dict()

        for i in range (len(numbers)):
            num = numbers[i]
            need = target - num
            if (seen.get(need) is not None) and seen.get(need) != i:
                return [seen.get(need) + 1, i + 1] if seen.get(need) < i else [i + 1, seen.get(need) + 1]
            seen[num] = i
        