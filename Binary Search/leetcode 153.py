#首先判断数组是否为空，如果为空，直接返回
#题目需要时间复杂度为O(logn),则想到二分查找法。
#设定左右边界后，判断中间值和左边届大小，若中间值大于左边界值
#说明左半部分为上升的数组，其发生循环的位置在右边。所以将更新左边界
#同时也更新最小值。同理，在右边界也需要更新最小值
# using result to store the min value
# if the value in the mid is bigger than the value in the left index
# the target should be in the right side of the Array. but it also might be the value in the left index
# so it is need to update the result = min (result, nums[left]), and set the left = mid + 1
# else update the result = min (result, nums[mid]) and set the right = mid -1


class Solution:
    def findMin(self, nums: List[int]) -> int:
        if nums is None:
            return
        left, right, result = 0, len(nums) - 1, nums[0]

        while left <= right:
            mid = (left + right) // 2
            if nums[mid] >= nums[left]:
                result = min(result, nums[left])
                left = mid + 1
            else:
                result = min(result, nums[mid])
                right = mid - 1
        return result
