def twoSum(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    i = 0
    dictNums = {}
    
    for a in nums:
        b = target - a
        if b in dictNums:
            return [dictNums[b],i]
        dictNums[a] = i
        i = i+1
    return []

if __name__ == "__main__":
    
    nums = [3, 1, 2, 8, 5]
    target = 10
    res = twoSum(nums, target)
    print(res)

