class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # Sort the array to use two-pointer technique
        nums.sort()
        result = []
        n = len(nums)
        
        # Iterate through the array
        for i in range(n-2):
            # Skip duplicates for i
            if i > 0 and nums[i] == nums[i-1]:
                continue
                
            # Use two pointers technique
            left = i + 1
            right = n - 1
            
            while left < right:
                current_sum = nums[i] + nums[left] + nums[right]
                
                if current_sum == 0:
                    # Found a valid triplet
                    result.append([nums[i], nums[left], nums[right]])
                    
                    # Skip duplicates for left
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    # Skip duplicates for right
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                        
                    left += 1
                    right -= 1
                    
                elif current_sum < 0:
                    left += 1
                else:
                    right -= 1
                    
        return result