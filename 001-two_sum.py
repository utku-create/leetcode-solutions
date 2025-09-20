def two_sum(nums, target):
    hashmap = dict()
    for indeks, mevcut_sayi in enumerate(nums):
        aranan = target - mevcut_sayi

        if aranan in hashmap:
            return [hashmap[aranan], indeks]
        if aranan not in hashmap:
            hashmap[mevcut_sayi] = indeks

print(two_sum([2,7,11,19], 9))
print(two_sum([2,3,4], 6))