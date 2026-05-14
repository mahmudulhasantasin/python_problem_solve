from collections import Counter

class Solution:
    def intersect(self, nums1, nums2):
        # count frequencies of nums1
        freq = Counter(nums1)
        
        result = []
        
        # check nums2 against frequency map
        for num in nums2:
            if freq[num] > 0:
                result.append(num)
                freq[num] -= 1
        
        return result