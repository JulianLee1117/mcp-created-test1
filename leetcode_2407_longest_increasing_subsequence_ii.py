class Solution:
    def lengthOfLIS(self, nums: List[int], k: int) -> int:
        """
        LeetCode 2407: Longest Increasing Subsequence II
        
        Problem:
        Given an integer array nums and an integer k, return the length of the longest 
        subsequence of nums that is strictly increasing and has a difference of at most k 
        between any two consecutive elements.
        
        Approach:
        - Use Segment Tree to efficiently maintain the maximum length ending at each number
        - For each number x in nums, we query the maximum length in range [x-k, x-1]
        - Update the segment tree with the new maximum length at position x
        
        Time Complexity: O(n * log(max_val))
        Space Complexity: O(max_val)
        """
        def update(index: int, val: int, tree: List[int], size: int) -> None:
            index += size  # Shift index to leaf node position
            tree[index] = val
            while index > 1:
                index //= 2
                tree[index] = max(tree[index * 2], tree[index * 2 + 1])

        def query(left: int, right: int, tree: List[int], size: int) -> int:
            left += size
            right += size
            result = 0
            while left <= right:
                if left % 2 == 1:
                    result = max(result, tree[left])
                    left += 1
                if right % 2 == 0:
                    result = max(result, tree[right])
                    right -= 1
                left //= 2
                right //= 2
            return result

        # Find the maximum value in nums to determine segment tree size
        max_val = max(nums)
        size = 1
        while size <= max_val:
            size *= 2
            
        # Initialize segment tree
        tree = [0] * (2 * size)
        
        # Process each number
        result = 1
        for num in nums:
            # Query the maximum length in range [num-k, num-1]
            left = max(0, num - k)
            right = num - 1
            curr_len = 1
            if left <= right:
                curr_len = query(left, right, tree, size) + 1
            
            # Update the maximum length ending at current number
            update(num, curr_len, tree, size)
            result = max(result, curr_len)
            
        return result