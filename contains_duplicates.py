nums = [1,2,3,1]


def containsDuplicate(nums: [int]) -> bool:
    hashset = set()
    for n in nums:
        if n in hashset:
            return True
        else:
            hashset.add(n)
    return False

print(containsDuplicate(nums))
