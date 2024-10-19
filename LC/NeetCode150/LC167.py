class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # Optimized
        # Two pointer Approach
        # Since the array is sorted we will try to find the sum by keeping two pointers and check for the sum
        # n
        # 1

        left, right = 0,len(numbers) - 1

        while(left<=right):
            print(left,right)
            if numbers[left] + numbers[right] == target:
                return [left+1,right+1]

            elif numbers[left] + numbers[right] > target:
                right-=1
            
            else:
                left+=1

        return -1