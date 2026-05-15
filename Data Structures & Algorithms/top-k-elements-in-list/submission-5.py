class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency = {}
        for value in nums:
            if value in frequency:
                frequency[value]+=1
            else:
                frequency[value]=1

        arr = []
        for num, cnt in frequency.items():
            arr.append([cnt, num])
        arr.sort()

        res = []
        while len(res) < k:
            res.append(arr.pop()[1])
        return res


