def find(self, nums, low, high, target):
    res = []
    while low < high:
        s = nums[low] + nums[high]
        if s == target:
            res.append([nums[low], nums[high]])
            low += 1
            high -= 1
            # [-2, 0, 0, 2, 2] these two whiles solve this case
            while low <= high and nums[low] == nums[low - 1]:
                low += 1
            while high >= low and nums[high] == nums[high + 1]:
                high -= 1
        elif s < target:
            low += 1
            # skip duplicate
            while low <= high and nums[low] == nums[low - 1]:
                low += 1
        else:
            high -= 1
            # skip duplicate
            while high >= low and nums[high] == nums[high + 1]:
                high -= 1
    return res