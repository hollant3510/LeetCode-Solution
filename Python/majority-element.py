from __future__ import print_function
# Time:  O(n)
# Space: O(1)

import collections

class Solution:
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        idx, cnt = 0, 1

        for i in xrange(1, len(nums)):
            if nums[idx] == nums[i]:
                cnt += 1
            else:
                cnt -= 1
                if cnt == 0:
                    idx = i
                    cnt = 1

        return nums[idx]

    def majorityElement2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return sorted(collections.Counter(nums).items(), key=lambda a: a[1], reverse=True)[0][0]

if __name__ == "__main__":
    print(Solution().majorityElement([1, 2, 3, 4, 5, 5, 5, 5, 5, 5, 6]))

