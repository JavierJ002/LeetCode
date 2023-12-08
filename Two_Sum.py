class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i = 0
        j = len(numbers) - 1
        resp = []
        while i < j:
            if numbers[i] + numbers[j] == target:
                resp.append(i+1)
                resp.append(j+1)
                return resp
            if numbers[i] + numbers[j] < target:
                i += 1
            if numbers[i] + numbers[j] > target:
                j-= 1
