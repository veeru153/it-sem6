from collections import Counter

nums = [1,2,3,3,4,4,4,4,5,6,6,7,8,8,8,9,9,9,9,10,10];

def mean(nums = nums):
    n = len(nums)
    return sum(nums)/n

def median(nums = nums):
    n = len(nums)

    if n % 2 == 0:
        a = nums[n//2]
        b = nums[n//2 - 1]
        return (a-b)/2
    else:
        return nums[n//2]

def mode(nums = nums):
    n = len(nums)

    numCount = Counter(nums)
    countDict = dict(numCount)
    mode = [k for k, v in countDict.items() if v == max(list(numCount.values()))]
    return mode

print(f"Numbers: {nums}")

print(f"Mean: {mean(nums)}")
print(f"Median: {median(nums)}")
print(f"Mode(s): {mode(nums)}")