# 根据中间值和左边届值比较，得到哪边是已经排好序的，然后再判断目标值是否在排好续中的序列当中，来更新左右边界。
# if nums[mid] == target then return mid
# if nums[mid] > nums[left], means the left side is Sorted.
    # let's judge the target whether in  the sorted ascending side of the Array.
    #  if nums[left] <= target and target < nums[mid]
    # r = mid -1
    # else: the target should in  the right side l = mid + 1
# else: means the right side is sorted.
    # let's judge the target whether in  the sorted ascending side of the Array.
    # if nums[mid] < target and target <= nums[right]
    # l = mid + 1
    # else: r = mid - 1




class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == target:
                return mid
            if nums[mid] >= nums[l]:
                if nums[l] <= target and target < nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1
            else:
                if nums[mid] < target  and target <= nums[r]:
                    l = mid + 1
                else:
                    r = mid -1

        return -1
