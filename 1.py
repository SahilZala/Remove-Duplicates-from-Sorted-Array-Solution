class Solution(object):
    def removeDuplicates(self, nums):
        dup = []
        for i in nums:
            pointer = 0
            for j in dup:
                if j == i:
                    pointer = 1

            if pointer == 0:
                dup.append(i)
        print(dup.__len__())

s = Solution()
s.removeDuplicates([1,1,2])