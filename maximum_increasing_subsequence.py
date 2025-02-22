from typing import List, Tuple

class Solution:
    def maxSumIncreasingSubsequence(self, nums: List[int]) -> Tuple[int, List[int]]:
        """
        Find the maximum sum increasing subsequence in an array.
        Returns both the maximum sum and the subsequence that forms it.
        
        Args:
            nums: List of integers
            
        Returns:
            Tuple containing:
                - Maximum sum of any increasing subsequence
                - List of numbers forming that subsequence
                
        Time Complexity: O(n^2)
        Space Complexity: O(n)
        
        Example:
            Input: [1, 101, 2, 3, 100, 4, 5]
            Output: (106, [1, 2, 3, 100])
        """
        if not nums:
            return (0, [])
            
        n = len(nums)
        
        # dp[i] stores the maximum sum of increasing subsequence ending at index i
        dp = nums.copy()
        
        # prev[i] stores the previous index in the maximum sum increasing subsequence
        prev = [-1] * n
        
        # Index of the maximum sum found so far
        max_sum_index = 0
        
        # For each position, look at all previous positions
        for i in range(1, n):
            for j in range(i):
                # If current number is greater than previous number and
                # including it gives a better sum
                if nums[i] > nums[j] and dp[j] + nums[i] > dp[i]:
                    dp[i] = dp[j] + nums[i]
                    prev[i] = j
            
            # Update max_sum_index if we found a better sum
            if dp[i] > dp[max_sum_index]:
                max_sum_index = i
        
        # Reconstruct the sequence
        sequence = []
        current = max_sum_index
        while current != -1:
            sequence.append(nums[current])
            current = prev[current]
        
        # Return the maximum sum and the reversed sequence
        return (dp[max_sum_index], sequence[::-1])

    def maxSumIncreasingSubsequenceBinarySearch(self, nums: List[int]) -> Tuple[int, List[int]]:
        """
        Alternative implementation using binary search for better time complexity.
        This version is more efficient for larger inputs.
        
        Time Complexity: O(n log n)
        Space Complexity: O(n)
        """
        from bisect import bisect_left
        
        if not nums:
            return (0, [])
            
        # piles[i] stores the smallest number that can end an increasing subsequence of length i+1
        piles = []
        # pile_sums[i] stores the maximum sum achievable for a subsequence of length i+1
        pile_sums = []
        # prev[i] stores the index of the previous number in the sequence ending at i
        prev = [-1] * len(nums)
        # value_to_pile[i] maps value to its pile for reconstruction
        value_to_pile = {}
        
        for i, num in enumerate(nums):
            pile_idx = bisect_left(piles, num)
            
            curr_sum = num
            if pile_idx > 0:
                curr_sum += pile_sums[pile_idx - 1]
                
            if pile_idx == len(piles):
                piles.append(num)
                pile_sums.append(curr_sum)
            elif curr_sum > pile_sums[pile_idx]:
                piles[pile_idx] = num
                pile_sums[pile_idx] = curr_sum
                
            value_to_pile[num] = pile_idx
            
            if pile_idx > 0:
                for prev_num, prev_pile in value_to_pile.items():
                    if prev_pile == pile_idx - 1 and prev_num < num:
                        prev[i] = nums.index(prev_num)
                        break
        
        # Reconstruct the sequence
        sequence = []
        current_value = piles[-1]
        current_index = nums.index(current_value)
        
        while current_index != -1:
            sequence.append(nums[current_index])
            current_index = prev[current_index]
        
        return (pile_sums[-1], sequence[::-1])

# Example usage and tests
def run_tests():
    solution = Solution()
    
    test_cases = [
        [1, 101, 2, 3, 100, 4, 5],
        [3, 10, 2, 1, 20],
        [1, 2, 3, 4, 5],
        [5, 4, 3, 2, 1],
        [10, 5, 4, 3],
    ]
    
    for nums in test_cases:
        max_sum, sequence = solution.maxSumIncreasingSubsequence(nums)
        print(f"Input: {nums}")
        print(f"Maximum sum: {max_sum}")
        print(f"Sequence: {sequence}")
        print()
        
        # Verify with binary search version
        max_sum_bs, sequence_bs = solution.maxSumIncreasingSubsequenceBinarySearch(nums)
        assert max_sum == max_sum_bs, f"Mismatch in sum: {max_sum} vs {max_sum_bs}"
        print("Binary search version verified ✓")
        print("-" * 50)