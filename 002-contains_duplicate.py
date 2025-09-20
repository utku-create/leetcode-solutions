def contains_duplicate(nums):
    hashmap = dict()

    for i, num in enumerate(nums):
        if num in hashmap:
            return True
        if num not in hashmap:
            hashmap[num] = i

    return False

print(contains_duplicate([1,3,2,1]))
print(contains_duplicate([1,3,2]))